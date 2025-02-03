text = input("Enter number to count sum: ")
total = 0 

for char in text:
    if char >= '0' and char <= '9':
        total = total + int(char) 
print("Sum:", total)