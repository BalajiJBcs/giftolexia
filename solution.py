import csv

def get_subordinate_ids(employee_id, data):
    """
    Recursively retrieves all subordinate employee IDs under the given employee ID.

    Args:
        employee_id (int): The ID of the employee whose subordinates are to be retrieved.
        data (list of tuples): The dataset containing information about employees,
            where each tuple represents an employee record in the format (id, manager_id, name, designation).

    Returns:
        list of int: A list containing the IDs of all subordinate employees, including the given employee.

    Example:
        >>> data = [(10, None, 'Ashley Davis', 'plant manager (fabrication)'),
        ...         (20, None, 'Bob Smith', 'marketing manager'),
        ...         (30, 10, 'Abigayle Heathcote', 'foreman(fabrication)'),
        ...         (40, 10, 'Ayana Greenfelder MD', 'plant manager(assembly)'),
        ...         (50, 30, 'Erik Hand', 'worker (fabrication)'),
        ...         (60, 40, 'Alexis Becker', 'foreman(assembly)'),
        ...         (70, 50, 'Jasper Dach', 'worker (fabrication)'),
        ...         (80, 50, 'Sierra Gerhold', 'worker(assembly)'),
        ...         (90, 60, 'Sierra Gerhold', 'worker(assembly)'),
        ...         (100, 60, 'Clemmie Blanda', 'worker(assembly)')]
        >>> get_subordinate_ids(40, data)
        [40, 60, 90, 100]
    """
    subordinate_ids = [employee_id]
    for record in data:
        if record[1] == employee_id:  # Check if the record's manager_id matches the given employee_id
            subordinate_ids += get_subordinate_ids(record[0], data)
    return subordinate_ids

def get_report_subset(employee_id, data):
    """
    Retrieves a subset of the dataset that the employee with the given ID can view.

    Args:
        employee_id (int): The ID of the employee for whom the subset of data is to be retrieved.
        data (list of tuples): The dataset containing information about employees,
            where each tuple represents an employee record in the format (id, manager_id, name, designation).

    Returns:
        list of tuples: A subset of the dataset containing only the records that the employee with
            the given ID has permission to view.
    """
    employee_subordinates = get_subordinate_ids(employee_id, data)
    return [record for record in data if record[0] in employee_subordinates]


def read_data_from_csv(file_path):
    """
    Reads employee data from a CSV file and converts it into a list of lists.

    Args:
        file_path (str): The path to the CSV file containing employee data.

    Returns:
        list of lists: A list of lists representing employee records. Each inner list
            contains four elements: [employee_id, manager_id, name, designation].
    """
    
    data = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data.append([int(row[0]), int(row[1]) if row[1] else None, row[2], row[3]])
    return data

# Path to the CSV file
csv_file_path = 'org_data.csv'

# Read data from the CSV file
data = read_data_from_csv(csv_file_path)

# Test cases
print(get_report_subset(40, data))  # Output for E.g 1
print(get_report_subset(10, data))  # Output for E.g 2
