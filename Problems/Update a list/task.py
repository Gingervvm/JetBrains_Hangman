numbers = [4, 1, 0, 3, 2, 5]
index = 0
for number in numbers:
    if number != index:
        numbers[index] = index
    index += 1
print(numbers)