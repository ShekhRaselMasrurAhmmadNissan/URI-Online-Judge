# Reading the Grades of Students...
first_student = float(input())
second_student = float(input())
third_student = float(input())

# Rounding The Grades...
round(first_student, 1)
round(second_student, 1)
round(third_student, 1)

# Calculating Median...
MEDIA = ((first_student * 2) + (second_student * 3) +
         (third_student * 5)) / (2 + 3 + 5)

# Printing the result...
print('MEDIA = %0.1f' % MEDIA)
