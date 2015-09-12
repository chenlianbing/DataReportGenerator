#!/bin/bash
# Many numbers in file and each number in one line, output the max number in this file.

E_BADARGS=85
FILE_PARSE=$1

if [ ! -e $FILE_PARSE ] # can also use "if [ -z $1]"
then
  echo "Usage: `basename $0` filename."
  exit $E_BADARGS
fi

#cat $FILE_PARSE | while read line
#do
#  #echo ${line}
#  if [[ $max_number -lt ${line} ]]
#  then
#    echo $line
#    echo "before, max_number=$max_number"
#    max_number=${line}
#    hh=$max_number
#    echo "after, max_number=$max_number"
#  fi
#done
# Really fussed about this problem, it can not work, the max_number is always equals 0.

cat $FILE_PARSE |
awk '
BEGIN {
  max_number=0;
}

{ if (max_number < $0)
    max_number = $0
}
END {
  print "max_number=", max_number;
}'

exit 0
