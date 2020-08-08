import feetConversion, cmConversion

def getMenuChoice():
    #Prints menu options
    def menu():       
        print(30 * "-", "Height Calculator", 30 * "-")
        print("1. Feet and Inches Calculator ")
        print("2. CM Calculator ")       
        print("3. Exit Calculator ")
        print(83 * "-")

    loop = True
    int_choice = -1
    # While loop is True, continue iterating until False.
    while loop:          
        menu()    # Displays menu
        choice = input("Enter your choice [1-3]: ")

        if choice == '1':
            int_choice = 1
            #Calls addition function on choice
            feetConversion.feetConversion()
            loop = True
        elif choice == '2':
            int_choice = 2
            #Calls subtraction function on choice
            cmConversion.cmConversion()
            loop = True 
        elif choice == '3':
            int_choice = -1
            print("Exiting..")
            #Loop becomes False and exits the script
            loop = False  
        else:
            #Any value other than 1-5 will validate as an error message to loop back to the menu
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]

#Call the function to activate the menu
getMenuChoice()