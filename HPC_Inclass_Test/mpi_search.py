import csv
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data_file= 'output.csv'
query_file= 'search_queries.txt'


# Read the rows from the search query file
rows_to_search = []
with open(query_file, 'r') as query_file:
    for line in query_file:
        row_values = line.strip().split(',')
        rows_to_search.append(row_values)

# Calculate the number of records per process
total_records = 1000000
records_per_process = total_records // size

# Calculate the start and end indices for the current process
start_index = rank * records_per_process
if (start_index != 0):
    start_index = start_index+1

end_index = ((rank + 1) * records_per_process)-1

# Open the CSV file
with open(data_file, 'r') as csv_file:
    # Create a CSV reader object
    reader = csv.reader(csv_file)

    # Skip the rows before the start index
    for _ in range(start_index):
        next(reader)

    # Iterate over the rows and check if any row matches the search query
    for i, row in enumerate(reader):
        for query_row in rows_to_search:
            if row == query_row:
                print(f"Process {rank} found row: {row}")

        # Break the loop if we have reached the end index
        if i == end_index - 1:
            break