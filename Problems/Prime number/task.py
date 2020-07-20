number = int(input())
i = 2
while i <= number/2:
    if number % i == 0:
        print("This number is not prime")
        break
    i += 1
else:
    print("This number is prime") if number not in (0, 1) else print("This number is not prime")