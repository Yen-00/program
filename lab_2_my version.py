def calculate_height(h0, t):
    g = 9.8  
    height = h0 - 0.5 * g * t**2
    return round(height, 2)

def calculate_car_distance(t):

    dist = 20 * t
    return round(dist, 2)


if __name__ == '__main__':
    h0 = float(input("Enter initial height: "))
    t = float(input("Enter time: "))
    print(f"Height of the ball at time {t} second(s) = {calculate_height(h0, t)} meters")
    
    t = float(input("Enter time for car  "))
    dist = calculate_car_distance(t)
    print(f"distance is {dist} m")

