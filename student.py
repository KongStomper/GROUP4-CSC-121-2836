def add_course(id, c_roster, c_max_size, registered_courses, course, waitlist):
    if course not in c_roster:
        print("Course not found")
        return
    if id in c_roster[course]:
        print("You are already enrolled in that course.")
        return
    if len(c_roster[course]) >= c_max_size[course]:
        print("Course is full. Adding to waitlist...")
        waitlist.append((id, course))
        print(f"{id} added to waitlist for {course}")
        return
    c_roster[course].append(id)
    registered_courses.append(course)
    print(f"{id} added to {course}")


def drop_course(id, c_roster, registered_courses, waitlist, course, c_max_size):
    if course not in c_roster:
        print("Course not found")
        return
    if id not in c_roster[course]:
        print("You are not enrolled in that course.")
        return
    c_roster[course].remove(id)
    registered_courses.remove(course)
    print(f"{id} dropped from {course}")
    if waitlist:
        next_student, next_course = waitlist.pop(0)
        add_course(next_student, c_roster, c_max_size, registered_courses, next_course, waitlist)
        print(f"{next_student} from waitlist added to {next_course}")

def list_courses(id, c_roster):
    registred_courses = []
    for course, students in c_roster.items():
        for id in students:
            registered_courses.append(course)
        print(f"Student {id} is registered for the following courses:")
        for course in registered_courses
            print(registered_courses)
        print(f"Total number: {len(registered_courses)}")
