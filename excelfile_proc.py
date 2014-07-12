# -*- coding: UTF-8 -*-
import csv
import xlrd
import comm

DBG_ConfigProductTitle = ['田园成品窗帘 隔热全遮光布 客厅卧室定制遮阳窗帘布特价清仓星星',\
						 '窗帘遮光布料成品宜家田园卧室客厅定制飘窗帘布窗纱特价清仓波点',\
						 '欧式成品清仓 定制拼接半遮光窗帘高档客厅卧室提花窗帘布料特价']
DBG_ConfigProductName = ['星星',\
						 '左右爱',\
						 '瓶安锦绣']						 
DBG_ConfigProductData = ['', '', '']


# Find one value in one list, return the position of that value, if
# the value can't be find, return -1.
# 2014-7-12 add comment
def findInList(list, value):
	try:
		pos = -1
		for i in range(0, len(list)):
			if (list[i] == value):
				pos = i
				break
		return pos		
	except:
		print ("In findInList: findInList Exception!!!")

# Get the product name according to the title		
def getProductName(title):
	try:
		pos = findInList(DBG_ConfigProductTitle, title)
		if (pos != -1):
			return DBG_ConfigProductName[pos]
		else:
			print("In getProductName: can not find product name, title = %s" % (title))
	except:
		print ("getProductName: Invalid Product Title!!!")

# Get product's basic data from line which read from the csv file
# and composite into new record
# line[2] : product title
# line[6] : sales
# line[8] : order
# format: rank:星星@13074.28@114@1/5/2@-1
def getProductData(line):
	productName = getProductName(line[2])
	productSale = line[6]
	productOrder = line[8]
	
	return ("rank:" + productName + "@" + productSale + "@" + productOrder + "@")
	

# Process the csv file, and format the product data, all the formated
# product date store in the globle variable 'DBG_ConfigProductData'
def DRG_GetProductInfo(filename):
	with open(filename, newline='') as f:
		reader = csv.reader(f)
		
		for line in reader:
			pos = findInList(DBG_ConfigProductTitle, line[2])
			if (pos != -1):
				productInfo = getProductData(line)
				DBG_ConfigProductData[pos] = productInfo			
		
	return True

# Append the rankinfo to DBG_ConfigProductData
def addRankInfo(productName, rankInfo):
	for i in range(len(DBG_ConfigProductData)):
		if (DBG_ConfigProductData[i].find(productName) >= 0):
			DBG_ConfigProductData[i] = DBG_ConfigProductData[i] + rankInfo
			#print ("in addRankInfo", productName, DBG_ConfigProductData[i])	

# Get the product's current rank and caculate compare info 
def searchRankInfo(productName, x, y, table):
	currentRankInfo = table.cell(x,y).value
	
	for i in range(x, 0, -1):
		lastRankInfo = table.cell(i-1,y).value
		if (lastRankInfo != ''):
			break
	
	curRankArray = currentRankInfo.split("/")
	lstRankArray = lastRankInfo.split("/")
	
	curRank = (int(curRankArray[0])-1)*13*4 + (int(curRankArray[1])-1)*4 + int(curRankArray[2])
	lstRank = (int(lstRankArray[0])-1)*13*4 + (int(lstRankArray[1])-1)*4 + int(lstRankArray[2])
	comRank = lstRank - curRank
	
	return (currentRankInfo + "@" + str(comRank))
	
# Get rank info from the excel handle	
def getRankInfoByName(productName, sheetHandle):
	table = sheetHandle.sheets()[0]
	productList = table.row_values(0)
	dateList = table.col_values(1)
	
	statDate = comm.DRG_GetStatisticDate()
	#print (statDate)
	for j in range(len(productList)):
		if (productName == productList[j]):	
			for i in range(len(dateList)):
				if (statDate == dateList[i]):
					return searchRankInfo(productName, i, j, table)
			
	return ""	
	
# Check if the sheet date is ok
# 2014-7-12 create
def isSheetLatest(sheetHandle):
	table = sheetHandle.sheets()[0]	
	dateList = table.col_values(1)
	
	statDate = comm.DRG_GetStatisticDate()
	for i in range(len(dateList)):
		if (statDate == dateList[i]):
			return True
	return False
	
# Process the csv file, and get rank info from EXCEL file
def DRG_GetRankInfo(filename, productList):
	sheetHandle = xlrd.open_workbook(filename)
	if (isSheetLatest(sheetHandle) == False):
		print ("In DRG_GetRankInfo, sheet data error!")
		return False
	
	for item in productList:
		header = item.split("@")[0]
		if (header.find("rank") >= 0):
			productName = header.split(":")[-1]
			rankInfo = getRankInfoByName(productName, sheetHandle)
			addRankInfo(productName, rankInfo)
	