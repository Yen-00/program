# Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    no_duplicates = list(set(numbers))
    no_duplicates.sort()
    return no_duplicates

# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0
    for num in arr:
        total = total + num
        result.append(total)
    return result

# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return lst[::step]

# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    total = 0
    for i in range(len(list1)):
        total = total + list1[i] * list2[i]
    return total

# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    result = [[0, 0], [0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]
    return result


# --- Quick tests to verify ---
print("Remove Duplicates and Sort:", remove_duplicates_and_sort([3, 1, 2, 3, 1]))
print("Cumulative Sum:", cumulative_sum([1, 2, 3, 4]))
print("Slice Every Nth:", slice_every_nth([1, 2, 3, 4, 5, 6], 2))
print("Dot Product:", dot_product([1, 2, 3], [4, 5, 6]))
print("Matrix Multiplication:", matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]))