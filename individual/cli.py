''' CLI Assignment
    Soren Kaster
    4/17/2025

    NAME: cli.py - command-line interface exercise
    SYNOPSIS: python3 cli.py marksby athletename
    DESCRIPTION: Shows a list of the marks of all the performances by any
    athlete whos name contains the specified athletename string, case-insensitively.
'''

import argparse
import csv


def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Shows a list of the marks of all the performances by any athlete whos name contains the specified athletename string, case-insensitively.')
    parser.add_argument('athletename', help='1 or more athlete to get performance list of')
    parsed_arguments = parser.parse_args()
    return parsed_arguments



def main():
    arguments = get_parsed_arguments()
    with open('data/MIAC_data.csv') as f:
        reader = csv.reader(f)
        for performance_row in reader:
            if arguments.athletename in performance_row[7]:
                print(performance_row)

            


main()
