import datetime 

pos_answer = ['yes','y']
neg_answer = ['no','n']

user_projects = {}

def project_entry():
# User inputs number of hours needed to complete project
	name = raw_input("What is the name of the project you're working on? ")

# User inputs number of hours needed to complete project
	time = input("Enter the number of hours your project will take: ")#should add %r % name here
	time *= 60
	user_projects[name] = time

# Prompt user to enter data on additional projects
ans = raw_input("Are you currently working on any projects?: ")
while ans.lower() not in neg_answer:
	project_entry()
	ans = raw_input("Do you have any more projects to work on?: ")

# User inputs average number of minutes they can spend on their projects
avgTotalDailyTime = input("Enter the the number of minutes you have to spend on your projects \
or projects per day: ")

# Create an ordered list of tupples from the user_projects dictionary
new_user_projects = sorted(user_projects.items(), key=lambda t: t[1])
for i in range(len(new_user_projects)):
	timePerProject = avgTotalDailyTime/len(new_user_projects[i:])
	# Calculate number of days required to complete the smallest project
	smallestProjectTime = new_user_projects[i:][0][1]
	smallestProject = new_user_projects[i:][0][0]
	i+1
	if smallestProjectTime % timePerProject == 0:
		daysNeeded = smallestProjectTime/timePerProject
	daysNeeded = smallestProjectTime/timePerProject + 1
	completionDate = (datetime.date.today() + datetime.timedelta(daysNeeded)).isoformat()
	# Tell user the date they will finish their project 
	print "If you work on your %s project everyday for %r minutes you will complete your project in\
	%r days on %r" % (smallestProject, timePerProject, daysNeeded, completionDate)
	
