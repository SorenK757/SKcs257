''' cli.py
    Soren Kaster
    4/17/2025

    NAME: cli.py - command-line interface exercise
    SYNOPSIS: python3 cli.py marksby athletename
    DESCRIPTION: Counts number of polevault performances above given height by given athlete name, case-insensitively.
'''

import argparse
import csv


def get_parsed_arguments():
    parser = argparse.ArgumentParser(description="Counts the number of marks an athlete of given name has cleared above given height in the pole vault and lists them. Athlete is listed first in either 'First Last' or 'Last, First' format, case-senstitive. Height is listed second in meters.")
    parser.add_argument('athletename', help="First command. Athlete to get performance list of. Athlete is listed first in either 'First Last' or 'Last, First' format, case-senstitive.")
    parser.add_argument('height', help='Second command. Height athlete may have cleared in polevault in meters')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def name_swap(name):
    if ',' in name:
        parts = name.split(", ")
        name = f'{parts[1]} {parts[0]}'
    else:
        parts = name.split(" ")
        name = f'{parts[1]}, {parts[0]}'
    return name


def main():
    count = 0
    list = []
    arguments = get_parsed_arguments()
    name = arguments.athletename
    if ',' not in arguments.athletename:
        name = name_swap(arguments.athletename)
    with open('data/MIAC_data.csv') as f:
        reader = csv.reader(f)
        for performance_row in reader:
            if name in performance_row[7]:
                if performance_row[8] == 'Pole Vault':
                    if arguments.height <= performance_row[10]:
                        list.append(f'{name_swap(name)} jumped {performance_row[10]} on {performance_row[2]}')
                        count += 1

    print(name_swap(name), 'cleared over', arguments.height, 'meters', count, 'times!')
    for i in list:
        print()
        print(i)


main()
