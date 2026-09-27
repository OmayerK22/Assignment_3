
class Student:
    def __init__(self, name, student_id, email, age, department, courses):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department
        self.__courses = courses

    # Encapsulation
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    # Method Overloading using default argument
    def display_info(self, show_email=True):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Age:", self.age)
        print("Department:", self.department)

        if show_email:
            print("Email:", self.__email)

        print("Courses:")
        for course in self.__courses:
            print("  ", course["name"], "-", course["marks"])

    def calculate_result(self):
        total_marks = 0

        for course in self.__courses:
            total_marks += course["marks"]

        average = total_marks / len(self.__courses)

        if average >= 80:
            grade = "A+"
        elif average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        print("Total Marks:", total_marks)
        print("Average Marks:", round(average, 2))
        print("Grade:", grade)

        return grade

    def get_student_type(self):
        return "Student"


class UndergraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        courses,
        semester
    ):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department,
            courses
        )

        self.semester = semester

    # Method Overriding
    def get_student_type(self):
        return "Undergraduate Student"

    # Method Overriding
    def display_info(self, show_email=True):
        super().display_info(show_email)
        print("Student Type:", self.get_student_type())
        print("Semester:", self.semester)


class GraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        courses,
        research_topic
    ):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department,
            courses
        )

        self.research_topic = research_topic

    # Method Overriding
    def get_student_type(self):
        return "Graduate Student"

    # Method Overriding
    def display_info(self, show_email=True):
        super().display_info(show_email)
        print("Student Type:", self.get_student_type())
        print("Research Topic:", self.research_topic)


# ==================================================
# Main Program
# ==================================================

students = []

print("==============================================")
print("       STUDENT MANAGEMENT SYSTEM")
print("==============================================")


while True:

    print("\nChoose Student Type")
    print("1. Undergraduate Student")
    print("2. Graduate Student")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "3":
        break

    if choice not in ["1", "2"]:
        print("\nInvalid choice. Please try again.")
        continue


    # ----------------------------------------------
    # Student Information
    # ----------------------------------------------

    print("\nEnter Student Information")

    name = input("Enter name: ")
    student_id = input("Enter student ID: ")
    email = input("Enter email: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")


    # ----------------------------------------------
    # Course Information
    # ----------------------------------------------

    courses = []

    number_of_courses = int(
        input("\nEnter number of courses: ")
    )

    for i in range(number_of_courses):

        print(f"\nCourse {i + 1}")

        course_name = input("Enter course name: ")
        marks = float(input("Enter marks: "))

        while marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            marks = float(input("Enter marks: "))

        courses.append({
            "name": course_name,
            "marks": marks
        })




    # ----------------------------------------------
    # Create Student Object
    # ----------------------------------------------

    if choice == "1":

        semester = input("\nEnter semester: ")

        student = UndergraduateStudent(
            name,
            student_id,
            email,
            age,
            department,
            courses,
            semester
        )

    else:

        research_topic = input(
            "\nEnter research topic: "
        )

        student = GraduateStudent(
            name,
            student_id,
            email,
            age,
            department,
            courses,
            research_topic
        )


    students.append(student)

    print("\nStudent added successfully!")

    another = input(
        "\nDo you want to add another student? (yes/no): "
    )

    if another.lower() != "yes":
        break


# ==================================================
# Display Student Information
# ==================================================

print("\n\n==============================================")
print("             STUDENT INFORMATION")
print("==============================================")


for student in students:

    student.display_info()

    print("\nResult:")
    student.calculate_result()

    print()


print("==============================================")
print("       PROGRAM ENDED SUCCESSFULLY")
print("==============================================")

