#!/bin/bash

echo "num_students,single_core_time,mpi_time" > runtime_data.csv

for num_students in $(seq 50 50 1000000); do
  echo -n "$num_students," >> runtime_data.csv

  start_time=$(date +%s%N)
  python3 sequential_script_var.py $num_students > /dev/null
  end_time=$(date +%s%N)
  single_core_time=$(echo "scale=3; ($end_time - $start_time) / 1000000" | bc)
  echo -n "$single_core_time," >> runtime_data.csv

  start_time=$(date +%s%N)
  mpirun -n 4 python3 mpi_script_var.py $num_students > /dev/null
  end_time=$(date +%s%N)
  mpi_time=$(echo "scale=3; ($end_time - $start_time) / 1000000" | bc)
  echo "$mpi_time" >> runtime_data.csv
done

python3 plot_runtime.py