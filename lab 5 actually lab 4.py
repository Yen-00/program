# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    row = 1
    while row <= n:
        if row == 1 or row == n:
            result += '*' * n + '\n'
        else:
            result += '*' + ' ' * (n - 2) + '*' + '\n'
        row += 1
    return result.strip()  # Removes the trailing newline

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    row = 1
    while row <= n:
        number = 1
        line = ""
        while number <= row:
            line += str(number)
            number += 1
        result += line + '\n'
        row += 1
    return result.strip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    row = 1
    while row <= n:
        spaces = ' ' * (n - row)       # spaces to push the stars to the right
        stars = '*' * (2 * row - 1)    # number of stars in the row
        result += spaces + stars + '\n'
        row += 1
    return result


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    print("Hollow Square:")
    print(hollow_square(n))
    
    print("\nNumber Pattern:")
    print(number_pattern(n))
    
    print("\nSum of Natural Numbers:")
    print(sum_of_natural_numbers(n))
    
    print("\nCentered Star Pyramid:")
    print(centered_star_pyramid(n))