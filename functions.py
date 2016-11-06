#AUTHENTICATE LOGIN PASSWORD

global conditionList
conditionList = ['PTSD', 'Anxiety', 'Alzheimers', 'Eating Disorders', 'Hepatitis', 'Cancer', 'Dementia', 'Schizophrenia', 'Paralysis', 'HIV/AIDS']
    
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


    zipcode = (input("Enter your primary Zip Code:"))

    while (zipcode.isdigit() == False or len(zipcode) != 5):
            zipcode = input("Please enter a valid zipcode:")
        


    typeChoice = int(input("Choose a primary type for your account: \n1.) Coping \n2.) Educator \n3.) Learner\n"))

    while (typeChoice > 3 or typeChoice < 1):
            typeChoice = int(input("Please enter a valid input: "))


    
    if (typeChoice == 1):
            accountType = "Coping"
 
            print("What is your primary condition/disability?")
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
            
            print("What is your primary condition/disability?")
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

            print("What condition/disability are you primarily interested in?")
            i = 1
            for item in conditionList:
                print(i,"-", item)
                i = i + 1
                    
            conChoice = input()
    
            while conChoice.isdigit == False:
                conChoice = input("Please enter valid option: ")

            condition = conditionList[int(conChoice)]

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





