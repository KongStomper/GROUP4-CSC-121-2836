def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    in_state = s_in_state.get(id, False)
    total_hours = 0
    total_cost = 0
    for course, roster in c_rosters.items():
        if id in roster:
            hours = c_hours[course]
            total_hours += hours
            if in_state:
                cost = hours * 225
            else:
                cost = hours * 850
            total_cost += cost
    return total_hours, total_cost


def display_hours_and_bill(hours, cost):
    print(f"Total credit hours: {hours}")
    print(f"Total cost of enrollment: ${cost}")
