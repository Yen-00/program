# Lecture 7: Lab 5 — Sensor List Builder and Calibrator

# Student ID = 2672601
# d1 = 1
# d2 = 0
# k = (1 + 0) % 4 + 2 = 3
# shift = 1 - 0 = 1
# rows_keep = (1 % 2) + 2 = 3

def main():

    d1 = 1
    d2 = 0
    k = (d1 + d2) % 4 + 2
    shift = d1 - d2
    rows_keep = (d1 % 2) + 2

    readings = []

    n = int(input("How many sensor readings will you enter? "))

    for i in range(n):
        value = float(input(f"Enter reading {i+1}: "))
        readings.append(value)

    print("Full list:", readings)

    if len(readings) == 0:
        print("The list is empty.")
        return

    print("First reading:", readings[0])
    print("Last reading:", readings[-1])

    if len(readings) >= 3:
        print("Slice from index 1 to index 3:", readings[1:3])
    else:
        print("Not enough values for slice.")

    print("Sum of readings:", sum(readings))

    shifted = [x + shift for x in readings]
    scaled = [x * k for x in readings]

    # zip() pairs elements from both lists by index.
    # If the lists have different lengths, zip() stops at the shortest list.
    zipped_sum = [a + b for a, b in zip(readings, shifted)]

    print("Shifted list:", shifted)
    print("Scaled list:", scaled)
    print("Element-wise sum (original + shifted):", zipped_sum)


if __name__ == "__main__":
    main()