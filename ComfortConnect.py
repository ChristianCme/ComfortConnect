# from Printnamesofmatch import match
from functions import createnewaccount
from functions import checkEmail
from functions import checkLoginPassword
from match import match

print( "Welcome to The Comfort Connection\n" )

global conditionList
conditionList = ['PTSD', 'Anxiety', 'Alzheimers', 'Eating Disorders', 'Hepatitis', 'Cancer', 'Dementia', 'Schizophrenia', 'Paralysis', 'HIV/AIDS']


ender = 0
while ender==0:

    print( "Main Menu" )
    choice = input("1.) Log in to Profile\n" "2.) Create New Profile\n" "3.) Exit\n")
    while (choice.isdigit() == False):
        print("Invalid input. Please try again")
        choice = input("1.) Log in to Profile\n" "2.) Create New Profile\n" "3.) Exit\n")

    
    choice = int(choice)
    
    if ( choice>3 or choice<1 ):
        print( "Invalid input.Please try again" )
        ender = 0
    if ( choice == 1 ):
        email = input( "Enter email: " )
        
        
        while (checkEmail(email)!=3):
            email = input( "Email does not exist\n" "Please try again: " )
            
        
        
        
        #if email passes
        password = input( "Enter Password: " )
        while checkLoginPassword(email, password)==False:
            password = input( "Incorrect password\n" "Try again: " )
        
        print("Login Successful\n")
        print("COMFORT CONNECTION MATCHING PROGRAM\n")

        #if log in works
        #call function to check file of group type
        #use data found from type function to print names and emails of matching users

        #Search Info
        
        zipcode = (input("Enter a Zip Code for this session:"))

        while (zipcode.isdigit() == False or len(zipcode) != 5):
                zipcode = input("Please enter a valid zipcode of 5 digits:")
        


        typeChoice = int(input("Choose an account type for this session: \n1.) Coping \n2.) Educator \n3.) Student\n"))

        while (typeChoice > 3 or typeChoice < 1):
                typeChoice = int(input("Please enter a valid input: "))


        distPref = 0
        if (typeChoice == 1):
                accountType = "Coping"
                ageMax = int(input("What is your MAXIMUM desired age for a partner? "))
                while ageMax <= 0:
                    ageMax = int(input("Incorrect value. Please try again: "))
                ageMin = int(input("What is your MINIMUM desired age for a partner? "))
                #distPref = 1 if state is desired range and 2 if region is desired range
                while ageMin < 0:
                    ageMin = int(input("Incorrect value. Please try again: "))
                    
                while(ageMax<ageMin):
                    ageMin = int(input("Incorrect min value. Please try again: "))
                    ageMax = int(input("Incorrect max value. Please try again: "))
                
                    
                distPref = int(input("What is your desired range for a partner?\n1.) State\n2.) Immediate Region\n3.) No Range Limit\n"))
            
                print("What condition/disability would you like to discuss today?")
                i = 1
                for item in conditionList:
                    print(i,"-", item)
                    i = i + 1
                    
                conChoice = input()
    
                while conChoice.isdigit == False:
                    conChoice = input("Please enter valid option: ")

                condition = conditionList[int(conChoice)]
        
        if (typeChoice == 2):
                accountType = "Educator"
                ageMax = 120
                ageMin = 0

                distPref = int(input("What is your desired range for a partner?\n1.) State\n2.) Immediate Region\n3.) No Range Limit\n"))
                
                print("What condition/disability are you interested in teaching about today?")
                i = 1
                for item in conditionList:
                    print(i,"-", item)
                    i = i + 1
                    
                conChoice = input()
    
                while conChoice.isdigit == False:
                    conChoice = input("Please enter valid option: ")

                condition = conditionList[int(conChoice)]
                    
            
        if (typeChoice == 3):
                accountType = "Student"
                ageMax = 120
                ageMin = 0
                
                distPref = int(input("What is your desired range for a partner?\n1.) State\n2.) Immediate Region\n3.) No Range Limit\n"))

                print("What condition/disability would you like to learn about today?")
                i = 1
                for item in conditionList:
                    print(i,"-", item)
                    i = i + 1
                    
                conChoice = input()
    
                while conChoice.isdigit == False:
                    conChoice = input("Please enter valid option: ")

                condition = conditionList[int(conChoice)]

        print(match(ageMin, ageMax, zipcode, distPref, condition, accountType))
        



    if ( choice == 2 ):
        print( "Creating new profile" )
        #call jonahs function
        createnewaccount()
        print( "Your new account has been created!" )
        #return to menu
        ender = 0

    if( choice == 3 ):
        print( "Goodbye! Thanks for visiting The Comfort Connection!" )
        ender = 1
        
