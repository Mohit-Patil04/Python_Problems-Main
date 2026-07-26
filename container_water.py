def maxArea(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        area = h * w
        
        max_water = max(max_water, area)
        
        # Move the smaller height pointer
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water