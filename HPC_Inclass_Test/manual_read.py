def extract_records(filename, indices):
    """
    Extract records from a file based on given indices.

    Args:
        filename (str): Name of the file to extract records from.
        indices (list): List of indices to extract records from the file.

    Returns:
        list: Extracted records as a list of lists.
    """
    records = []
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i in indices:
                records.append(line.strip().split())
    return records

def generate_search_queries(records, output_file):
    """
    Generate search queries from records and write them to a file.

    Args:
        records (list): List of records.
        output_file (str): Name of the file to write the search queries to.
    """
    with open(output_file, 'w') as file:
        for record in records:
            line = '\t'.join(record)
            file.write(line + '\n')

input_file = 'output.csv'
indices_to_extract = [0, 10, 20, 50, 100000, 500000]

# Extract records based on given indices
extracted_records = extract_records(input_file, indices_to_extract)

output_file = 'search_queries.txt'

# Generate search queries and write them to a file
generate_search_queries(extracted_records, output_file)
