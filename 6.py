def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(row)
    print()


def main():
    # Personalization values (student ID last digit = 1, second-last = 0)
    d1 = 1
    d2 = 0
    k = (d1 + d2) % 4 + 2   # = (1 + 0) % 4 + 2 = 3
    shift = d1 - d2           # = 1 - 0 = 1
    rows_keep = (d1 % 2) + 2  # = (1 % 2) + 2 = 3

    # Component A: Build the matrix
    matrix = [
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32]
    ]

    # Print full matrix
    print_matrix(matrix, "Original matrix:")

    # Print one specific element
    print("Specific element matrix[1][2]:", matrix[1][2])

    # Print first two rows
    print("First two rows:", matrix[:2])

    # Print first column
    first_column = [row[0] for row in matrix]
    print("First column:", first_column)

    # Print upper-left 2x2 sub-array
    upper_left_2x2 = [row[:2] for row in matrix[:2]]
    print("Upper-left 2x2 sub-array:", upper_left_2x2)
    print()

    # Component B: ID-based modification
    row_index = d1 % len(matrix)        # 1 % 3 = 1
    col_index = d2 % len(matrix[0])     # 0 % 4 = 0

    # Identify which row and column are being changed
    print(f"Modifying row {row_index} (d1 % number_of_rows = {d1} % {len(matrix)})")
    print(f"Modifying column {col_index} (d2 % number_of_columns = {d2} % {len(matrix[0])})")
    print()

    # Add shift to every value in row_index
    for j in range(len(matrix[row_index])):
        matrix[row_index][j] += shift

    # Multiply every value in col_index by k
    for i in range(len(matrix)):
        matrix[i][col_index] *= k

    # Print modified matrix
    print_matrix(matrix, "Modified matrix:")

    # Print sub-array using first rows_keep rows and first k columns
    sub_array = [row[:k] for row in matrix[:rows_keep]]
    print(f"Sub-array (first {rows_keep} rows, first {k} columns):")
    for row in sub_array:
        print(row)


if __name__ == "__main__":
    main()

# Personalization values:
# d1 = 1, d2 = 0, k = 3, shift = 1, rows_keep = 3

# Component B logic:
# row_index = 1 % 3 = 1 -> modify second row (index 1)
# col_index = 0 % 4 = 0 -> modify first column (index 0)
# Add shift (1) to row 1: [25,26,27,28] -> [26,27,28,29]
# Multiply column 0 by k (3): 21->63, 26->78, 29->87

# Modified matrix result:
# [63, 22, 23, 24]
# [78, 27, 28, 29]
# [87, 30, 31, 32]

# Sub-array (rows_keep=3, k=3):
# [63, 22, 23]
# [78, 27, 28]
# [87, 30, 31]