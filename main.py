import re
import os
import sys

DRG_CURR_PATH = os.path.abspath(os.path.dirname(sys.argv[0]))
DRG_TEST_PATH = DRG_CURR_PATH + "\Test"
print (DRG_CURR_PATH)
print (DRG_TEST_PATH)

# Read source data from input_data.txt, located in path: report.txt
os.chdir(DRG_TEST_PATH)

read_file = open("input_data.txt", "r")
write_file = open("report.txt", "w")

# output sentences
def DRG_GetOutputLine(sales, order, rank, compareRank):
	salesStr = "销售额 " + sales +"元。"
	orderStr = "销售笔数 " + order + " 笔。"
	rankStr = "排名 " + rank + " 名。"
	
	intComRank = int(compareRank)
	if (intComRank > 0):
		rankCompareStr = "排名相比前一天上升 " + str(intComRank) + " 名。"
	elif (intComRank == 0):
		rankCompareStr = "排名与前一天持平。"
	else:
		rankCompareStr = "排名相比前一天降低 " + str(-intComRank) + " 名。"	
	
	return (salesStr + orderStr + rankStr + rankCompareStr)
	
# Parse function
def DRG_ParseLine(input_line):
	print (input_line)
	if re.match("rank", input_line ):
		rank_list = re.split('/', input_line)
		print (rank_list)
		return_line = DRG_GetOutputLine(rank_list[1], rank_list[2], rank_list[3], rank_list[4])
    
		return return_line
	return ""

# Read each line and do transforming
for read_line in read_file:
    out_line = DRG_ParseLine(read_line)
    print (out_line)
    write_file.write("\r\n" + out_line)

# Close the opened file
write_file.close()
read_file.close()

