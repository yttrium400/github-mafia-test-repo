def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def is_passing(grade):
    # Logic error: D should be passing but function returns False for 'D'
    if grade == "A" or grade == "B" or grade == "C" or grade == "D":
        return True
    return False