#!/bin/bash

echo "Running sequential program..."
start=$(date +%s.%N)
python3 sequential_script.py > /dev/null 2>&1
end=$(date +%s.%N)
runtime_seq=$(python3 -c "print(${end} - ${start})")
echo "Execution time for sequential program: $runtime_seq seconds"

echo "Running parallel program..."
start=$(date +%s.%N)
mpirun -np 4 python3 mpi_script.py > /dev/null 2>&1
end=$(date +%s.%N)
runtime_par=$(python3 -c "print(${end} - ${start})")
echo "Execution time for parallel program: $runtime_par seconds"

echo "The parallel program was $(python3 -c "print(${runtime_seq}/${runtime_par})") times faster than the sequential program."
