import re

# Read source data from sourcedata.txt, located in path: F:/store_data_holly.txt
read_file = open("F:\\Tao\\data\\report_data.txt", "r")
write_file = open("F:\\Tao\\data\\report.txt", "w")

# Parse function
def parse_line(input_line):  
    if re.match("rank", input_line ):
        rank_list = re.split("/", input_line)
        return_line = rank_list[0] + ", Sales: " + rank_list[1] + ", Order Numbers: " + \
                rank_list[2] + ", Rank: "+rank_list[3]
    
        return return_line
    return ""

# Read each line and do transforming
for read_line in read_file:
    out_line = parse_line(read_line)
    print (out_line)
    write_file.write(out_line)

# Close the opened file
write_file.close()
read_file.close()
