num_rows = 5
starting_num = 1
i = 1

while i <= num_rows:
    j = 1
    while j <= (2 * i - 1):  
        print(starting_num, end="")
        j += 1
    print() 
    if i < 3:
        starting_num += 2
    else:
        starting_num += 1
    i += 1 
