def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate_percentage(part, total):
    """
    Calculates the percentage of part out of total.
    Returns a value between 0 and 100.
    """
    if total == 0:
        return 0
    
    # Needs to be multiplied by 100
    return (part / total) * 100