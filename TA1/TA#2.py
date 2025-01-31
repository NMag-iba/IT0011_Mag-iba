text = input("Enter number to count sum: ")
sum = 0

for char in text:
    if char.isdigit():  
        sum += int(char)  
print("Sum of digits:", sum)
