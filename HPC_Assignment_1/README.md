# PART 1
# Sequential Program to Calculate Average Marks per Subject

## Prerequisites

Before running the scripts, make sure you have the following requirements:

- Python 3.x

- tabulate library

You can install the required Python libraries by running the following command:

    pip install tabulate

## Usage

1.Navigate to the project directory.

    cd /path/to/directory

2.Run the python script `sequential_script.py`:
    
    python3 sequential_script.py    

# PART 2
# MPI Program to Calculate Average Marks per Subject

## Prerequisites

Before running the scripts, make sure you have the following requirements:

- mpi4py library

You can install the required Python libraries by running the following command:

    pip install mpi4py

## Usage

1.Navigate to the project directory.

    cd /path/to/directory

2.Run the python script `mpi_script.py`:
    
    mpirun -n 4 python3 mpi_script.py

# PART 3
# Runtime Comparison for Single Core and MPI Scripts for 50 Students

## Usage

1.Navigate to the project directory.

    cd /path/to/directory

2.Make the scripts executable (if not already done).

    chmod +x sequential_script.py
    chmod +x mpi_script.py
    chmod +x runtime_comparision.sh

3.Run the bash script `runtime_comparision.sh` to perform the runtime comparison:
    
    ./run_experiments.sh

# PART 4
# Runtime Comparison for Single Core and MPI Scripts with Varying Number of Students

To compare the runtime performance between a single-core script and an MPI script for calculating the average grade of each student for a given number of students, the folowing experiment is conducted by varying the number of students from 50 to 1,000,000 and measuring the runtime for each run.

## Additional Prerequisites

Before running the scripts, make sure you have the following requirements:

- numpy library
- matplotlib library

## Usage

1.Navigate to the project directory.

    cd /path/to/directory

2.Make the scripts executable (if not already done).

    chmod +x sequential_script.py
    chmod +x mpi_script.py
    chmod +x plot_runtime.py
    chmod +x run_experiments.sh

3.Run the bash script `run_experiments.sh` to perform the runtime comparison:

    ./run_experiments.sh


This script will generate a CSV file (`runtime_data.csv`) containing the runtime data for both scripts.

This script will generate a plot showing the runtime of each script as a function of the number of students.


## Customization

- If you want to modify the range or step size of the number of students, you can edit the bash script `run_experiments.sh` and adjust the `seq` command parameters.
