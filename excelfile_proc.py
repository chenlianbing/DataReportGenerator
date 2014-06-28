# -*- coding: UTF-8 -*-
import csv
import xlrd

DBG_ConfigProductTitle = ['田园成品窗帘 隔热全遮光布 客厅卧室定制遮阳窗帘布特价清仓星星',\
						 '窗帘遮光布料成品宜家田园卧室客厅定制飘窗帘布窗纱特价清仓波点',\
						 '欧式成品清仓 定制拼接半遮光窗帘高档客厅卧室提花窗帘布料特价']
DBG_ConfigProductName = ['星星',\
						 '左右爱',\
						 '瓶安锦绣']						 
DBG_ConfigProductData = ['', '', '']


# Find one value in one list, return the position of that value, if
# the value can't be find, return -1
def findInList(list, value):
	try:
		pos = -1
		for i in range(0, len(list)):
			if (list[i] == value):
				pos = i
				break
		return pos		
	except:
		print ("findInList Exception!!!")

# Get the product name according to the title		
def getProductName(title):
	try:
		pos = findInList(DBG_ConfigProductTitle, title)
		if (pos != -1):
			return DBG_ConfigProductName[pos]
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
	print (filename)
	with open(filename, newline='') as f:
		reader = csv.reader(f)
		
		for line in reader:
			pos = findInList(DBG_ConfigProductTitle, line[2])
			if (pos != -1):
				productInfo = getProductData(line)
				DBG_ConfigProductData[pos] = productInfo			
		
	return True
	

def getRankInfoByName(productName, sheetHandle):
	table = sheetHandle.sheets()[0]
	productList = table.row_values(0)
	
	statDate = DRG_GetStatisticDate();
	for i in range(len(productList)):
		print (productList[i])
	
# Process the csv file, and get rank info from EXCEL file
def DRG_GetRankInfo(filename, productList):
	sheetHandle = xlrd.open_workbook(filename)
	
	for item in productList:
		header = item.split("@")[0]
		if (header.find("rank") >= 0):
			productName = header.split(":")[-1]
			rankInfo = getRankInfoByName(productName, sheetHandle)
			
			print ("In DRG_GetRankInfo", productName)

	pass