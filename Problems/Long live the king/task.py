hor = int(input())
ver = int(input())
angle = [1, 8]
if 1 < hor < 8 and 1 < ver < 8:
    print(8)
elif hor in angle and ver in angle:
    print(3)
elif hor in angle and ver not in angle or hor not in angle and ver in angle:
    print(5)