import pandas as pd
import matplotlib.pyplot as plt

# Read the runtime data from a CSV file
df = pd.read_csv('runtime_data.csv')

# Create a figure and set the size
plt.figure(figsize=(10, 6))

# Plot the runtime for single core and MPI on the same graph
plt.plot(df['num_students'], df['single_core_time'], label='Single Core')
plt.plot(df['num_students'], df['mpi_time'], label='MPI')

# Set the x-axis label and y-axis label
plt.xlabel('Number of students')
plt.ylabel('Runtime (ms)')

# Add a legend to the graph
plt.legend()

# Set the title of the graph
plt.title('Runtime vs. Number of Students')

# Enable grid lines
plt.grid(True)

# Display the graph
plt.show()

