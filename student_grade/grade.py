#Initialising dictionary
student_grades={}

#Adding Elements
def add_student(name,grade):
    student_grades[name]=grade
    print(f'Added {name} with grade {grade}')


#update A student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f'{name} grade has been updated to {grade}')

    else:
        print(f'{name} is not found !')

#Delete Student:

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been deleted successfully")

def display():
    if student_grades:
        for name , grade in student_grades.items():
            print(f"{name}: {grade}")

    else:
        print("No students found/added")

def main():
    while True:
        print('\n Student Grades Management')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = int(input("Enter Your Choice:"))
        if choice==1:
            name=input("Enter Student name: ")
            grade=int(input("Enter Student Grade: "))
            add_student(name,grade)

        elif choice==2:
            name=input("Enter Student name: ")
            grade=int(input("Enter Student Grade: "))
            update_student(name, grade)

        elif choice==3:
            name=input("Enter Student name: ")
            delete_student(name)

        elif choice==4:
            print("Displaying all students:")
            display()
        elif choice==5:
            print("Closing the program....")
            break
        else:
            print("Please enter a valid choice (1-5)")

if __name__ == "__main__":
    main()
        
        
            

