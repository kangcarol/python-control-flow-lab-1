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

length_a = input('Enter the lengths of three side of a triangle, starting with side a:')
length_b = input('Enter the lengths of three side of a triangle, side b:')
length_c = input('Enter the lengths of three side of a triangle, side c:')

if length_a == length_b and length_a ==length_c:
  print(f'A triangle with sides of {length_a}, {length_b} & {length_c} is an equalateral triangle')
elif length_a != length_b and length_b !=length_c and length_a !=length_c:
  print(f'A triangle with sides of {length_a}, {length_b} & {length_c} is scalene triangle')
else:
  print(f'A triangle with sides of {length_a}, {length_b} & {length_c} is an isosceles triangle')
