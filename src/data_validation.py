# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 23:17:02 2018

@author: yguo
"""

import datetime

"""
functions to check data validity, according to the predefined limitions.
"""
#CMTE_ID fields shouldn't be empty 
def check_cmteID(cmteID):
    if cmteID:
        return True
    else:
        print ("CMTE_ID empty, skip this transaction")
        return False
#Transaction_AMT fields shouldn't be empty    
def check_tranAMT(tranAMT):
    if tranAMT:
        return True
    else:
        print ("transaction amount empty, skip this transaction")
        return False

#name should not be empty, name should not be digital
def check_name(name):
    if name and name.isdigit() == False:
        return True
    else:
        print("name empty or name is not character, skip this transaction")
        return False

#only consider individual contributions
def check_otherID(otherID):
    if otherID:
        print("not individual donation, skip this transaction")
        return False
    else:
        return True

#zipcode has at least 5 digits and no more than 9 digits
def check_zipCode(zipcode):
    if zipcode == "" or len(zipcode) < 5 or zipcode.isdigit() == False:
        print("zipcode format wrong, skip this transaction")
        return False
    else:
        return True

#only consider individual contributions, where Other_Id is empty       
def check_tranDate(Transaction_DT):
    if len(Transaction_DT)!=8:
        print ("transaction date format not 8-digit, skip this transaction")
        return False
    try:
        date=datetime.datetime.strptime(Transaction_DT, '%m%d%Y')
    #if date is not the format of MMDDYYYY or value is not correct, like MM>12, return false
    except ValueError:
        print ("transaction date invalid: format incorrect, skip this transaction")
        return False 
    else:
        #transaction date shouldn't beyond today's date
        if date>datetime.datetime.today():
            print("transaction date invalid: beyond current date, skip this transaction")
            return False
        else:
            return True
        
