# -*- coding: UTF-8 -*-

import os
import sys
from textline_proc import DRG_GetOutputLine, DRG_ParseLine

DRG_CURR_PATH = os.path.abspath(os.path.dirname(sys.argv[0]))
DRG_TEST_PATH = DRG_CURR_PATH + "\Test"
print (DRG_CURR_PATH)
print (DRG_TEST_PATH)

# Read source data from input_data.txt, located in path: report.txt
os.chdir(DRG_TEST_PATH)


read_file = open("input_data.txt", "r")
write_file = open("report.txt", "w")

# Read each line and do transforming
for read_line in read_file:
    out_line = DRG_ParseLine(read_line)
    print (out_line)
    write_file.write("\r\n" + out_line)

# Close the opened file
write_file.close()
read_file.close()

