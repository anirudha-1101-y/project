"""Report module for the Student Marks Tracker."""


def show_report(students):
    """Print each student's marks, average, and overall class average."""
    total_of_averages = 0

    # Loop through the list of student dictionaries.
    for student in students:
        name = student["name"]
        marks = student["marks"]

        # Loop through the marks list to calculate the total.
        total_marks = 0
        for mark in marks:
            total_marks += mark

        average = total_marks / len(marks)
        total_of_averages += average
        print(f"{name}: marks = {marks}, average = {average:.2f}")

    class_average = total_of_averages / len(students)
    print("-" * 30)
    print(f"Class average: {class_average:.2f}")
