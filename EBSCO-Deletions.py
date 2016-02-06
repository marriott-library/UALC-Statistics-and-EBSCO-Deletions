# EBSCO Deletions Helper
#
# Expects to be run in the same directory as a file called [REMOVALS].txt which contains one removal ID per line.
# Expects that a folder called [CSVs] is also in the same directory, and that [CSVs] contains CSV reports from ALMA.
# Output can be copied from the terminal or piped to a file. Errors are not handled so files must be properly-formatted.
#
# Script should be run using Python 3 or higher. Example command for Mac OS X to pipe to a file (run in same directory):
#     python3 EBSCO-Deletions.py > Output.txt

import csv
import os
import re

def ingest_removals(removals_path):
    removal_ids = set()
    with open(removals_path, newline='') as removals_txt:
        for line in removals_txt:
            removal_ids.add(int(line))
    return removal_ids

def ingest_reports(reports_path):
    alma_titles = {}

    for report_filename in os.listdir(reports_path):
        if report_filename.endswith(".csv"):
            with open(reports_path + os.path.sep + report_filename, newline='') as report_csv:
                report_reader = csv.reader(report_csv)
                next(report_reader) # Skips the first row in each file, which is a header row.

                for row in report_reader:
                    match = re.search("EBSC [0-9]*;", row[1])
                    if match:
                        alma_titles[int(row[1][match.start() + 5 : match.end() - 1])] = int(row[0])

    return alma_titles

if __name__ == '__main__':
    removals_path = os.getcwd() + os.path.sep + "[Removals].txt"
    reports_path = os.getcwd() + os.path.sep + "[CSVs]"

    removal_ids = ingest_removals(removals_path)
    alma_titles = ingest_reports(reports_path)

    for removal_id in removal_ids:
        if removal_id in alma_titles :
            print(alma_titles[removal_id])
