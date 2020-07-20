import math


def copysign_y_to_x(first, second):
    return math.copysign(first, second)


# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))
print(copysign_y_to_x(x, y))