# Student ID = 2561586
# d1 = 6
# d2 = 8
# k = 4
# shift = -2
# rows_keep = 2

def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(row)
    print()


def main():
    d1 = 6
    d2 = 8
    k = (d1 + d2) % 4 + 2
    shift = d1 - d2
    rows_keep = (d1 % 2) + 2

    matrix = [
        [5, 10, 15, 20, 25],
        [30, 35, 40, 45, 50]
    ]

    print_matrix(matrix, "Original rectangular matrix:")

    # Component A
    print("Dimensions in words:")
    print(f"{len(matrix)} rows and {len(matrix[0])} columns")

    print("\nRows:")
    for row in matrix:
        print(row)

    last_column = [row[-1] for row in matrix]
    print("\nLast column:", last_column)

    first_3_cols = [row[:3] for row in matrix]
    print("\nAll rows, first 3 columns:")
    for row in first_3_cols:
        print(row)

    # Component B
    chosen_row = d1 % len(matrix)  # 6 % 2 = 0
    old_row = matrix[chosen_row][:]
    new_row = [value + k for value in old_row]
    matrix[chosen_row] = new_row

    start_col = d2 % 2  # 8 % 2 = 0
    sliced_subarray = [row[start_col:] for row in matrix]

    print("\nChosen row index:", chosen_row)
    print("Old row:", old_row)
    print("New row:", new_row)

    print_matrix(matrix, "Matrix after row replacement:")

    print("Sliced sub-array from starting column", start_col)
    for row in sliced_subarray:
        print(row)

# Explanation:
# d1 = 6 → chosen_row = 6 % number_of_rows = 6 % 2 = 0
# d2 = 8 → start_col = d2 % 2 = 8 % 2 = 0


if __name__ == "__main__":
    main()