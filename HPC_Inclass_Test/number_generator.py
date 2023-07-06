import random
import csv


def rand_number_generator(MIN, MAX):
    """
    Generate random numbers within the given range and write them to a CSV file.

    Args:
        MIN (int): Minimum value of the random numbers.
        MAX (int): Maximum value of the random numbers.
    """
    filename = "output.csv"

    with open(filename, "w", newline="") as outfile:
        writer = csv.writer(outfile)

        for i in range(1000000):
            row = [random.randint(MIN, MAX) for _ in range(20)]
            writer.writerow(row)


if __name__ == "__main__":
    rand_number_generator(0, 100)

    # if content:
    #     printIntegerData(content)
