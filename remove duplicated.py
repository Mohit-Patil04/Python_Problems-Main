nums = [1, 2, 2, 3, 4, 4, 5]

unique = []
for num in nums:
    if num not in unique:
        unique.append(num)

print(unique)