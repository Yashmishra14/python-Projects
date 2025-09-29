'''
Add student/teacher/course

Display all students/teachers/courses

Assign students to courses

Search student/teacher by ID

Update student/teacher info

Delete student/teacher

Save all data into JSON file

'''
import json

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"[Student] ID:{self.student_id}, Name:{self.name}, Age:{self.age}, Grade:{self.grade}"


class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"[Teacher] ID:{self.teacher_id}, Name:{self.name}, Subject:{self.subject}"


class Course:
    def __init__(self, course_id, name, teacher_id=None):
        self.course_id = course_id
        self.name = name
        self.teacher_id = teacher_id
        self.students = []

    def __str__(self):
        return f"[Course] ID:{self.course_id}, Name:{self.name}, Teacher:{self.teacher_id}, Students:{self.students}"


class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []
        self.load_data()

    # ==================== Student Methods ====================
    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added successfully!")
        self.save_data()

    def display_students(self):
        if not self.students:
            print("No Students Found!")
        else:
            for s in self.students:
                print(s)

    def search_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            print(f"Student '{student.name}' deleted successfully!")
            self.save_data()
        else:
            print("Student not found!")

    # ==================== Teacher Methods ====================
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Teacher '{teacher.name}' added successfully!")
        self.save_data()

    def display_teachers(self):
        if not self.teachers:
            print("No Teachers Found!")
        else:
            for t in self.teachers:
                print(t)

    def search_teacher(self, teacher_id):
        for t in self.teachers:
            if t.teacher_id == teacher_id:
                return t
        return None

    # ==================== Course Methods ====================
    def add_course(self, course):
        self.courses.append(course)
        print(f"Course '{course.name}' added successfully!")
        self.save_data()

    def display_courses(self):
        if not self.courses:
            print("No Courses Found!")
        else:
            for c in self.courses:
                print(c)

    def assign_student_to_course(self, student_id, course_id):
        student = self.search_student(student_id)
        if not student:
            print("Student not found!")
            return
        for c in self.courses:
            if c.course_id == course_id:
                if student_id not in c.students:
                    c.students.append(student_id)
                    print(f"Student '{student.name}' assigned to course '{c.name}'!")
                    self.save_data()
                    return
        print("Course not found!")

    # ==================== File Handling ====================
    def save_data(self):
        data = {
            "students": [vars(s) for s in self.students],
            "teachers": [vars(t) for t in self.teachers],
            "courses": [vars(c) for c in self.courses]
        }
        with open("school.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open("school.json", "r") as f:
                data = json.load(f)
                self.students = [Student(**s) for s in data.get("students", [])]
                self.teachers = [Teacher(**t) for t in data.get("teachers", [])]
                self.courses = [Course(**c) for c in data.get("courses", [])]
        except FileNotFoundError:
            self.students, self.teachers, self.courses = [], [], []


# ==================== MAIN PROGRAM ====================
def main():
    school = School()

    while True:
        print("\n========= SCHOOL MANAGEMENT MENU =========")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Add Teacher")
        print("4. Display Teachers")
        print("5. Add Course")
        print("6. Display Courses")
        print("7. Assign Student to Course")
        print("8. Delete Student")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            school.add_student(Student(sid, name, age, grade))

        elif choice == "2":
            school.display_students()

        elif choice == "3":
            tid = input("Enter Teacher ID: ")
            name = input("Enter Teacher Name: ")
            subject = input("Enter Subject: ")
            school.add_teacher(Teacher(tid, name, subject))

        elif choice == "4":
            school.display_teachers()

        elif choice == "5":
            cid = input("Enter Course ID: ")
            name = input("Enter Course Name: ")
            school.add_course(Course(cid, name))

        elif choice == "6":
            school.display_courses()

        elif choice == "7":
            sid = input("Enter Student ID: ")
            cid = input("Enter Course ID: ")
            school.assign_student_to_course(sid, cid)

        elif choice == "8":
            sid = input("Enter Student ID to delete: ")
            school.delete_student(sid)

        elif choice == "9":
            print("Exiting School Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
