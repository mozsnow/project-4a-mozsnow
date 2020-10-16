def fall_distance(time):
    gravity = 9.8
    distance = 0.5 *gravity *(time ** 2)
    return distance
print('\n' + '\033[4m' + 'Time (s) Distance Fallen (m)' + '\033[0m')
for seconds in range(1,7):
    distance_fallen = fall_distance(seconds)
    print(' ' + format(seconds, '<d'), format(distance_fallen, '10.1f'))