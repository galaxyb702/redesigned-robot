#Rashmi Ramesh
#4/15/2025
#The purpose is Major Indescision (help students select their majors)

def menuSelection():
	print("1. Engineering")
	print("2. Health and Clinical Sciences")
	print("3. Business Administration")
	print("4. Bio-Medical Sciences")
	print("5. Communications and Journalism")
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
	print("Please provide the last 5 quiz scores of your selected subject:\n")
	if selection == 1:
		print("Math Scores")
		
		for score in range(1,6):
			mscore=int(input("Quiz " + str(score) + "/5 - Enter your Math score (0-100): "))
			quizScore.append(mscore)
	elif selection == 2 or selection == 4:
		print("Biology Scores")
		for score in range(1,6):
			bscore= int(input("Quiz " + str(score) + "/5 - Enter your Biology score (0-100): "))
			quizScore.append(bscore)
	elif selection == 3 or  selection == 5 :
		print("Language Arts Scores")
		for score in range(1,6):
			lscore = int(input("Quiz " + str(score) + "/5 - Enter your Language Arts score (0-100): "))
			quizScore.append(lscore)
	avg = average(quizScore)
	print("Your average score for the last 5 quizzes is: " + str(avg))
	if avg >= 90:
		display(selection)
	else:
		menuSelection()
		
def display(selection):
	if selection == 1:
		print("Here are more details about Engineering:")
		print("  - Career Paths: Mechanical, Civil, Electrical, Software Engineer")
		print("  - Key Skills: Problem-solving, Physics, Mathematics, CAD Design")
		print("  - Typical Courses: Calculus, Thermodynamics, Materials Science, Circuit Design")
		print("  - Average Salary: $70,000 - $120,000+")
		print("  - Job Growth: Strong demand across industries")
	elif selection == 2:
		print("Here are more details about Health and Clinical Sciences:")
		print("  - Career Paths: Nurse, Physical Therapist, Physician Assistant, Radiologist")
		print("  - Key Skills: Attention to detail, Compassion, Scientific knowledge, Communication")
		print("  - Typical Courses: Anatomy, Physiology, Microbiology, Pharmacology, Clinical Practice")
		print("  - Average Salary: $60,000 - $150,000+")
		print("  - Job Growth: High demand in healthcare sector")
	elif selection == 3:
		print("Here are more details about Business Administration:")
		print("  - Career Paths: Manager, Financial Analyst, Entrepreneur, Consultant")
		print("  - Key Skills: Leadership, Data Analysis, Strategic Planning, Communication")
		print("  - Typical Courses: Accounting, Economics, Management, Marketing, Finance")
		print("  - Average Salary: $55,000 - $130,000+")
		print("  - Job Growth: Moderate demand across all sectors")
	elif selection == 4:
		print("Here are more details about Bio-Medical Sciences:")
		print("  - Career Paths: Biomedical Engineer, Research Scientist, Medical Device Developer")
		print("  - Key Skills: Biology, Chemistry, Problem-solving, Lab skills, Data analysis")
		print("  - Typical Courses: Molecular Biology, Biochemistry, Genetics, Bioengineering")
		print("  - Average Salary: $65,000 - $125,000+")
		print("  - Job Growth: Growing field with emerging opportunities")
	elif selection == 5:
		print("Here are more details about Communications and Journalism:")
		print("  - Career Paths: Journalist, Public Relations, Marketing Specialist, Content Creator")
		print("  - Key Skills: Writing, Critical thinking, Creativity, Interviewing, Social media")
		print("  - Typical Courses: News Writing, Media Ethics, Digital Media, Public Relations")
		print("  - Average Salary: $45,000 - $100,000+")
		print("  - Job Growth: Evolving field with digital media opportunities")

def main():
	menuSelection()
main()

