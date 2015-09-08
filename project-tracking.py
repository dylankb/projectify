import datetime 

# User inputs number of hours needed to complete project
hoursNeededinMinutes = input("Enter the number of hours your project will take: ")
hoursNeededinMinutes*= 60

# User inputs average number of minutes they can spend on their project in decimal
avgDailyMinutes = input("Enter the the number of minutes you will spend on \
project per day: ")

# Calculate number of days required by divide total time needed over avg num 
# of hours

if hoursNeededinMinutes % avgDailyMinutes == 0:
    daysNeeded = hoursNeededinMinutes/avgDailyMinutes
daysNeeded = hoursNeededinMinutes/avgDailyMinutes + 1

# Tell user the date they will finish their project 
completionDate = (datetime.date.today() + datetime.timedelta(daysNeeded)).isoformat()
print completionDate



# VERSION TO DO

# V0.1 - Script calculates time to complete one project

# V.2 - Script provides time to complete multiple projects
# User inputs each projects completion date
# Prompt user to ask if they have additional projects they
# Calculate completion date for each project if user spent equal 
# time on each task

# V.3 
# Allow the user to designate the number of minutes they will spend on each project



# Other
# Prompt user for how much time they want to spend on their project with some choices.
# have an other choice for custom values
