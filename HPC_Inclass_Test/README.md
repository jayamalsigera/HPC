# Python MPI Search Program

This project includes a set of Python scripts to generate a large dataset of random numbers, manually search for specific records, and perform parallel searching using MPI.

The project consists of three main scripts:

1. `number_generator.py`: This script generates a large dataset of random numbers and saves it to a CSV file.
2. `manual_search.py`: This script extracts specific records from the dataset and generates a set of search queries.
3. `mpi_search.py`: This script uses MPI to perform parallel searching of the queries in the dataset.

## Prerequisites

Before running the scripts, please ensure you have the following installed:

- Python 3.6 or above
- MPI for Python (mpi4py)
- MPI implementation (like Open MPI or MPICH)

## How to Run

Extract the zip file containing the project scripts to a directory of your choice.

    unzip your_project.zip -d /path/to/directory

Navigate to the directory containing the scripts.

    cd /path/to/directory

Make the scripts executable (if not already done).

    chmod +x number_generator.py
    chmod +x manual_search.py
    chmod +x mpi_search.py
    chmod +x run_scripts.sh

Run the run_scripts.sh bash script. This script runs the three Python scripts in the order they need to be executed.

    ./run_scripts.sh

The scripts will run, and the output can be observed from terminal.