

firstName = input("Enter First Name:")
while(firstName.isalpha() == False):
        firstName = input("Please enter a valid name. No numbers allowed!")
lastName = input("Enter Last Name:")
while(lastName.isalpha() == False):
        lastName = input("Please enter a valid name. No numbers allowed!")

name = firstName + " " + lastName


age = int(input("Enter Age:"))

while (age > 120 or age < 18):
	print("Please enter a valid age")
	age = int(input("Enter Age:"))


zipcode = (input("Enter your Zip Code:"))

while (zipcode.isdigit() == False or len(zipcode) != 5):
        zipcode = input("Please enter a valid zipcode:")
        


#condition = conditionList()


typeChoice = int(input("Choose a type for your account: \n1.) Coping \n2.) Educator \n3.)Learner\n"))

while (typeChoice > 3 or typeChoice < 1):
	typeChoice = int(input("Please enter a valid input: "))



if (typeChoice == 1):
	accountType = "Coping"
	ageMax = int(input("What is your maximum desired age for a partner?"))
	ageMin = int(input("What is your minimum desired age for a partner?"))
        #distPref = 1 if state is desired range and 2 if region is desired range
	distPref = int(input("What is your desired range for a partner?\n1.)State\n2.)Immediate Region"))
        
if (typeChoice == 2):
	accountType = "Educator"
if (typeChoice == 3):
	accountType = "Learner"

email = input("Please enter your email: \n")

#Checks to see if input is both valid and not already taken
#emailCheck()

password = input("Enter your password:\n")



