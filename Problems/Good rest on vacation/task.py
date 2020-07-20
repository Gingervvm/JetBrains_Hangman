days = input()
day_food_cost = input()
flight_cost = input()
hotel_night_cost = input()
duration = int(days)
food_cost = int(day_food_cost) * duration
hotel_cost = int(hotel_night_cost) * (duration - 1)
print(food_cost + hotel_cost + int(flight_cost) * 2)