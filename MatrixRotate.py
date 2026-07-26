def rotate(matrix):
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()

    return matrix


# ---- User Input ----
n = int(input("Enter size of matrix (n x n): "))

matrix = []
print("Enter the matrix row-wise:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# ---- Rotate ----
rotate(matrix)

# ---- Output ----
print("Rotated Matrix:")
for row in matrix:
    print(*row)