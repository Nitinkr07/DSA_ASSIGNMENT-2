
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] 

rows = len(matrix)
cols = len(matrix[0])



print("Row Sums:")
for i in range(rows): 
    row_sum = 0
    for j in range(cols):
        row_sum += matrix[i][j]
    print(f"Row {i} sum = {row_sum}") 


print("\nColumn Sums:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Column {j} sum = {col_sum}") 


key = 5
found = False
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == key:
            print(f"\nElement {key} found at position ({i},{j})")
            found = True
            break
    if found:
        break
if not found:
    print(f"\nElement {key} not found") 


print("\nTranspose:")
transpose = []
for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transpose.append(new_row)

for row in transpose:
    print(row)   