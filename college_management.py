class Student:
    def __init__(self, name, student_id, email):
        self.name = name
        self.student_id = student_id
        self.email = email
        self.courses_enrolled = []

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Email: {self.email}"


class Instructor:
    def __init__(self, name, instructor_id, email):
        self.name = name
        self.instructor_id = instructor_id
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, ID: {self.instructor_id}, Email: {self.email}"


class Course:
    def __init__(self, name, code, instructor):
        self.name = name
        self.code = code
        self.instructor = instructor
        self.enrolled_students = []

    def __str__(self):
        return f"Course: {self.name}, Code: {self.code}, Instructor: {self.instructor.name}"


class College:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student(self, student, course):
        course.enrolled_students.append(student)
        student.courses_enrolled.append(course)

    def assign_instructor(self, course, instructor):
        course.instructor = instructor

    def input_grade(self, student, course, grade):
        # In a real-world scenario, you would implement grading functionality here
        print(f"Grade {grade} recorded for student {student.name} in course {course.name}")


def print_students(college):
    print("\nStudents:")
    for student in college.students:
        print(student)


def print_instructors(college):
    print("\nInstructors:")
    for instructor in college.instructors:
        print(instructor)


def print_courses(college):
    print("\nCourses:")
    for course in college.courses:
        print(course)


def enroll_student_to_course(college):
    print_students(college)
    student_id = int(input("Enter student ID: "))
    print_courses(college)
    course_code = input("Enter course code: ")

    student = next((s for s in college.students if s.student_id == student_id), None)
    course = next((c for c in college.courses if c.code == course_code), None)

    if student and course:
        college.enroll_student(student, course)
        print(f"{student.name} enrolled in {course.name}")
    else:
        print("Student or course not found.")


def assign_instructor_to_course(college):
    print_instructors(college)
    instructor_id = int(input("Enter instructor ID: "))
    print_courses(college)
    course_code = input("Enter course code: ")

    instructor = next((i for i in college.instructors if i.instructor_id == instructor_id), None)
    course = next((c for c in college.courses if c.code == course_code), None)

    if instructor and course:
        college.assign_instructor(course, instructor)
        print(f"{instructor.name} assigned to teach {course.name}")
    else:
        print("Instructor or course not found.")


def input_student_grade(college):
    print_students(college)
    student_id = int(input("Enter student ID: "))
    print_courses(college)
    course_code = input("Enter course code: ")
    grade = input("Enter grade: ")

    student = next((s for s in college.students if s.student_id == student_id), None)
    course = next((c for c in college.courses if c.code == course_code), None)

    if student and course:
        college.input_grade(student, course, grade)
    else:
        print("Student or course not found.")


def main():
    college = College()

    student1 = Student("Alice", 1, "alice@example.com")
    college.add_student(student1)

    student2 = Student("Bob", 2, "bob@example.com")
    college.add_student(student2)

    instructor1 = Instructor("Charlie", 101, "charlie@example.com")
    college.add_instructor(instructor1)

    instructor2 = Instructor("David", 102, "david@example.com")
    college.add_instructor(instructor2)

    course1 = Course("Python Programming", "CS101", instructor1)
    college.add_course(course1)

    course2 = Course("Web Development", "CS102", instructor2)
    college.add_course(course2)

    # Sample enrollments
    college.enroll_student(student1, course1)
    college.enroll_student(student2, course2)

    # Sample assignments
    college.assign_instructor(course1, instructor1)
    college.assign_instructor(course2, instructor2)

    # Sample input grade
    college.input_grade(student1, course1, "A")
    college.input_grade(student2, course2, "B")

    while True:
        print("\nOptions:")
        print("1. Enroll Student to Course")
        print("2. Assign Instructor to Course")
        print("3. Input Student Grade")
        print("4. Print Students")
        print("5. Print Instructors")
        print("6. Print Courses")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            enroll_student_to_course(college)
        elif choice == "2":
            assign_instructor_to_course(college)
        elif choice == "3":
            input_student_grade(college)
        elif choice == "4":
            print_students(college)
        elif choice == "5":
            print_instructors(college)
        elif choice == "6":
            print_courses(college)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
