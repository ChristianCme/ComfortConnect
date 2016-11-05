# from Printnamesofmatch import match
from functions import createnewaccount
from functions import checkEmail
from functions import conditionList
from functions import checkLoginPassword
from match import match

print( "Welcome to ......." )

ender = 0
while ender==0:

    print( "Main Menu" )
    choice = int(input("1.) Log in to Profile\n" "2.) Create New Profile\n" "3.) Exit\n"))

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
        
            

        #if log in works
        #call function to check file of group type
        #use data found from type function to print names and emails of matching users

        #Search Info
        
        zipcode = (input("Enter your Zip Code:"))

        while (zipcode.isdigit() == False or len(zipcode) != 5):
                zipcode = input("Please enter a valid zipcode:")
        


        typeChoice = int(input("Choose a type for your account: \n1.) Coping \n2.) Educator \n3.) Learner\n"))

        while (typeChoice > 3 or typeChoice < 1):
                typeChoice = int(input("Please enter a valid input: "))



        if (typeChoice == 1):
                accountType = "Coping"
                ageMax = int(input("What is your maximum desired age for a partner? "))
                ageMin = int(input("What is your minimum desired age for a partner? "))
                #distPref = 1 if state is desired range and 2 if region is desired range
                while(ageMax<ageMin):
                    ageMin = int(input("Incorrect value. Please try again: "))
                while ageMax <= 0:
                    ageMax = int(input("Incorrect value. Please try again: "))
                while ageMin < 0:
                    ageMin = int(input("Incorrect value. Please try again: "))
                    
                distPref = int(input("What is your desired range for a partner?\n1.) State\n2.) Immediate Region\n3. No Range Limit "))
            
                print("What is your condition/disability?")
                conLength = len(conditionList())
                conditions = conditionList()
                for i in range(1, conLength):
                    print(i,"-", conditions[i])

                print("Or Type New Condition/Disability")
                conChoice = input()
    
                if conChoice.isdigit == True:
                    conChoice = int(conChoice)
                    condition = conditions[conChoice]
                else:
                    condition = conChoice
        
        if (typeChoice == 2):
                accountType = "Educator"
                ageMax = 120
                ageMin = 0
                print("What is your condition/disability?")
                conLength = len(conditionList())
                conditions = conditionList()
                for i in range(1, conLength):
                    print(i,"-", conditions[i])
                    
                print("Or Type New Condition/Disability")
                conChoice = input()
    
                if conChoice.isdigit == True:
                    conChoice = int(conChoice)
                    condition = conditions[conChoice]
                else:
                    condition = conChoice
                    
            
        if (typeChoice == 3):
                accountType = "Learner"
                ageMax = 120
                ageMin = 0
                

                print("What condition/disability would you like to learn about?")
                conLength = len(conditionList())
                conditions = conditionList()
                for i in range(1, conLength):
                    print(i,"-", conditions[i])
    
                print("Or Type New Condition/Disability")
                conChoice = input()

                if conChoice.isdigit == True:
                    conChoice = int(conChoice)
                    condition = conditions[conChoice]
                else:
                    condition = conChoice

        
        print( match(ageMax, ageMin, zipcode, distPref, condition, group))
        



    if ( choice == 2 ):
        print( "Creating new profile" )
        #call jonahs function
        createnewaccount()
        print( "Your new account has been created!" )
        #return to menu
        ender = 0

    if( choice == 3 ):
        print( "Goodbye!" )
        ender = 1
        
