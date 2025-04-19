import math

def solve_trigonometry(operation, value, in_degrees=True):
    if in_degrees:
        value = math.radians(value)  # Convert degrees to radians

    if operation == "sin":
        return math.sin(value)
    elif operation == "cos":
        return math.cos(value)
    elif operation == "tan":
        return math.tan(value)
    elif operation == "arcsin":
        result = math.asin(value)
        return math.degrees(result) if in_degrees else result
    elif operation == "arccos":
        result = math.acos(value)
        return math.degrees(result) if in_degrees else result
    elif operation == "arctan":
        result = math.atan(value)
        return math.degrees(result) if in_degrees else result
    else:
        return "Invalid operation"

print("Sine of 30 degrees:", solve_trigonometry("sin", 30))
print("Cosine of 60 degrees:", solve_trigonometry("cos", 60))
print("Tangent of 45 degrees:", solve_trigonometry("tan", 45))
print("Arcsine of 0.5 (degrees):", solve_trigonometry("arcsin", 0.5, in_degrees=True))
