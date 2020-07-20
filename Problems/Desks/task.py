first_group_num = int(input())
second_group_num = int(input())
third_group_num = int(input())
desc_count_1 = first_group_num // 2 + first_group_num % 2
desc_count_2 = second_group_num // 2 + second_group_num % 2
desc_count_3 = third_group_num // 2 + third_group_num % 2
print(desc_count_1 + desc_count_2 + desc_count_3)