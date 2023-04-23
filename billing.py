def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
 in_state = s_in_state.get(id, False)
    courses = [c for c, s in c_rosters.items() if id in s]
    total_hours = sum(c_hours.get(c, 0) for c in courses)
    if in_state:
        tuition_cost = 100
    else:
        tuition_cost = 200

    total_cost = total_hours * tuition_cost

    return total_hours, total_cost

def display_hours_and_bill(hours, cost):
