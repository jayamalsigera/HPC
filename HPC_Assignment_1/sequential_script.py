import random
import sys
from tabulate import tabulate

def generate_random_grades():
    #Generate random grades between 0 and 100.
    return random.randint(0, 100)

def calculate_average(grades):
    #Calculate the average grade from a list of grades
    total = sum(grades)
    return total / len(grades)

def main(students):

    subjects = ['Mathematics', 'English', 'Data Structures and Algorithms', 'High Performance Computing']

    # Generate random grades for each student in different subjects
    student_grades = {i+1: {subject: generate_random_grades() for subject in subjects} for i in range(students)}

    # Initialize dictionary to store grades for each subject
    subject_grades = {subject: [] for subject in subjects}

    # Create table data for printing
    table_data = []

    # Iterate over student grades
    for student, grades in student_grades.items():
        row = [student]
        row.extend(grades.values())
        table_data.append(row)

        # Collect grades for each subject
        for subject, grade in grades.items():
            subject_grades[subject].append(grade)

    headers = ["Student"]
    headers.extend(subjects)

    # Print the table of student grades
    print(tabulate(table_data, headers=headers, tablefmt='pretty'))

    # Calculate and print the average for each subject
    averages_row = ["Average"]
    for subject in subjects:
        subject_avg = calculate_average(subject_grades[subject])
        averages_row.append(subject_avg)

    print(tabulate([averages_row], headers=headers, tablefmt='pretty'))

if __name__ == "__main__":
    students = 50  # Update the number of students to 50
    main(students)
