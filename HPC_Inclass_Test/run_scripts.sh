#!/bin/bash

# Running number_generator.py
python3 number_generator.py

# Running manual_search.py
python3 manual_read.py

# Running mpi_search.py using mpiexec command
mpirun -n 4 python3 mpi_search.py