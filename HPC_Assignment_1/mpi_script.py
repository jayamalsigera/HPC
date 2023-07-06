import random
import sys
from mpi4py import MPI
from tabulate import tabulate

def generate_random_grades():
    #Generate random grades between 0 and 100.
    return random.randint(0, 100)

def calculate_subject_averages(student_grades):
    #Calculate the average grade from a list of grades
    subject_averages = {}
    for subject, grades in student_grades.items():
        subject_avg = sum(grades) / len(grades)
        subject_averages[subject] = subject_avg
    return subject_averages

def main(students):
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    

    subjects = ['Mathematics', 'English', 'Data Structures and Algorithms', 'High Performance Computing']

    # Generate random grades for each subject for the given number of students
    if rank == 0:
        student_grades = {subject: [generate_random_grades() for _ in range(students)] for subject in subjects}
    else:
        student_grades = None

    # Broadcast the student grades to all processors
    student_grades = comm.bcast(student_grades, root=0)

    local_table_data = []
    all_table_data = []

    # Divide the students among processors
    start = rank * (students // size)
    if rank != size - 1:
        end = start + (students // size)
    else:
        end = students

    # Calculate the average for the subjects assigned to the current processor
    for subject in subjects:
        grades = student_grades[subject][start:end]
        subject_avg = sum(grades) / len(grades)
        local_table_data.append([subject, subject_avg])

    # Gather the local data from all processors to the root processor
    all_table_data = comm.gather(local_table_data, root=0)

    if rank == 0:
        # Flatten the gathered data and print the table of subject averages
        all_table_data = [item for sublist in all_table_data for item in sublist]
        headers = ["Subject", "Average"]
        print(tabulate(all_table_data, headers=headers, tablefmt='pretty'))

if __name__ == "__main__":
    students = 50
    main(students)
