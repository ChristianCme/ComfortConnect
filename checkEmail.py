#checks if email is already taken and if valid email

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