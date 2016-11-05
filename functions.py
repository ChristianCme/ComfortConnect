#CREATE NEW ACCOUNT

def createnewaccount():
    from functions import conditionList
    from functions import checkEmail
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
            ageMax = int(input("What is your maximum desired age for a partner? "))
            ageMin = int(input("What is your minimum desired age for a partner? "))
            #distPref = 1 if state is desired range and 2 if region is desired range
            distPref = int(input("What is your desired range for a partner?\n1.)State\n2.)Immediate Region\n"))
            print( conditionList())
        
    if (typeChoice == 2):
            accountType = "Educator"
            print( conditionList())
    if (typeChoice == 3):
            accountType = "Learner"

    email = input("Please enter your email: ")

    #Checks to see if input is both valid and not already taken
    while checkEmail(email)=="False":
        email = input( "Invalid email. Please try again: " )
    
    
    password = input("Enter your password:\n")



#AUTHINTCATE PASSWORD


def checkPassword(email, password):
	users = []

	#opens file
	f = open("data.csv", "r")
	
	#reads file and creates list of users and passwords
	for line in f:
		cells = line.split(",")
		users.append(cells[0:2])

	count = 0
	usermatch = "False"

	#Looks for inputted user name
	for user in users:
		if user[0] == email:
				break
		count = count + 1

	usermatch = count

	#If username is not found
	if usermatch == "False":
		return 3

	#Splits line of correct user and checks password
	if users[usermatch][1] == password:
		return True
	else:
		return False

	f.close()


#AUTHINTICATE EMAIL

def checkEmail(email):
	users = []

	#opens file
	f = open("data.csv", "r")
	
	#reads file and creates list of users and passwords
	for line in f:
		cells = line.split(",")
		users.append(cells[0])


	#Looks for inputted user name
	for user in users:
		if user == email:
				return False

	if "@" not in email:
		return False
	
	if "." not in email.split('@')[1]:
		return False

	return True

	f.close()


#CONDITIONS LIST



def conditionList():
	#opens file
	f = open("data.csv", "r")
	
	conditions = []

	#reads file and creates list of unique conditions
	for line in f:
		cells = line.split(",")
		if cells[5] not in conditions:
			conditions.append(cells[5])

	f.close()

	return conditions[1:-1]



