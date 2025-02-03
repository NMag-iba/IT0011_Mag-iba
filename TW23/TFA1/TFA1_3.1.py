fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

s_fname = fname[0:4]
greetings = "Greeting Message: Hello, {}! Welcome. You are {} years old."

print("\nFull name:  ", fname + " " + lname)
print("Sliced name: ", s_fname)
print(greetings.format(s_fname, age))