#!/bin/bash
#Program:
#  Given the keyword, and then extract numbers on the right of "=".
#History:
#  20150908 create

FILE_PARSE=$1
E_PARAMERR=85

usage()
{
    echo "Usage: extractor.sh file keyword" 2>&1
    # For example:   ./extractor.sh filename.log cost
    exit $E_PARAMERR  # Too few arguments passed to script.
}

if [ ! -e ${FILE_PARSE} ]; then
  echo -e "$1: No such file." 2>&1
  usage
fi

if [ -z "$2" ]; then
  echo "$2: No keyword specified." 2>&1
  usage
fi


KEYWORD=$2
mkdir ${KEYWORD}

echo -e "\n Going to parse the file ..."
echo "The log file name is:  $FILE_PARSE"
echo "The keyword is:        $KEYWORD"

#Pick up lines contained the keyword.
temp_log_file=temp.log
cat ${FILE_PARSE} | grep -i "${KEYWORD}" > ./${KEYWORD}/${temp_log_file}
echo -e "\n Generate temp log file: ${temp_log_file}."

pushd ${KEYWORD}
dos2unix ${temp_log_file}
sed -i '/^\s*$/d' ${temp_log_file} #delete blank lines.

#Cut out keyword section, which match 'keyword=num'
#for example:
# Log: pre-procmsg=1000,procmsg=2000,post-procmsg=3000
# Given the keyword 'procmsg',there're 3 steps:
# 1. procmsg=2000,post-procmsg=3000 (cut letters before 'procmsg')
# 2. procmsg=2000
# 3. 2000

#Step 1:
keyword_log_file=${KEYWORD}.log
cp ${temp_log_file} ${keyword_log_file}
sed -i "s/^.*${KEYWORD}/${KEYWORD}/g" ${keyword_log_file}

#Step 2:
temp_data_file=temp.data
cat ${keyword_log_file} | awk 'BEGIN {FS=","} $1 {print $1}' > ${temp_data_file}

#Step 3:
data_file=${KEYWORD}.data
cat ${temp_data_file} | awk 'BEGIN {FS="="} $1 {print $2}' > ${data_file}
echo -e "\n Generate data file: ${data_file}"

popd

echo -e "\n Done."
echo -e "\n"


