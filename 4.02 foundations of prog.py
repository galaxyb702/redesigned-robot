# Answer Key Lesson 04.02

# <student's first and last name>

# <the date>

 

# This program asks the user to move the turtle

# to the pond by providing input for turning

# left or right and moving forward or backward.

 

import turtle

 

def sunBurst(t):

    # Draw a pond.

    # move to position

    t.penup()

    x = 110

    y = 110

    t.setpos(x, y) #Sets the position of the turtle

    t.setheading(270)

    t.pendown()

    t.color( "blue" )

 

    # draw star

    for n in range(20):

        t.forward(60)

        t.left(100)

 

 

def printMenu():

    # This function prints the menu to the screen

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("~  Menu of Turtle Moves   ~")

    print("~  F: Move Forward        ~")

    print("~  B: Move Backward       ~")

    print("~  L: Turn Left           ~")

    print("~  R: Turn Right          ~")

    print("~  Q: Quit                ~")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

 

 

def main():

    t = turtle.Turtle()

    t.shape("turtle")

    t.speed(10)

 

    sunBurst(t)

 

    t.color("red")

    t.penup()

    t.setpos(0,0)

    t.pendown()

 

    choice = "-1"

    print("Try to move the turtle to the pond.")

    printMenu()   

 

    while(choice != "Q"):

 

        choice = input("How do you want to move the turtle? (f, b, l, r, q) ")

 

        if(choice == "F"):

            t.forward(10)

        elif(choice == "B"):

            t.backward(10)

        elif(choice == "L"):

            t.left(90)

        elif(choice == "R"):

            t.right(90)

        elif(choice == "Q"):

            print("Thank you!")

        else:

            print("I didn't understand your request, please try again.")

 

main()

 
