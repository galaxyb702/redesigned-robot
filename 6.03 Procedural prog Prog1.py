#Hamza Hamza
#4/15/2025
#The purpose is Major Indescision (help students select their majors)

def menuSelection():
	print("1. Business Administration")
	print("2. Health and Clinical Sciences")
	print("3. Social Sciences")
	print("4. Bio-Medical Sciences")
	print("5. Communications")
	selection = int(input("Type the number corresponding to the topic you want to look into"))
	quiz(selection)

def average(quizScore):
	total = sum(quizScore)
	length = len(quizScore)
	avg = total / length
	return avg


#Get the average grade from last five quizzes of the selected option.  
#     print average of the list 
	 
def quiz(selection):
	quizScore = []
	print("Please provide the last 5 quiz scores of your ")
	if selection == 1:
		print("Math Scores")
		
		for score in range(1,6):
			mscore=int(input("What was your score for math's "))
			quizScore.append(mscore)
	elif selection == 2:
		print("Biology Scores")
		for score in range(1,6):
			bscore= int(input("What was your score for biology's "))
			quizScore.append(bscore)
	elif selection == 4:
		print("Biology Scores")
		for score in range(1,6):
			bscore= int(input("What was your score for biology's "))
			quizScore.append(bscore)
	elif selection == 3:
		print("Social Science Scores")
		for score in range(1,6):
			sscore = int(input("What was your score for biology's "))
			quizScore.append(sscore)
	elif selection == 5:
		print("Language Arts Scores")
		for score in range(1,6):
			lscore = int(input("What was your score for language arts's "))
			quizScore.append(lscore)
	avg = average(quizScore)
	if avg > 70:
		display(selection)
	else:
		menuSelection()
		
def display(selection):
	if selection == 1:
		print("Here are more details about Business Administration:")
	elif selection == 2:
		print("Here are more details about Health and Clinical Sciences:")
	elif selection == 3:
		print("Here are more details about Social Sciences:")
	elif selection == 4:
		print("Here are more details about Bio-Medical Sciences:")
	elif selection == 5:
		print("Here are more details about Communications:")

def main():
	menuSelection()
main()

