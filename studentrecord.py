student = {}
while True:
    print("\n=== Student Management System ===")
    
    ...
    choice = input("1 to 8 : ")


    # Add student section
    if choice == "1":
        name = input("Enter student name: ")

        if name in student:
            print("Student already exists")
        else:
            marks = float(input("Enter marks: "))
            student[name] = marks
            print("Student recorded successfully")

    # View student
    elif choice == "2":
        if len(student) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for name, marks in student.items():
                print(f"{name} : {marks}")

    # search student
    elif choice =="3":
        name= input("enter name to search : ")
        if name in student:
            print(f"{name} scored {student[name]}")
        else:
            print("Student not found.")

            # update marks
    elif choice =="4":
        name= input("enter name of student : ")
        if name in student:
            new_marks = float(input("enter new marks: "))
            student[name] = new_marks
            print("marks updated")
        else:
            print("studnt not found")
    # delete section
    elif choice == "5":
     name= input("enter name to delete : ")
     if name in student:
         del student[name]
         print("Student deleted sucessfully ")
     else:
         print("student not found")

    # Average Marks
    elif choice == "6":
        if len(student)==0:
            print("no student available")
        else:
            average=sum(student.values())/len(student)
            print(f"Average marks : {average:.2f}")
    # find topper
    elif choice =="7":
         if len(student)==0:
            print("no student available")
         else:
            topper=max(student,key=student.get)
            print("name:", topper)
            print(f" marks : {student[topper]}")
        # exit
    elif choice =="8":
        print("thanks for exiting") 
        break
    else:
        print("invalid choice ")   