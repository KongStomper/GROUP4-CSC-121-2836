#
#
#

def list_courses(id, c_roster):
    if id in c_roster:
        courses = c_roster[id]
        print(f"Student {id} is registered for the following courses:")
        for course in courses:
            print(course)
    else:
        print(f"Student {id} is not registered for any courses.")
