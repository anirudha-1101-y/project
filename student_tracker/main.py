"""Simple Student Marks Tracker project.

Run this file with: python main.py
"""

from school.data import get_students
from school.reports import show_report


def main():
    students = get_students()  # This is a list of dictionaries.

    print("STUDENT MARKS TRACKER")
    print("-" * 30)
    show_report(students)


if __name__ == "__main__":
    main()
