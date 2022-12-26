"""Utility functions for wrangling data."""

from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    rows: list[dict[str, str]] = []
    for row in csv_reader:
        rows.append(row)
    file_handle.close()    
    return rows


def column_values(rows: list[dict[str, str]], key: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    values: list[str] = []
    for row in rows:
        values.append(row[key])
    return values    


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows (e.g. list[dict[str, str]]) into one."""
    """represented as a dictionary of columns (e.g. dict[str, list[str]])."""
    col_data: dict[str, list[str]] = {}
    for row in rows[0].keys():
        values: list[str] = column_values(rows, row)
        col_data[row] = values
    return col_data    


def head(not_mutated_data: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. dict[str, list[str]]) table with."""
    """only the first N (a parameter) rows of data for each column."""
    goal: dict[str, list[str]] = {}
    i: int = 0
    for columns in not_mutated_data.keys():
        i = 0
        first_n_values: list[str] = []
        if number_of_rows >= 348:
            for values in columns:
                while i < 348:
                    first_n_values.append(not_mutated_data[columns][i])
                    i += 1
        else:        
            for values in columns:
                while i < number_of_rows:
                    first_n_values.append(not_mutated_data[columns][i])
                    i += 1
        goal[columns] = first_n_values                
    return goal


def select(data: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. dict[str, list[str]]) table with only."""
    """a specific subset of the original columns."""
    goal: dict[str, list[str]] = {}
    i: int = 0
    while i < len(names):
        goal[names[i]] = data[names[i]]
        i += 1
    return goal 


def count(values: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique."""
    """value in the given list and each value associated is the count of the number of times that."""
    """value appeared in the input list."""
    goal: dict[str, int] = {}
    for item in values:
        if item in goal:
            goal[item] += 1
        else:
            goal[item] = 1    
    return goal


def non_comp_major(subset: dict[str, list[str]]) -> list[bool]:
    """Given a dict[str, list[str]], this function will produce a list[bool]."""
    """If the person was a non-comp major the answer will be true."""
    result: list[bool] = []
    for item in subset['comp_major']:
        result.append(item == 'No')
    return result


def masked(subset: dict[str, list[str]], mask: list[bool], selection: str) -> list[str]:
    """If selection is true it'll return a list of the non-comp majors grades."""
    """If selection is false it'll return a list of the comp majors grades."""
    true_result:list[str] = []
    false_result: list[str] = []
    x: int = 0
    for i in range(len(mask)):
        if mask[i]:
            true_result.append(subset['grade'][x])
        else:
            false_result.append(subset['grade'][x])
        x += 1
    if selection == "true":
        return true_result
    else:
        if selection == "false":
            return false_result
    

def grade_counts(grades: list[str]) -> dict[str, int]:
    """Counts the occurence of each grade in a list of grades."""
    counts: dict[str, int] = {}
    for character in grades:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    return counts