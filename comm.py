# -*- coding: UTF-8 -*-
import datetime

def DRG_GetStatisticDate():
	statDate = datetime.date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day) \
		- datetime.timedelta(1)
		
	return (str(statDate))
		
	