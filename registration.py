from student import add_course, drop_course, list_courses, calculate_class_and_student_gpa
from billing import calculate_hours_and_bill, display_hours_and_bill

# Student data
student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
student_in_state = {'1001': True, '1002': False, '1003': True, '1004': False}
course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
course_roster = {'CSC101': ['1004', '1003'], 'CSC102': ['1001'], 'CSC103': ['1002'], 'CSC104': []}
course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}
student_gpa = [('1001', 3.5), ('1002', 2.2), ('1003', 4.0), ('1004', 3.9)]
import hashlib

def encrypt_pin(pin):
    hash_object = hashlib.sha256(pin.encode('utf-8'))
    return hash_object.hexdigest()

def login(id, s_list):
    for student in s_list:
        if student[0] == id:
            correct_pin = student[1]
            break
    else:
        print("Incorrect ID.")
        return False

    encrypted_pin = encrypt_pin(input("Enter your PIN: "))
    if encrypted_pin == correct_pin:
        print("Verification successful!")
        return True
    else:
        print("Incorrect PIN.")
        return False
student_list = [('1001', encrypt_pin('111')), ('1002', encrypt_pin('222')), ('1003', encrypt_pin('333')), ('1004', encrypt_pin('444'))]

  
def main():
    """Manage course registration system."""
    s_list = dict(student_list)
    while True:
        id = input("Enter ID to log in, or 0 to quit: ")
        if id == '0':
            break
        if login(id, student_list):
            registered_courses = []
            waitlist = []
            while True:
                print("\n    Select Option: \n" + " -------- ".center(20) +
                    f"\n|{'1: Add Course':^20s}|\n" + " -------- ".center(20) +
                    f"\n|{'2: Drop Course':^20s}|\n" + " -------- ".center(20) +
                    f"\n|{'3: List Courses':^20s}|\n" + " -------- ".center(20) +
                    f"\n|{'4: Show Bill':^20s}|\n" + " -------- ".center(20) +
                    f"\n|{'5: Show GPA:':^20s}|\n" + " -------- ".center(20) +
                    f"\n|{'0 to exit:':^20s}|\n" + " -------- ".center(20))

                choice = input()
                if choice == '0':
                    break
                elif choice == '1':
                    course = input("Enter course you want to add: ")
                    if course not in course_hours:
                        print("Course not found")
                    elif id in course_roster[course]:
                        print("You are already enrolled in that course.")
                    elif len(course_roster[course]) < course_max_size[course]:
                        add_course(id, course_roster, course_max_size, registered_courses, course, waitlist)
                        print("Course added.")
                    else:
                        print("Course already full.")
                        waitlist.append(id)
                        print(f"Added {id} to waitlist for {course}.")
                elif choice == '2':
                    course = input("Enter course you want to drop: ")
                    # Check if the currents student is registered to the course they want to drop
                    if course not in course_hours:
                        print("Course not found")
                    elif id not in course_roster[course]:
                        print("You are not enrolled in that course.")
                    else:
                        drop_course(id, course_roster, registered_courses, waitlist, course, course_max_size)
                        print("Course dropped.")
                        # Check if there are students on the waitlist for this course
                        if waitlist:
                            next_student = waitlist.pop(0)
                            add_course(next_student, course_roster, course_max_size, registered_courses, course)
                            print(f"{next_student} has been enrolled in {course} from the waitlist.")
                elif choice == '3':
                    list_courses(id, course_roster)
                elif choice == '4':
                    credit_hours, cost = calculate_hours_and_bill(id, student_in_state, course_roster, course_hours)
                    display_hours_and_bill(credit_hours, cost)
                elif choice == '5':
                    calculate_class_and_student_gpa(course_roster, student_gpa, id)

if __name__ == '__main__':
    main()
