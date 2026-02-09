def weekday(day_number):
    if day_number < 1 or day_number > 7:
        return "Not a proper day number!"
    
    if 1 <= day_number <= 5:
        return "It is a Weekday!"
    else:
        return "It is a Weekend!"

def name(day_number):
    if day_number == 1:
        return "It is a Monday!"
    elif day_number == 2:
        return "It is a Tuesday!"
    elif day_number == 3:
        return "It is a Wednesday!"
    elif day_number == 4:
        return "It is a Thursday!"
    elif day_number == 5:
        return "It is a Friday!"
    elif day_number == 6:
        return "It is a Saturday!"
    elif day_number == 7:
        return "It is a Sunday!"
    else:
        return "Not a proper day number!"
    

if __name__ == '__main__':
    day_number = int(input("Enter a day number (1-7): "))
    print(weekday(day_number))

    
    print(name(day_number)) 