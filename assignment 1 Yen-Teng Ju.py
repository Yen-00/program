# Programming in Science - Assignment 1


# -------------------------
# Question 1
# -------------------------

# Task 1 – Code
# Function checks if a number is positive, negative, or zero.

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


# Task 2 – Understanding
# Input:
#   number → the value being checked
#
# Output:
#   A string ("Positive", "Negative", or "Zero")
#
# Main variables:
#   number → the value passed into the function
#
# Functions used:
#   if, elif, else conditional statements
#
# Explanation:
# The function compares the number to zero.
# If the number is greater than zero it returns "Positive".
# If the number is less than zero it returns "Negative".
# Otherwise the number must be zero.


# Task 3 – Modification
# I modified the function to also identify even or odd numbers.

# Modified version (example):
# def check_number(number):
#     if number > 0:
#         if number % 2 == 0:
#             return "Positive Even"
#         else:
#             return "Positive Odd"
#     elif number < 0:
#         return "Negative"
#     else:
#         return "Zero"
#
# Explanation:
# This modification adds another check using the modulus operator
# to see if the number is even or odd.


# -------------------------
# Question 2
# -------------------------

# Task 1 – Code
# Function returns a star pattern.

def star_shape(rows):
    shape = ""
    for i in range(1, rows + 1):
        shape += "*" * i + "\n"
    return shape.strip()


# Task 2 – Understanding
# Input:
#   rows → number of rows to print
#
# Output:
#   A string showing the star pattern
#
# Main variables:
#   rows → total number of rows
#   i → loop counter
#   shape → stores the final pattern
#
# Functions used:
#   for loop
#   range()
#
# Explanation:
# The loop runs from 1 to the number of rows.
# Each loop adds a line with i stars.
# The pattern increases by one star each row.


# Task 3 – Modification
# I modified the function to use the symbol "#" instead of "*".

# Modified version:
# shape += "#" * i + "\n"
#
# Explanation:
# This changes the visual output of the pattern.


# -------------------------
# Question 3
# -------------------------

# Task 1 – Code
# Counts numbers and replaces multiples of 3.

def count_multiples_of_3(limit):
    num = 1
    result = ""
    while num <= limit:
        if num % 3 == 0:
            result += "Multiple of 3\n"
        else:
            result += str(num) + "\n"
        num += 1
    return result.strip()


# Task 2 – Understanding
# Input:
#   limit → the highest number to count to
#
# Output:
#   A string containing numbers or "Multiple of 3"
#
# Main variables:
#   num → current number being checked
#   result → stores the output text
#
# Functions used:
#   while loop
#   modulus operator %
#
# Explanation:
# The loop starts at 1 and continues until it reaches the limit.
# Each number is checked to see if it is divisible by 3.
# If it is divisible by 3, the text "Multiple of 3" is added.


# Task 3 – Modification
# I modified the function to also mark multiples of 5.

# Modified version:
# if num % 3 == 0:
#     result += "Multiple of 3\n"
# elif num % 5 == 0:
#     result += "Multiple of 5\n"
# else:
#     result += str(num) + "\n"
#
# Explanation:
# Now the function checks another condition.


# -------------------------
# Question 4
# -------------------------

# Task 1 – Code
# Sum of even numbers in a range.

def sum_of_even_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total


# Task 2 – Understanding
# Input:
#   start → starting value of the range
#   end → ending value of the range
#
# Output:
#   The sum of even numbers in that range
#
# Main variables:
#   total → stores the sum
#   num → current number being checked
#
# Functions used:
#   for loop
#   modulus operator %
#
# Explanation:
# The loop goes through each number in the range.
# If the number is even, it is added to the total.


# Task 3 – Modification
# I modified the function so it prints each even number being added.

# Modified version:
# if num % 2 == 0:
#     print("Adding:", num)
#     total += num
#
# Explanation:
# This helps visualize which numbers are included in the sum.


# -------------------------
# Main Function Block
# -------------------------

if __name__ == "__main__":

    print("Question 1:")
    number = int(input("Enter a number: "))
    print(check_number(number))

    print("\nQuestion 2:")
    rows = int(input("Enter number of rows: "))
    print(star_shape(rows))

    print("\nQuestion 3:")
    limit = int(input("Enter the limit: "))
    print(count_multiples_of_3(limit))

    print("\nQuestion 4:")
    start = int(input("Enter the start value: "))
    end = int(input("Enter the end value: "))
    print(sum_of_even_numbers(start, end))