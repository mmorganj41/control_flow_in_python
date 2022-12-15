# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

months = {
	'Jan': [1, 31],
	'Feb': [2, 29],
	'Mar': [3, 31],
	'Apr': [4, 30],
	'May': [5, 31],
	'Jun': [6, 30],
	'Jul': [7, 31],
	'Aug': [8, 31],
	'Sep': [9, 30],
	'Oct': [10, 31],
	'Nov': [11, 30],
	'Dec': [12, 31],
}

try:
	month = input('Enter the month of the year (Jan - Dec): ').capitalize()
	day = int(input('Enter the day of the month: '))
	if months[month][1] < day or day < 1:
		print('No such day')
	else:
		month_date = months[month][0]*100 + day
		if month_date < 320 or month_date > 1220:
			season = 'Winter'
		elif month_date < 521:
			season = 'Spring'
		elif month_date < 922:
			season = 'Summer'
		else:
			season = 'Fall'
		print(f'{month} {day} is in {season}')
except:
	print('Error')