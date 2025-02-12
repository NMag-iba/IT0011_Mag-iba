try :
    file = open("students.txt", "r")
    contents = file.read()
    file.close()
    
    print("\nReading Student Information: ")
    print(contents)
        
except FileNotFoundError:
    print("Error in finding 'students.txt' file")