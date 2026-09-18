def grade(marks):
    x = sum(marks) / len(marks)
    if x >= 90:
        return "A+"
    if x >= 80:
        return "A"
    if x >= 70:
        return "B"
    if x >= 60:
        return "C"
    if x >= 50:
        return "D"
    return "Fail"
