def calculate_billing_info(id, s_in_state, c_rosters, c_hours):
    hours = 0
    cost = 0
    for course in c_rosters:
        if id in c_rosters[course]:
            hours += c_hours.get(course, 0)
            if s_in_state:
                cost += c_hours[course] * 225
            else:
                cost += c_hours[course] * 850
        return hours, cost

def display_hours_and_bill(hours, cost):
