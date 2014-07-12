# -*- coding: UTF-8 -*-
import datetime

# Get data statistic date.
# 2014-7-12 add comment
def DRG_GetStatisticDate():
	statDate = datetime.date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day) \
		- datetime.timedelta(1)
		
	return (str(statDate))
		
# Construct Product Sales Table Name
# 2014-7-12 create
def DRG_GetSalesTableName():
	strDate = DRG_GetStatisticDate()
	strDate = strDate.replace('-', '')
	
	filename = "baobei-" + strDate + ".csv"	
	return filename