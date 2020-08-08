#Converting feet and inches into cm
def feetConversion():
    #Take user input for feet and inches
    feet = int(input("Input your height in feet: "))
    inches = int(input("Input your height in inches: "))
    #Inches and feet multiplied by 12 
    inches += feet * 12
    #CM rounds inches by 2.54 to give final value
    cm = round(inches * 2.54, 1)
    print("Your height is: %d cm." % cm)

feetConversion()