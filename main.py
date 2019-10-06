#!/usr/bin/env python3
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("PATH",
                    type=str,
                    help="Location of csv file")
args = parser.parse_args()


def csv_to_dict(file_loc):
    with open(file_loc, mode="r") as csv_file:
        csv_dict = csv.reader(csv_file, delimiter=',')
        line = 0
        headers = []
        temp_list = []
        for row in csv_dict:
            if line == 0:
                headers.extend(row)
            else:
                temp_dict = {}
                item_loc = 0
                for item in row:
                    temp_dict[headers[item_loc]] = item
                    item_loc += 1
                temp_list.append(temp_dict)
            line += 1
        return temp_list


if __name__ == "__main__":
    print(csv_to_dict(args.PATH))
