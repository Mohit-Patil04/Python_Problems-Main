def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Start only if it's the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            count = 1

            while current + 1 in num_set:
                current += 1
                count += 1

            longest = max(longest, count)

    return longest