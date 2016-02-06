# UALC Stats Helper (Pioneer Stats)
#
# Expects to be run in the same directory as a file called [RAW-STATS].csv which contains Pioneer database statistics.
#
# [RAW-STATS].csv must have no column headers and no blank lines, and each row must be formatted as follows:
#     Database Name, Site, Month, Searches, Views, Downloads
#
# STATS MUST NOT SPAN A CALENDAR YEAR BREAK - DO NOT INCLUDE STATS FROM, FOR EXAMPLE, 2015 AND 2016 IN THE SAME CSV!
#
# Output can be copied from the terminal or piped to a file. Errors are not handled so files must be properly-formatted.
#
# Script should be run using Python 3 or higher. Example command for Mac OS X to pipe to a file (run in same directory):
#     python3 UALC-Pioneer.py > Output.csv

import csv
import os
import re

def ingest_stats(stats_path):
    stats = []

    if stats_path.endswith(".csv"):
        with open(stats_path, newline= '') as stats_csv:
            stats_reader = csv.reader(stats_csv)

            school_stats = ["-", "-", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

            for row in stats_reader:
                school_name = row[1]
                if school_name != school_stats[1]:
                    if school_stats[0] == "-":
                        # On the first iteration, school_stats must be set to the correct database and school name for the first row, since above it was set to a default value.
                        school_stats = [row[0], school_name, "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
                    else:
                        # Appends the previous row's stats and starts a row for a new school each time a new school is encountered.
                        stats.append(school_stats[0] + ',' + school_stats[1] + ',' + school_stats[2] + ',' + school_stats[3] + ',' + school_stats[4] + ',' + school_stats[5] + ',' + school_stats[6] + ',' + school_stats[7] + ',' + school_stats[8] + ',' + school_stats[9] + ',' + school_stats[10] + ',' + school_stats[11] + ',' + school_stats[12] + ',' + school_stats[13] + ',' + school_stats[14] + ',' + school_stats[15] + ',' + school_stats[16] + ',' + school_stats[17] + ',' + school_stats[18] + ',' + school_stats[19] + ',' + school_stats[20] + ',' + school_stats[21] + ',' + school_stats[22] + ',' + school_stats[23] + ',' + school_stats[24] + ',' + school_stats[25] + ',' + school_stats[26] + ',' + school_stats[27] + ',' + school_stats[28] + ',' + school_stats[29] + ',' + school_stats[30] + ',' + school_stats[31] + ',' + school_stats[32] + ',' + school_stats[33] + ',' + school_stats[34] + ',' + school_stats[35] + ',' + school_stats[36] + ',' + school_stats[37])
                        school_stats = [row[0], school_name, "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

                # Parses out the current month that the row being processed corresponds to.
                month_offset = ((int(row[2]) - 1) * 3) + 2

                # Puts the searches stat from the current row into the correct place within school_stats.
                school_stats[month_offset] = row[3]

                # Puts the views stat from the current row into the correct place within school_stats.
                school_stats[month_offset + 1] = row[4]

                # Puts the downloads stat from the current row into the correct place within school_stats.
                school_stats[month_offset + 2] = row[5]

            # Appends the last row of stats.
            stats.append(school_stats[0] + ',' + school_stats[1] + ',' + school_stats[2] + ',' + school_stats[3] + ',' + school_stats[4] + ',' + school_stats[5] + ',' + school_stats[6] + ',' + school_stats[7] + ',' + school_stats[8] + ',' + school_stats[9] + ',' + school_stats[10] + ',' + school_stats[11] + ',' + school_stats[12] + ',' + school_stats[13] + ',' + school_stats[14] + ',' + school_stats[15] + ',' + school_stats[16] + ',' + school_stats[17] + ',' + school_stats[18] + ',' + school_stats[19] + ',' + school_stats[20] + ',' + school_stats[21] + ',' + school_stats[22] + ',' + school_stats[23] + ',' + school_stats[24] + ',' + school_stats[25] + ',' + school_stats[26] + ',' + school_stats[27] + ',' + school_stats[28] + ',' + school_stats[29] + ',' + school_stats[30] + ',' + school_stats[31] + ',' + school_stats[32] + ',' + school_stats[33] + ',' + school_stats[34] + ',' + school_stats[35] + ',' + school_stats[36] + ',' + school_stats[37])
    return stats

if __name__ == '__main__':
    stats_path = os.getcwd() + os.path.sep + "[RAW-STATS].csv"
    new_stats = ingest_stats(stats_path)

    # Prints column headers for the CSV, then prints each row of statistics which were read from the input file.
    print("Database,School,Searches (Jan),Views (Jan),Downloads (Jan),Searches (Feb),Views (Feb),Downloads (Feb),Searches (Mar),Views (Mar),Downloads (Mar),Searches (Apr),Views (Apr),Downloads (Apr),Searches (May),Views (May),Downloads (May),Searches (Jun),Views (Jun),Downloads (Jun),Searches (Jul),Views (Jul),Downloads (Jul),Searches (Aug),Views (Aug),Downloads (Aug),Searches (Sep),Views (Sep),Downloads (Sep),Searches (Oct),Views (Oct),Downloads (Oct),Searches (Nov),Views (Nov),Downloads (Nov),Searches (Dec),Views (Dec),Downloads (Dec)")
    for stat_row in new_stats:
        print(stat_row)
