# -*- coding: UTF-8 -*-

import os
import sys
import textline_proc
import excelfile_proc

#from textline_proc import textline_proc.DRG_GetOutputLine, DRG_ParseLine
#from excelfile_proc import DRG_GetProductInfo, DRG_GetRankInfo, DBG_ConfigProductData

DRG_CURR_PATH = os.path.abspath(os.path.dirname(sys.argv[0]))
DRG_TEST_PATH = DRG_CURR_PATH + "\Test"
print (DRG_CURR_PATH)
print (DRG_TEST_PATH)
os.chdir(DRG_TEST_PATH)

# Stage I: Read data from EXCEL file, and write to input_data.txt
procRes = excelfile_proc.DRG_GetProductInfo("baobei-20140618.csv")
if (procRes == False):
	print ("Err.")
else:
	for item in excelfile_proc.DBG_ConfigProductData:
		print (item)
	
procRes = excelfile_proc.DRG_GetRankInfo("销量排名记录.xls", excelfile_proc.DBG_ConfigProductData)	
if (procRes == False):
	print ("Err.")
	
	'''
# Stage II: Parse data from input_data and write to report.txt
read_file = open("input_data.txt", "r")
write_file = open("report.txt", "w")

# Read each line and do transforming
for read_line in read_file:
	out_line = textline_proc.DRG_ParseLine(read_line)
	
	if(out_line != "Invalid Line"):
		print (out_line)
		write_file.write("\r\n" + out_line)

# Close the opened file
write_file.close()
read_file.close()
'''
