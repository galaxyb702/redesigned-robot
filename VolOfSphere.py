#pavati 
#11/19/2025
#this program will calculate volume and surface area of a sphere

from math import *
#Output: 
def main():
    print("Jim is writing a report about planets")
    print("For fun facts, he wants to calculate the volume and surface area for a planet")
    print("He needs your help by providing the name of the planet and its radius")
	
    #Input:
    name = input ("please enter the name of the planet")
    radius = float (input("please enter the radius of the planet"))
    #Processing 
    surfaceArea = 4 * 3.14 *pow(radius, 2)
    vol = 4/3 * 3.14 * pow (radius, 3)
    #Output:
    print ("the planet "+ name + "with a radius of "+ str (radius))
    print ("the surface area of "+ name + " is "+str (surfaceArea))
    print ("the volume of "+ name + " is "+ str (vol))
main()