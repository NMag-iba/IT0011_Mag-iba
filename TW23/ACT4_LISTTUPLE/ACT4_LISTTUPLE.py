students = []  

while True:
    print("----------------------------------")
    print("               Home               ")
    print("----------------------------------")
    print("1. Open File")
    print("2. Save File")
    print("3. Save as File")
    print("4. Show All Students Record")
    print("5. Show Student Record")
    print("6. Add Record")
    print("7. Edit Record")
    print("8. Delete Record")
    print("0. Exit")
    print("----------------------------------")
    choice = input("Choose from 0-8: ")
    print("----------------------------------")

    if choice == "1": 
        existing_file = "studentRecord.txt"  
        print(f"Existing file: {existing_file}")
        print("----------------------------------")
        
        filename = input("Enter file name: ")  

        try:
            with open(filename, "r") as file:
                students = []
                
                for line in file:
                    line = line.strip()
                    if not line:
                        continue  

                    parts = line.split(",")

                    if len(parts) == 5:
                        student = (
                            int(parts[0]),  
                            (parts[1], parts[2]),
                            int(parts[3]), 
                            int(parts[4])  
                        )
                        students.append(student)
                    else:
                        print(f"Skipping invalid line: {line}")
            print("File successfully opened!")
        
        except FileNotFoundError:
            print(f"File '{filename}' does not exist.")
            create_new = input("Would you like to create a new file? (yes/no): ").strip().lower()
            
            if create_new == "yes":
                with open(filename, "w") as file:
                    print(f"New file '{filename}' created successfully.")
            else:
                print("Returning to main menu...")
    
    elif choice == "2":
        with open("studentRecord.txt", "w") as file:
            for student in students:
                file.write(f"{student[0]},{student[1][0]},{student[1][1]},{student[2]},{student[3]}\n")
        print("File saved successfully!")
    elif choice == "3":
        filename = input("Enter new file name: ")
        with open(filename, "w") as file:
            for student in students:
                file.write(f"{student[0]},{student[1][0]},{student[1][1]},{student[2]},{student[3]}\n")
        print("File saved successfully!")
    elif choice == "4":
        if not students:
            print("Please open a file.")
            continue
        print("4.2 Order by last name")
        print("4.3 Order by grade")
        print("----------------------------------")
        sub_choice = input("Choose order: ")
        print("----------------------------------")
        if sub_choice == "4.2":
            sorted_students = sorted(students, key=lambda x: x[1][1])
            for student in sorted_students:
                print("Student ID:", student[0])
                print("Student Name:", student[1][0], student[1][1])
                print("Student Class Standing:", student[2])
                print("Major Exam Grade:", student[3])
                print("----------------------------------")
        elif sub_choice == "4.3":
            sorted_students = sorted(students, key=lambda x: (0.6 * x[2] + 0.4 * x[3]), reverse=True)
            for student in sorted_students:
                final_grade = 0.6 * student[2] + 0.4 * student[3]
                print("Student ID:", student[0])
                print("Student Name:", student[1][0], student[1][1])
                print("Student Class Standing:", student[2])
                print("Major Exam Grade:", student[3])
                print("Final Grade:", f"{final_grade:.2f}")
                print("----------------------------------")
        else:
            print("Invalid choice for option 4.")
    elif choice == "5":
        if not students:
            print("Please open a file.")
            continue
        student_id = input("Enter Student ID to search: ")
        found = False
        for student in students:
            if str(student[0]) == student_id:
                print("Student Record Found:")
                print("Student ID:", student[0])
                print("Student Name:", student[1][0], student[1][1])
                print("Student Class Standing:", student[2])
                print("Major Exam Grade:", student[3])
                found = True
                break
        if not found:
            print("Student ID not found.")
    elif choice == "6":
        print("Adding record...")
        student_id = int(input("Enter Student ID (6-digit number): "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = int(input("Enter Class Standing Grade: "))
        major_exam = int(input("Enter Major Exam Grade: "))
        students.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully!")
    elif choice == "7":
        print("Editing record...")
        student_id = input("Enter Student ID to edit: ")
        for i, student in enumerate(students):
            if str(student[0]) == student_id:
                print("Editing Student Record:")
                first_name = input(f"Enter First Name ({student[1][0]}): ") or student[1][0]
                last_name = input(f"Enter Last Name ({student[1][1]}): ") or student[1][1]
                class_standing = input(f"Enter Class Standing Grade ({student[2]}): ")
                major_exam = input(f"Enter Major Exam Grade ({student[3]}): ")
                students[i] = (
                    student[0],
                    (first_name, last_name),
                    int(class_standing) if class_standing else student[2],
                    int(major_exam) if major_exam else student[3]
                )
                print("Record updated successfully!")
                break
        else:
            print("Student ID not found.")
    elif choice == "8":
        print("Deleting record...")
        student_id = input("Enter Student ID to delete: ")
        for i, student in enumerate(students):
            if str(student[0]) == student_id:
                del students[i]
                print("Record deleted successfully!")
                break
        else:
            print("Student ID not found.")
    elif choice == "0":
        print("Exiting program...")
        break 
    else:
        print("Invalid choice. Please select a number from 0-8.")