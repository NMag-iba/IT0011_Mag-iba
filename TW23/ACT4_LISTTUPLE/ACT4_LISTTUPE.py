import ast  # Safe alternative to eval()

students = []
filename = "studentRecord.txt"  # Default existing file

while True:
    print("----------------------------------")
    print("                Home                ")
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

    choice = input("Choose from 0-8: ").strip()
    print("----------------------------------")

    if choice == "1":
        print(f"Existing File: {filename}")
        print("----------------------------------")

        while True:
            file_input = input("Enter the file name: ").strip()

            try:
                with open(file_input, "r") as file:
                    lines = file.readlines()

                students.clear()  # Clear old data before reloading

                for line in lines:
                    line = line.strip()
                    if line:  # Skip empty lines
                        try:
                            student_data = ast.literal_eval(line)  # Safe alternative to eval()
                            if isinstance(student_data, tuple) and len(student_data) == 4:
                                # Ensure Student ID is always stored as a string
                                student_data = (str(student_data[0]), student_data[1], student_data[2], student_data[3])
                                students.append(student_data)
                            else:
                                print(f"Skipping invalid record: {line}")
                        except (SyntaxError, ValueError):
                            print(f"Skipping invalid line: {line}")

                filename = file_input  # Update filename
                print(f"File '{filename}' successfully opened!")
                break

            except FileNotFoundError:
                print("File not found.")
                create_new = input("Do you want to create a new file? (yes/no): ").strip().lower()
                if create_new == "yes":
                    filename = input("Enter new file name: ").strip()
                    open(filename, "w").close()  # Create the new file
                    print(f"New file '{filename}' created!")
                    break
                else:
                    print("Returning to the main menu.")
                    break

    elif choice == "2":
        if students:
            try:
                with open(filename, "w") as file:
                    for student in students:
                        file.write(str(student) + "\n")
                print(f"File '{filename}' saved successfully.")
            except Exception as e:
                print(f"Error saving file: {e}")
        else:
            print("No records to save. Open a file first.")

    elif choice == "3":
        if students:
            new_filename = input("Enter new file name: ").strip()
            try:
                with open(new_filename, "w") as file:
                    for student in students:
                        file.write(str(student) + "\n")
                filename = new_filename
                print(f"File saved as '{filename}' successfully.")
            except Exception as e:
                print(f"Error saving file: {e}")
        else:
            print("No records to save. Open a file first.")

    elif choice == "4":
        if not students:
            print("No records found. Open a file first.")
        else:
            print("1. Order by last name")
            print("2. Order by grade (60% Class Standing, 40% Major Exam)")
            print("----------------------------------")
            sub_choice = input("Choose output (1-2): ").strip()
            print("----------------------------------")

            if sub_choice == "1":
                students.sort(key=lambda x: x[1][1].lower())  # Sort by last name (case insensitive)
            elif sub_choice == "2":
                students.sort(key=lambda x: (0.6 * x[2]) + (0.4 * x[3]), reverse=True)  # Sort by computed grade
            else:
                print("Invalid choice for option 4.")
                continue  # Return to menu

            for student in students:
                computed_grade = (0.6 * student[2]) + (0.4 * student[3])
                print(f"{student} -> Computed Grade: {computed_grade:.2f}")

    elif choice == "5":
        if not students:
            print("No records found. Open a file first.")
        else:
            student_id = input("Enter Student ID: ").strip()
            found = next((s for s in students if str(s[0]).strip() == student_id.strip()), None)
            if found:
                print(found)
            else:
                print("Student ID not found.")

    elif choice == "6":
        student_id = input("Enter Student ID: ").strip()
        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last Name: ").strip()

        try:
            class_standing = float(input("Enter Class Standing: ").strip())
            major_exam = float(input("Enter Major Exam Grade: ").strip())
            students.append((student_id, (first_name, last_name), class_standing, major_exam))
            print("Record added successfully.")
        except ValueError:
            print("Invalid input. Class Standing and Major Exam must be numbers.")

    elif choice == "7":
        student_id = input("Enter Student ID to edit: ").strip()
        for i, student in enumerate(students):
            if str(student[0]).strip() == student_id.strip():
                first_name = input("Enter new First Name: ").strip()
                last_name = input("Enter new Last Name: ").strip()

                try:
                    class_standing = float(input("Enter new Class Standing: ").strip())
                    major_exam = float(input("Enter new Major Exam Grade: ").strip())
                    students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
                    print("Record updated successfully.")
                except ValueError:
                    print("Invalid input. Class Standing and Major Exam must be numbers.")
                break
        else:
            print("Student ID not found.")

    elif choice == "8":
        student_id = input("Enter Student ID to delete: ").strip()
        for i, student in enumerate(students):
            if str(student[0]).strip() == student_id.strip():
                del students[i]
                print("Record deleted successfully.")
                break
        else:
            print("Student ID not found.")

    elif choice == "0":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please select a number from 0-8.")