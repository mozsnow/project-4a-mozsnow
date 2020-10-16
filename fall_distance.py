def fall_distance(time):
    gravity = 9.8
    distance = ( 1 /2 ) * gravity * (time ** 2)
    return distance
def main():
    print( "Time Falling Distance" )
    for currentTime in range( 1, 5 ):
        print( currentTime, "\t", format( fall_distance( currentTime ),\
               ".2f" ) )
main()
""