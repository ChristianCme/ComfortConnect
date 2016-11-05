#Authentication system


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



	


