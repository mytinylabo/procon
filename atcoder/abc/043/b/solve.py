strokes = input().strip()
display = []

for s in strokes:
    if s == "B":
        if display:
            display.pop()
    else:
        display.append(s)

print("".join(display))
