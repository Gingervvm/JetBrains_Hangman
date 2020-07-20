money_sum = int(input())
sheep_cost = 6769
cow_cost = 3848
pig_cost = 1296
goat_cost = 678
chicken_cost = 23
if money_sum >= sheep_cost:
    print(str(money_sum // sheep_cost) + " sheep")
elif money_sum >= cow_cost:
    print(str(money_sum // cow_cost) + " cows" if money_sum // cow_cost != 1 else "1 cow")
elif money_sum >= pig_cost:
    print(str(money_sum // pig_cost) + " pigs" if money_sum // pig_cost != 1 else "1 pig")
elif money_sum >= goat_cost:
    print(str(money_sum // goat_cost) + " goats" if money_sum // goat_cost != 1 else "1 goat")
elif money_sum >= chicken_cost:
    print(str(money_sum // chicken_cost) + " chickens" if money_sum // chicken_cost != 1 else "1 chicken")
else:
    print("None")