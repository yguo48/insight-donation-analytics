# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:04:19 2018

@author: yguo
"""

from data_validation import *
import math
import sys
from sortedcontainers import SortedList
from datetime import datetime

def DonationAnalytics(dataPath,percentilePath,outputPath):
    #initilizing dicts for data processing
    DonorZip = {} # Dict1: donor name + zipcode as key, to identify repeat donors
    Donation = {} # Dict2: cmteID + zipcode + Year as key, to record donation list for repeat donors
    
    #read percentile value assigned in the percentilePath
    percentileFile = open(percentilePath, 'r')
    percentile = int(percentileFile.readline().rstrip())
    
    #open the output file
    outputFile = open(outputPath, 'w+')
    
    #load input data file and process data
    inputFile = open(dataPath, 'r')
    tracker = 0
    for line in inputFile:
        tracker = tracker + 1
        print("reading transaction_" + str(tracker))
        inputData = line.split('|')      #separate the line data by '|'
        if len(inputData) != 21:
            continue                     #if length is not meeting FCE format, ignore the line and continue
        cmteID = inputData[0]
        name = inputData[7]
        zipcode = inputData[10]
        tranDT = inputData[13]
        tranAMT = inputData[14]
        otherID = inputData[15]
        # validate the data format and value, skip if incorrect
        if(check_otherID(otherID)==False or check_cmteID(cmteID)==False or check_tranAMT(tranAMT)==False 
           or check_name(name)==False or check_zipCode(zipcode)==False or check_tranDate(tranDT)==False):
            continue
        tranAMT = float(tranAMT)
        DonorZipID = name + "|" + zipcode[:5]
        DonationID = cmteID + "|" + zipcode[:5] + "|" + tranDT[-4:]
        
        if DonorZipID in DonorZip and dateCompare(DonorZip.get(DonorZipID),tranDT):  #repeat donor in a later year is considered
            if DonationID in Donation:
                List = Donation.get(DonationID)
                List.add(tranAMT)
                Donation.update({DonationID:List})
            else:
                newList = SortedList()
                newList.add(tranAMT)
                Donation.update({DonationID:newList})
            # calculate the percentile, total amount, and total # of transactions from repeat donors
            outputPer = calcPercentile(percentile, Donation.get(DonationID))
            outputAmt = dataFormat(sum(Donation.get(DonationID)))
            outputTran = len(Donation.get(DonationID))
            output = DonationID + "|" + str(outputPer) + "|" + str(outputAmt) + "|" + str(outputTran)
            outputFile.write(output + "\n")
        else:
            DonorZip.update({DonorZipID:tranDT})  #update the donorzip dic with new DonorZipID or an earlier tranDT
        
    inputFile.close()
    outputFile.close()
    print("\ndata process complete")

# function to calculate the percentile for a given sorted list
def calcPercentile(percentile, sortedList):
    index = math.ceil(float(percentile)/100*float(len(sortedList)))-1  #nearest rank method for percentile calculation; -1 since list incex is 0-based
    index = int(index)
    value = round(sortedList[index])
    return value

# fucntion to compare date, return true if date2 is later than date1
def dateCompare(date1, date2):
    date1 = datetime.strptime(date1, '%m%d%Y')
    date2 = datetime.strptime(date2, '%m%d%Y')
    if date1 < date2:
        return True
    else:
        return False
# function to format data: input is float
def dataFormat(data):
    if data-round(data) == 0:
        return int(data)
    else:
        return float(data)
    
    
# main function: validate the shell running command
# call the DonationAnalytics function if shell input corret, or return error message
def main():
    try:
        script,dataPath,percentilePath,outputPath = sys.argv 
    except IndexError:
        print ("Shell error: script/input/output path not correct")
    try:
        inputcheck = open(dataPath, 'r')
        inputcheck.close()
    except IOError:
        print ("Shell error: The main Input file doesn't exist")
        sys.exit()
    try:
        percentilecheck = open(percentilePath,'r')
        percentilecheck.close()
    except IOError:
        print ("Shell error: The Percentile input file doesn't exist")
        sys.exit()
    try:
        outputcheck = open(outputPath,'w')
        outputcheck.close()
    except IOError:
        print ("Shell error: The Output file doesn't exist")
        sys.exit()
    #print ("script/input/output path correct")    
    DonationAnalytics(dataPath,percentilePath,outputPath)

'''
# non-shell main function for local test
def main():
    dataPath = "input\itcont.txt"
    percentilePath = "input\percentile.txt"
    outputPath = "output\repeat_donors.txt"
    DonationAnalytics(dataPath,percentilePath,outputPath)  

'''
if __name__ == "__main__":
	main()
