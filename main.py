#!/usr/bin/env python3
import sys
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
        main_list = []
        for row in csv_dict:
            if line == 0:
                headers.extend(row)
                print(headers)
            else:
                temp_dict = {}
                for item in row:
                    print(item)
                    temp_dict[headers[row.index(item)]] = item
                main_list.append(temp_dict)
            line += 1
        print(main_list)






if __name__ == "__main__":
    csv_to_dict(args.PATH)
