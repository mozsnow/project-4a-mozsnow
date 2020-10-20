def func():
    print ( "Time\tFalling Distance\n" )
  print( currentTime,"\t", "\t", fall_distance( currentTime ) )
def fall_distance(time):
    gravity = 9.8
    distance = (1 / 2) * gravity * (time ** 2)
    return distance