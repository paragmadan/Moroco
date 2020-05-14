#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import datetime
import requests
import json
import os
import datetime


def dump_to_csv(output,st):                                                       #Output is the data returned in json format
    #flnm=raw_input("Enter file name you want to dump data in")
    os.chdir("C:\Users\RZFW9607\Desktop\Data" )
    flnm=st
    # print(type(output["data"][0]))
    # fromdate=fromdate.replace('-','')
    dt=datetime.datetime.now()                                                 #Get the time in order to attach timestamp to the file
    timestmp=dt.strftime("%d%m%Y_%H%M%S")
    #print(type(timestmp))
    #print(timestmp)
    filename = '%s_%s.csv' %(flnm,timestmp)
    #print(type(filename))
    print('Results Generated at:'+os.getcwd()+"/"+filename)
    csvfile = csv.writer(open(filename, 'wb+'))
    #print output

    # csvfile.writerow(["amount","creationDate","receiverMsisdn","senderMsisdn","transactionType","transactionDate","omTransactionId","addonTransactionId","errorCode","errorDescription","channelType","initialOmTransactionId","initialAddonTransactionId","initialTransactionDate","transactionStatus","hpsstransactionId"])
    if(len(output['data'])==0):
        print("No data Found")
    else:
        t = output['data'][0]                                           #To get the Headers(Headings of the Column)
        csvfile.writerow([m.upper() for m in t.keys()])

        # print(response.content)

        for i in output['data']:

            # csvfile.writerow([i["amount"],i["creationDate"],i["receiverMsisdn"],i["senderMsisdn"],i["transactionType"],i["transactionDate"],i["omTransactionId"],i["addonTransactionId"],i["errorCode"],i["errorDescription"],i["channelType"],i["initialOmTransactionId"],i["initialAddonTransactionId"],i["initialTransactionDate"],i["transactionStatus"],i["hpsstransactionId"]])
            #  csvfile.close()

            csvfile.writerow([m for m in i.values()])                           #Write all entries to the file



