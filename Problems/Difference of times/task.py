first_hour = input()
first_mins = input()
first_seconds = input()
second_hour = input()
second_mins = input()
second_seconds = input()
print(int(second_seconds) + int(second_mins) * 60 + int(second_hour) * 3600 - (int(first_seconds) + int(first_mins) * 60 + int(first_hour) * 3600))