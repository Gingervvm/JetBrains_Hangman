min_sleep = int(input())
max_sleep = int(input())
current_sleep = int(input())
if current_sleep < min_sleep:
    print("Deficiency")
elif current_sleep > max_sleep:
    print("Excess")
else:
    print("Normal")
