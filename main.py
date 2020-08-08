import math

def conversionCalculator():
    print("Welcome to the height calculator!")
    print("Convert CM to Feet and Inches")
    cm = int(input("Input a number in cm format: "))
    feet = 0.0328084 * cm
    inches = 0.393701 * cm
    print("Your height is " , math.trunc(feet) ,"ft", round(inches,2), "inches")

conversionCalculator()