import math
# the line below grabs the input and stores it as diameter.
#the int turns the input into a integer
diameter = int(input("Type the diameter of your circle:"))
# radius is just half the diameter
radius = diameter / 2
# formula for area 
area = math.pi * radius * radius
# formula for Circumference
circumference = 2 * math.pi * radius
# the two lines below display the answers
print ("your area is " + str(area))
print ("your circumference is " + str(circumference))
