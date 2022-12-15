
# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Enter the lengths of three side of a triangle:")
try:
	list = [int(input("a: ")), int(input("b: ")), int(input("c: "))]
	if len(set(list)) == 1:
		type = 'equalateral'
	elif len(set(list)) == 3:
		type = 'scalene'
	else:
		type = 'isosceles'
	print(f'A triangle with sides of {list[0]}, {list[1]} & {list[2]} is a {type} triangle')
except:
	print("Error")
