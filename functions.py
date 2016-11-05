#AUTHENTICATE LOGIN PASSWORD

    
def checkLoginPassword(email,password):

    f = open("data.csv","r")
    count = 0
    for line in f:
        cells = line.split(",")
        if cells[0] == email:
            if cells[1] == password:
                return True
            else:
                return False
            
    f.close()


        
#AUTHENTICATE EMAIL

def checkEmail(email):

    #opens file
    f = open("data.csv","r")
    
    if email in f.read():
        return 3
    if "@" not in email:
        return False
    if "." not in email.split('@')[1]:
        return False

    return True

    f.close()
        
#CONDITIONS LIST



def conditionList():
    #opens file
    f= open("data.csv","r")

    conditions = []

    #reads file and creates list of unique conditions
    for line in f:
        cells = line.split(",")
        if cells[5] not in conditions:
            conditions.append(cells[5])
    f.close()

    return conditions[1:-1]

    #CREATE NEW ACCOUNT

def createnewaccount():
    firstName = input("Enter First Name:")
    while(firstName.isalpha() == False):
            firstName = input("Please enter a valid name. No numbers allowed!")
    lastName = input("Enter Last Name:")
    while(lastName.isalpha() == False):
            lastName = input("Please enter a valid name. No numbers allowed!")

    name = firstName + " " + lastName


    age = input("Enter Age:")

    while (age.isdigit() == False):
            print("Please enter a valid age")
            age = input("Enter Age:")


    zipcode = (input("Enter your Zip Code:"))

    while (zipcode.isdigit() == False or len(zipcode) != 5):
            zipcode = input("Please enter a valid zipcode:")
        


    typeChoice = int(input("Choose a type for your account: \n1.) Coping \n2.) Educator \n3.) Learner\n"))

    while (typeChoice > 3 or typeChoice < 1):
            typeChoice = int(input("Please enter a valid input: "))



    if (typeChoice == 1):
            accountType = "Coping"
 
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

    email = input("Please enter your email: ")

    #Checks to see if input is both valid and not already taken
    check = 0
    while check == 0:
        if checkEmail(email)==False:
            email = input( "Invalid email. Please try again: " )
        if checkEmail(email)==3:
            email = input( "Email already taken. Please try again: ")
        if checkEmail(email)==True:
            check = 1
    password = input("Enter your password:")

    f = open("data.csv","a")
    f.write("\n" + email + "," + password + "," + name + "," + age + "," + zipcode + "," + condition + "," + accountType)






