#Gets list of conditions

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
