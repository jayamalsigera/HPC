import subprocess

def run_script(script_name):
    """
    Run a Python script using the subprocess module.

    Args:
        script_name (str): Name of the script to run.

    Notes:
        - Executes the script using the 'python3' command.
        - Captures the stdout and stderr outputs.
        - Prints the output and error messages if the script returns a non-zero exit code.
        - Prints a success message if the script executes successfully.
    """
    process = subprocess.run(['python3', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if process.returncode != 0:
        print(f'Error occurred while executing {script_name}')
        print('Output:', process.stdout.decode())
        print('Error:', process.stderr.decode())
    else:
        print(f'Successfully executed {script_name}')

if __name__ == "__main__":
    scripts = ['number_generator.py', 'manual_read.py', 'mpi_search.py']

    # Run each script and handle the execution result
    for script in scripts:
        run_script(script)
