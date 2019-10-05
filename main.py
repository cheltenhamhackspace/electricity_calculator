#!/usr/bin/env python3
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-location",
                    "-l",
                    dest="loc",
                    help="Location of csv file")
args = parser.parse_args()
print(args)


def load_csv(file_loc):
    csv_dict = csv.DictReader(file_loc, delimiter=',')
    return csv_dict




