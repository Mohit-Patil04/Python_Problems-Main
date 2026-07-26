def spiral_order(matrix):
    result = []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Left → Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Top → Bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Right → Left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # Bottom → Top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


# ---- User Input ----
r = int(input("Enter rows: "))
c = int(input("Enter cols: "))

matrix = []
print("Enter matrix:")

for _ in range(r):
    matrix.append(list(map(int, input().split())))

# ---- Output ----
print("Spiral Order:")
print(*spiral_order(matrix))