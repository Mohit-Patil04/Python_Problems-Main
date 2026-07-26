def next_permutation(nums):
    n = len(nums)
    
    # Step 1: Find the break point
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    # Step 2: Swap with next greater element
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 3: Reverse the remaining part
    nums[i + 1:] = reversed(nums[i + 1:])
    
    return nums