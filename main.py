#Imported to math.trunc to remove decimal places
import math

#Converts value from cm to ft and inches
def conversionCalculator():
    print("Welcome to the height calculator!")
    print("Convert CM to Feet and Inches")
    cm = int(input("Input a number in cm format: "))
    #Gives answer in ft
    feet = 0.0328084 * cm
    #Takes remainder of ft after decimal place
    inches = feet % 1
    #Multiply by 12 to get the remainder of feet
    ans = inches * 12
    print("Your height is " , math.trunc(feet) ,"ft", round(ans), "inches")

