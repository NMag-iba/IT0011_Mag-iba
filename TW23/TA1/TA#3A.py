num_rows = 5 

for i in range(1, num_rows + 1):  
    print(" " * (num_rows - i), end="")  
    for j in range(1, i + 1):  
        print(j, end="") 
    print() 