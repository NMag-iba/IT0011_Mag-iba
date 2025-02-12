try:
    with open("numbers.txt", 'r') as file:
        line_num = 1
        for line in file:
            numbers = line.strip().split(',')
            if all(num.strip().isdigit() for num in numbers):
                numbers = [int(num) for num in numbers]
                total_sum = sum(numbers)
                if str(total_sum) == str(total_sum)[::-1]:
                    status = "Palindrome"
                else:
                    status = "Not a palindrome"
                print(f"Line {line_num}: {line.strip()} (sum {total_sum}) - {status}")
            line_num += 1
except FileNotFoundError:
    print("Error: The file 'numbers.txt' was not found.")