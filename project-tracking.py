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

prevWorkDoneMin = 0
prevWorkDoneDay = 0

# Create an ordered list of tupples from the user_projects dictionary
new_user_projects = sorted(user_projects.items(), key=lambda t: t[1])
for i in range(len(new_user_projects)):
	# Calculate time that can be spent per project for all remaining projects
	timePerProject = avgTotalDailyTime/len(new_user_projects[i:])
	# Find the the remaining time left on the smallest project
	smallestProjectTime = new_user_projects[i:][0][1] - prevWorkDoneMin
	smallestProject = new_user_projects[i:][0][0]
	i+=1
	# Calculate the number of days it will take to complete the smallest project remaining project
	if smallestProjectTime % timePerProject == 0:
		daysNeeded = smallestProjectTime/timePerProject
		prevWorkDoneMin += daysNeeded * timePerProject
	else:
		daysNeeded = smallestProjectTime/timePerProject + 1
		if len(new_user_projects[i:]) != 0:
		    prevWorkDoneMin += (daysNeeded * timePerProject) + (timePerProject - smallestProjectTime % timePerProject) / len(new_user_projects[i:])
		else: 
		    prevWorkDoneMin += (daysNeeded * timePerProject) + (timePerProject - smallestProjectTime % timePerProject) / len(new_user_projects)
		  
	# Calculate the completion date of the smallest remaining project
	completionDate = (datetime.date.today() + datetime.timedelta(daysNeeded + prevWorkDoneDay)).isoformat()
	prevWorkDoneDay += daysNeeded 
	# Tell user the date they will finish their project or projects
	print "If you split your %r minutes of time evenly across all your projects you will complete your %s project in\
 %r days on %r" % (avgTotalDailyTime, smallestProject, prevWorkDoneDay, completionDate)
	
