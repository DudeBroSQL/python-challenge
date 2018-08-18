'''
Filename: main.py
Author: Sean C
Date: 20180817
Ask:
	Read in election Data and calculate certain metrics
Purpose: 
	Homework

================
===Psuedocode===
================
N/A

### Things You Should Know ###
N/A

'''
###########################
####Import Statement(s)####
###########################
import pandas as pd

###########################
#########Variables#########
###########################
#Anything that can be declared ahead of time
filePath = 'C:\\Users\\Shawn\\Desktop\\python-challenge\\PyPoll\\'
filename = 'C:\\Users\\Shawn\\Desktop\\python-challenge\\PyPoll\\election_data.csv.txt'

df = pd.read_csv(filename)
totalVotes = df.shape[0]	#After analyzing the data we know the count of rows is equal to the number of months.  Hence we can use the first value in shape()
#print(totalMonths, totalProfit)
candidateValues = list(set(list(df['Candidate'])))
#print(totalVotes)
#print(candidateValues)

candidateTally = {}
for el in candidateValues:
	candidateTally[el] = 0
	#print(candidateTally)
for el in df['Candidate']:
	#print(el)
	tal = candidateTally[el]
	#print(tal)
	candidateTally.update({el: tal + 1})
	#if el == 100:  #if statement for testing
	#	break
candidateTallyPercent = {}
for key in candidateTally:
	candidateTallyPercent[key] = float(candidateTally[key])/float(totalVotes)
#print(candidateTallyPercent)
winner = ""
winningVal = 0
for k in candidateTally:
	if candidateTally[k] > winningVal:
		winningVal = candidateTally[k]
		winner = k

totals = ""
for k in candidateTally:
	totals = totals + "%s: %.3f (%d) \n" % (k,candidateTallyPercent[k]*100,candidateTally[k]) 
	#print(k,candidateTallyPercent[k],candidateTally[k])
#print(totals)

electionRes = "Election Results \n" +\
	"---------------------------- \n" +\
	"Total Votes : %d \n" % (totalVotes) +\
	"---------------------------- \n" +\
	"%s" % (totals) +\
	"---------------------------- \n" +\
	"Winner: %s \n" % (winner) +\
	"---------------------------- \n"

print(electionRes)	
newFile = filePath + "election_Analysis.txt"
f = open(newFile, "w")
f.write(electionRes)


































