gravity = 9.8
def main():
    intro()
    beginning_second = 1 # the beginning of the fall
    final_second = 11 # the end of a fall
    print()
    print ( "Time(second) \tDistance (meters)") # headers for the table
    # the loop to calculate per second fall distance
    for time in range (beginning_second, final_second):
        # the loop uses arguments for beginning and ending time
        distance = falling_distance(time)
        # argument time comes from argument t in the function below
        print(time, '\t\t', format(distance, ',.2f'))
def falling_distance(t):
    # definition of the falling distance function
    g = gravity
    return (1/2*g*(t**2)) # the distance value is being returned