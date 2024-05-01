 

# <student's first and last name>
# <the date>
 
# This program will calculate distance between two points.
 
from math import *
 
def calcDistance(x1, y1, x2, y2):
    # Returns distance between two points
 
    distance = sqrt( pow( x2 - x1, 2) + pow(y2 - y1, 2) )
    return distance
 
 
def main():
 
    # Values for x and y. Variety of values include integers, floats, positive, and negative
    x1 = [4, 5, 0, 9.8, 24]
    y1 = [4, 5, 0, 9.8, -12]
    x2 = [3, 5, -7, 5.5, -2]
    y2 = [3, 5, -4, 2.2, 9]
 
    listLen = len(x1)
 
    print("Distance between Two Points")
    print(" x1, y1    x2, y2    Distance")
    for n in range(0, listLen):
 
        d = calcDistance(x1[n], y1[n], x2[n], y2[n])
        print(" " + str(x1[n]) + ", "+ str(y1[n]) + "       "+ str(x2[n]) + ", "+ str(y2[n]) + "     " +" " + str(d))
 
main() 
