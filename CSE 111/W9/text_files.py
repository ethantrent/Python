# TEXT FILES

"""The built-in open function opens a file for reading or writing. Here is an excerpt from the official documentation for 
the open function:

open(filename, mode="rt")
Open a file and return a corresponding file object.

filename is the name of the file to be opened.

mode is an optional string that specifies the mode in which the file will be opened. It defaults to "rt" which means open for 
reading in text mode. Other common values are "wt" for writing a text file (truncating the file if it already exists), 
and "at" for appending to the end of a text file."""

# Example 1

def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    text_list = read_list("plants.txt")

    # Print the entire list.
    print(text_list)


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# Call main to start this program.
if __name__ == "__main__":
    main()

"""After the body of a for loop that reads from a file, we can write a call to the file.close method. 
However, when calling the open function, most programmers use a with block and nest the for loop inside 
the with block. When the with block ends, the computer will automatically close the file, so that the programmer 
doesn't have to write a call to the file.close method."""

# CSV FILES

"""CSV is an acronym for comma separated values. A CSV file is a text file that contains tabular data with each row 
on a separate line of the file and each cell (column) separated by a comma."""

# Example 2

import csv

def main():
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open("hymns.csv", "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            print(row_list)


# Call main to start this program.
if __name__ == "__main__":
    main()


# PROCESSING EACH ROW IN A CSV FILE

"""After reading each row from a CSV file, the for loop in the previous example simply prints the row list to a terminal window."""

# Example 3

import csv

# Indexes of some of the columns
# in the dentists.csv file.
COMPANY_NAME_INDEX = 0
NUM_EMPS_INDEX = 3
NUM_PATIENTS_INDEX = 4


def main():
    # Open a file named dentists.csv and store a reference
    # to the opened file in a variable named dentists_file.
    with open("dentists.csv", "rt") as dentists_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(dentists_file)

        # The first row of the CSV file contains column
        # headings and not data about a dental office,
        # so this statement skips the first row of the
        # CSV file.
        next(reader)

        running_max = 0
        most_office = None

        # Read each row in the CSV file one at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # For the current row, retrieve the
            # values in columns 0, 3, and 4.
            company = row_list[COMPANY_NAME_INDEX]
            num_employees = int(row_list[NUM_EMPS_INDEX])
            num_patients = int(row_list[NUM_PATIENTS_INDEX])

            # Compute the number of patients per
            # employee for the current dental office.
            patients_per_emp = num_patients / num_employees

            # If the current dental office has more
            # patients per employee than the running
            # maximum, assign running_max and most_office
            # to be the current dental office.
            if patients_per_emp > running_max:
                running_max = patients_per_emp
                most_office = company

    # Print the results for the user to see.
    print(f"{most_office} has {running_max:.1f}"
            " patients per employee")


# Call main to start this program.
if __name__ == "__main__":
    main()


# READING A CSV FILE INTO A COMPOUND LIST

"""The program in example 3 reads and processes each row in a CSV file. 
That program needs to access the data in each row once only. If a program needs to access the contents of 
a CSV file multiple times, the program can read the contents of the file into a compound list and then access 
the data from the list. The program in example 4 contains a function named read_compound_list that reads the 
contents of a CSV file into a compound list."""

# Example 4

import csv

def main():
    # Read the contents of the dentists.csv file
    # into a compound list.
    dentists_list = read_compound_list("dentists.csv")

    # Print the entire list.
    print(dentists_list)


def read_compound_list(filename):
    """Read the contents of a CSV file into a compound
    list and return the list. Each element in the
    compound list will be a small list that contains
    the values from one row of the CSV file.

    Parameter filename: the name of the CSV file to read
    Return: a list of lists that contain strings
    """
    # Create an empty list that will
    # store the data from the CSV file.
    compound_list = []

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank,
            # append it to the compound_list.
            if len(row_list) != 0:

                # Append one row from the CSV
                # file to the compound list.
                compound_list.append(row_list)

    # Return the compound list.
    return compound_list


# Call main to start this program.
if __name__ == "__main__":
    main()

# READING A CSV FILE INTO A COMPOUND DICTIONARY

"""If the values in one of the columns of a CSV file are unique, then a progam can read the contents of a CSV file 
into a compound dictionary and then use the dictionary to quickly find data. Recall that each item in a dictionary 
is a key value pair."""

# Example 5

import csv


def main():
    # Index of the phone number column
    # in the dentists.csv file.
    PHONE_INDEX = 2

    # Read the contents of the dentists.csv into a
    # compound dictionary named dentists_dict. Use
    # the phone numbers as the keys in the dictionary.
    dentists_dict = read_dictionary("dentists.csv", PHONE_INDEX)

    # Print the dentists compound dictionary.
    print(dentists_dict)


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()