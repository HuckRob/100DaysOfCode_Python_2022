# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_heights_added = 0
for student in student_heights:  #this can be done with sum()
    total_heights_added = total_heights_added + student
average_student_height_rounded = round(total_heights_added/len(student_heights))

print(average_student_height_rounded)
