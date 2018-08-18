'''
Filename: main.py
Author: Sean C
Date: 20180817
Ask:
	Read in Budge Data and calculate certain metrics
Purpose: 
	Homework

================
===Psuedocode===
================
1.Read in csv file 
2a.Count number of values in the first column
	2b.Put into variable int (totalMonths)
3a.Sum all values in second column 
	3b.Put into variable int (totalProfit)
4a.List comprehension the differences into variable list (differences)
	4b.count number of elements into variable int (changes)
		4c.calculate average of changes into variable float (avgChanges)
5a.Create 4 variables (currentMonthIdxP, lastMonthIdxP, isPositiveChg, largestProfit)
	5b.Loop through table starting from Idx 2 as currentMonthIdxP and currentMonthIdxP -1  as lastMonthIdxP assign variables appropriately
6a.Create 4 variables (currentMonthIdxL, lastMonthIdxL, isNegativeChg, largestLoss)
	6b.Loop through table starting from Idx 2 as currentMonthIdxL and currentMonthIdxL -1  as lastMonthIdxL assign variables appropriately	

### Things You Should Know ###

'''
###########################
####Import Statement(s)####
###########################
import pandas as pd

###########################
#########Variables#########
###########################
#Anything that can be declared ahead of time
filePath = 'C:\\Users\\Shawn\\Desktop\\python-challenge\\PyBank\\'
filename = 'C:\\Users\\Shawn\\Desktop\\python-challenge\\PyBank\\budget_data.csv'

df = pd.read_csv(filename)
totalMonths = df.shape[0]	#After analyzing the data we know the count of rows is equal to the number of months.  Hence we can use the first value in shape()
totalProfit = df['Revenue'].sum()
#print(totalMonths, totalProfit)
revenueValues = list(df['Revenue'])
dateValues = list(df['Date'])
#print(revenueValues)
#print(dateValues)
absDiff = []
for idx,item in enumerate(revenueValues[:-1]):
	#print('[' + str(idx) + ' : Index number' + '] [' + str(item) + ': Value at Index]' )
	#print('[' + str(idx + 1) + ' : Index number' + '] [' + str(revenueValues[idx + 1]) + ': Value at Index]' )
	#print('LastMonth = %d , CurrentMonth = %d ,  %d - %d = %d' % (item,revenueValues[idx + 1],item,revenueValues[idx + 1], item - revenueValues[idx + 1]) )
	#print('The absolute value of the difference = %d (This is change)' % (abs(item - revenueValues[idx + 1])))
	absDiff.append(abs(item - revenueValues[idx + 1]))						
#print(absDiff)
numIdxAbsDiff = len(absDiff)
sumAbsDiff = sum(absDiff)
avgAbsDiff = float(sumAbsDiff)/float(numIdxAbsDiff)
#print('Number of elements in absDiff = %d' % (numIdxAbsDiff))
#print('Sum of elements in absDiff = %d' % (sumAbsDiff))
#print('Average of absDiff = %.2f' % (avgAbsDiff))

lnum = 0 #last_Number
cnum = 0 #current_Number
LargestProfitIdx = 0
LargestLossIdx = 0
LargestProfitNum = 0
LargestLossNum = 0

for idx,item in enumerate(revenueValues[:-1]):
	lnum = revenueValues[idx]
	cnum = revenueValues[idx + 1]
	if cnum > lnum:
		#if true then this is a positive change
		if cnum > LargestProfitNum:
			#if this is true then it is the new Largest Profit
			#set the variables
			LargestProfitNum = cnum
			LargestProfitIdx = idx + 1

lnum = 0 #last_Number
cnum = 0 #current_Number
for idx,item in enumerate(revenueValues[:-1]):
	lnum = revenueValues[idx]
	cnum = revenueValues[idx + 1]
	if cnum < lnum:
		#if true then this is a negative change
		if cnum < LargestLossNum:
			#if this is true then it is the new Largest Loss
			#set the variables
			LargestLossNum = cnum
			LargestLossIdx = idx + 1

#print('The largest profit was %d and it occured at date %s' % (LargestProfitNum, dateValues[LargestProfitIdx]))
#print('The largest loss was %d and it occured at date %s' % (LargestLossNum, dateValues[LargestLossIdx]))

FinAnalysis = "Financial Analysis \n" +\
	"---------------------------- \n" +\
	"Total Months : %d \n" % (totalMonths) +\
	"Total : %d \n" % (totalProfit) +\
	"Average Change : $%.2f \n" % (avgAbsDiff) +\
	"Greatest Increase in Profits : %s ($%d) \n" % (dateValues[LargestProfitIdx],LargestProfitNum) +\
	"Greatest Decrease in Profits : %s ($%d)" % (dateValues[LargestLossIdx],LargestLossNum)
	
print(FinAnalysis)
newFile = filePath + "Financial_Analysis.txt"
f = open(newFile, "w")
f.write(FinAnalysis)


































