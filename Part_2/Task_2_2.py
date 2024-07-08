import random

random_list = [random.randint(-10, 10) for _ in range(20)]

min_value = random_list[0]
max_value = random_list[0]
negative_count = 0
positive_count = 0
zero_count = 0

for number in random_list:
    if number < min_value:
        min_value = number
    if number > max_value:
        max_value = number
    if number < 0:
        negative_count += 1
    elif number > 0:
        positive_count += 1
    else:
        zero_count += 1

print("List of random numbers:", random_list)
print("Minimum element:", min_value)
print("Maximum element:", max_value)
print("Number of negative elements:", negative_count)
print("Number of positive elements:", positive_count)
print("Number of zeros:", zero_count)
