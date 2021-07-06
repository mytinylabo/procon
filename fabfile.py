import os
import re
import hashlib
from pathlib import Path

from invoke import task, run
from invoke.exceptions import UnexpectedExit, CommandTimedOut

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

TIMEOUT_SEC = 10


def do_test(basedir, solver_file, cases_file):
    solver = Path(basedir, solver_file)
    cases = Path(basedir, cases_file)

    # テストケースを読み込む
    blocks = re.split(r"\n{2,}", open(cases, "r").read())
    if len(blocks) == 0 or len(blocks) % 2 != 0:
        print("input-output pair mismatch\n")
        return

    print(solver)

    results = []

    for i in range(0, len(blocks), 2):
        # 入力
        feed = blocks[i].strip() + "\n"

        if feed.upper().startswith("#SKIP"):
            # テストケースを飛ばす
            results.append("SK")
            continue

        # 解答
        answer = re.sub(r"^#BLANK",
                        "",
                        blocks[i + 1].strip(),
                        flags=re.IGNORECASE) + "\n"

        print(f"==== case {(i // 2) + 1} ====")
        print(answer.strip())
        print("----------------")
        try:
            # スクリプト実行
            result = run(f"time python {solver} <<EOF\n{feed}EOF\n",
                         timeout=TIMEOUT_SEC)
            if answer.strip().upper() == "#DONTCARE":
                # 解答なしケース
                results.append("DC")
            else:
                # 解答ありケースは stdout と比較
                results.append("AC" if result.stdout == answer else "WA")

        except UnexpectedExit:
            # solve.py の実行時エラーのとき
            # Invoke 側のスタックトレースを省くための握り潰し。
            # 他の異常終了も潰しそうだけど困った時に考える
            break

        except CommandTimedOut:
            # タイムアウトが発生したら以降のケースを中断する
            print(f"Execution timed out: over {TIMEOUT_SEC} seconds.")
            print("Test aborted.")
            break

        print()

    print(" ".join(results))
    print()


class AutoTestHandler(PatternMatchingEventHandler):
    def __init__(self, basedir, targets):
        super().__init__(targets)
        self.basedir = basedir
        self.filehash = {}
        self.targets = targets

    def on_modified(self, event):
        # ファイルの内容変更がある場合のみテストを実行する
        new_stamp = hashlib.sha1(open(event.src_path, "rb").read()).hexdigest()
        if old_stamp := self.filehash.get(event.src_path):
            if old_stamp == new_stamp:
                # 更新無し
                return

        self.filehash[event.src_path] = new_stamp

        msg = f"Modified on {event.src_path}"
        hr = ("=-" * (len(msg) // 2)) + "="
        print(f"\n{hr}\n{msg}\n")

        do_test(self.basedir, *self.targets)

        print(f'Watching "{self.basedir}" ...')
        print("cmd >> ", end="", flush=True)


@task
def procon(_, path, retry=False):
    basedir = Path(path)
    os.makedirs(basedir, exist_ok=True)

    solver_file = "solve.py" if not retry else "solve_retry.py"
    cases_file = "cases.txt"

    solver = Path(basedir, solver_file)
    cases = Path(basedir, cases_file)

    solver.touch()
    cases.touch()

    # VSCode でファイルを開く
    run(f"code {solver}")
    run(f"code {cases}")

    watch(path, solver_file, cases_file)


def watch(path, solver_file, cases_file):
    basedir = Path(path)
    observer = Observer()
    observer.schedule(AutoTestHandler(basedir, [solver_file, cases_file]),
                      basedir)

    print(f'Start watching "{basedir}" ...')
    observer.start()

    solver = Path(basedir, solver_file)
    gencase = Path(basedir, "gencase.py")
    bigcase = Path(basedir, "bigcase.txt")

    try:
        while cmd := input("cmd >> "):
            try:
                if cmd == "g":
                    # テストケース生成スクリプトを実行
                    gencase.touch()
                    run(f"python {gencase}", echo=True)

                elif cmd == "b":
                    # テストケース生成スクリプトを実行し、すぐにソルバに食わせる
                    # 大規模データのテストに使う想定なので
                    # bigcase.txt というファイルに生成したケースを保存する
                    gencase.touch()
                    run(f"python {gencase}>{bigcase}", echo=True)
                    run(f"time python {solver}<{bigcase}", echo=True)

            except UnexpectedExit:
                continue

    except KeyboardInterrupt:
        observer.unschedule_all()
        print("Finishing...")
        observer.stop()

    observer.join()
    print("Done.")
