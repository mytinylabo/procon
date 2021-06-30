A, B = map(int, input().split())

if A == B:
    print("Draw")
elif {A, B} == {1, 13}:
    print("Alice" if A < B else "Bob")
else:
    print("Alice" if A > B else "Bob")
