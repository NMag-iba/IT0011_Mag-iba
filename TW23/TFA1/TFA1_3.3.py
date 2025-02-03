lname = input("Enter last name: ")
fname = input("Enter first name: ")
age = input("Enter Age: ")
c_number = input("Contact Number: ")
course = input("Course: ")

student_info = "Last Name: " + lname + "\nFirst Name: " + fname + "\nAge: " + age + "\nContact Number: " + c_number + "\nCourse: " + course

file = open("students.txt", "a")
file.write(student_info)
file.close()
print("Student information has been saved to 'students.txt'")