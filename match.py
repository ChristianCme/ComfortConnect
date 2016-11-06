#series of functions to return matches

global conditionList
conditionList = ['PTSD', 'Anxiety', 'Alzheimers', 'Eating Disorders', 'Hepatitis', 'Cancer', 'Dementia', 'Schizophrenia', 'Paralysis', 'HIV/AIDS']


def ageMatch(ageMin, ageMax):
	#opens file
	f = open("data.csv", "r")
	
	matches = []

	#reads file and creates list of matches based on max and min ages
	next(f)
	for line in f:
		cells = line.split(",")
		if int(cells[3]) >= int(ageMin) and int(cells[3]) <= int(ageMax):
			matches.append(cells)

	f.close()
        
	return matches

def zipMatch(zipcode, distPref):
	#distPref 1 = State 2 = Immediate region
	#opens file
	f = open("data.csv", "r")
	
	matches = []

	#reads file and creates list of based on location
	for line in f:
		cells = line.split(",")
		if distPref == 1:
			if cells[4][0] == str(zipcode)[0]:
				matches.append(cells)
		if distPref == 2:
			if cells[4][0:3] == str(zipcode)[0:3]:
				matches.append(cells)
		if distPref == 3:
			matches.append(cells)

	f.close()

	return matches


def conditionMatch(condition):
	#opens file
	f = open("data.csv", "r")
	
	matches = []

	#reads file and creates list of based on location
	for line in f:
		cells = line.split(",")
		if cells[5] == condition:
			matches.append(cells)

	f.close()

	return matches

def groupMatch(group):
	#Matches all coping with coping and matches student and educator with the other
	#opens file
	f = open("data.csv", "r")
	
	matches = []

	#reads file and creates list of based on location
	for line in f:
		cells = line.split(",")
		if group == "Coping":
			if cells[6][:-1] == "Coping":
				matches.append(cells)
		if group == "Student":
			if cells[6][:-1] == "Educator":
				matches.append(cells)
		if group == "Educator":
			if cells[6][:-1] == "Student":
				matches.append(cells)

	f.close()

	return matches

def match(ageMin, ageMax, zipcode, distPref, condition, group):
	#Compares all of the results and gets total matches
	
	agematchs = ageMatch(ageMin, ageMax)
	zipmatches = zipMatch(zipcode, distPref)
	conditionmatches = conditionMatch(condition)
	groupmatches = groupMatch(group)

	matches1 = []
	matches2 = []
	finalmatches = []

	for line1 in agematchs:
		for line2 in zipmatches:
			if line1 == line2:
				matches1.append(line1)

	for line1 in conditionmatches:
		for line2 in groupmatches:
			if line1 == line2:
				matches2.append(line1)

	for line1 in matches1:
		for line2 in matches2:
			if line1 == line2:
				finalmatches.append(line1)

	return finalmatches