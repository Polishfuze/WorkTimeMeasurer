#This program was developed by PolishFuze (PolishFuze@gmail.com)
#It is intended to serve as a command line timer for measuring work time and to save it to a *.csv file
#Replace the Workfile with the location of the file that you want to use for timekeeping.
#This programme is suited for my own personal needs so it automatically rounds up from half an hour so 6.5h of work are counted as 7h
#I do not take anu responsibility for this programme or any loss of data, incorrect data, and programme failiures and instabilities it may create
#Run this at your own risk
#Preferably after glancing at the code below
#
#

Workfile = "C:/Users/micha/OneDrive/Dokumenty/WorkSheet.csv"

import time
import csv
import datetime

RowsThatWereAlreadyHere = []
      
def timediff(BeginTime, EndTime):
    diff = 0
    if(BeginTime[2] != EndTime[2]):
        diff = 24 - BeginTime[3] + EndTime[3]
    else:
        diff = EndTime[3] - BeginTime[3]
    if(BeginTime[4]-EndTime[4] >= 16):
        diff += 1
    return diff

def FormatTheFile():
    with open(Workfile ,'w', newline='' ) as f:
        writer = csv.writer(f, delimiter=',')
        CleanRow = (['LP', 'Data', 'Start', 'Koniec', 'W sumie godzin'])
        writer.writerow(CleanRow)
        


text = input("Please type begin to start the counter, type help to get help ");

while text.lower() != "begin":
    if text.lower() == "help":
        print("This is the help, type help to get this prompt,\nType format to format (or create if it wasn't created already) your workfile in an earlier specified location\nWARNING THIS WILL ERASE ALL DATA FROM THE FILE!,\nType Workdir to change the work directory and or filename,\nType type begin to begin the counter,\nType stop to stop the counter\n")
        text = input("Now please type begin to start the counter ")
    elif text.lower() == "format":
        if(input("This will erase all data from your save file, if you wish to continue, type continue ").lower() == "continue"): 
            FormatTheFile()
        text = input("Now please type begin to start the counter ")
    elif text.lower() == "workdir":
        Workfile = input("Input your new file path (e.g. C:/user/documents/Worksheet.csv): ")
        print("Your new path file is: " + Workfile)
        text = input("Now please type begin to start the counter ")
    elif text.lower() == "abort":
        exit()
    elif text.lower() != "begin ":
        print("Unknown command ")
        text = input("Now please type begin to start the counter ")
        
BeginTimeStruct = time.localtime()

 
while text.lower() != "stop":
    if text.lower() == "help":
        print("This is the help, type help to get this prompt,\nType format to format (or create if it wasn't created already) your workfile in an earlier specified location\nWARNING THIS WILL ERASE ALL DATA FROM THE FILE!,\nType Workdir to change the work directory and or filename,\nType type begin to begin the counter,\nType stop to stop the counter\n")
        text = input("Now please type stop to stop the counter ")
    elif text.lower() == "format":
        if(input("This will erase all data from your save file, if you wish to continue, type continue ").lower() == "continue"): 
            FormatTheFile()
        text = input("Now please type stop to start the counter ")
    elif text.lower() == "workdir":
        Workfile = input("Input your new file path (e.g. C:/user/documents/Worksheet.csv): ")
        print("Your new path file is: " + Workfile)
        text = input("Now please type stop to start the counter ")
    elif text.lower() == "begin":
        text = input("Now please type stop to stop the counter ")
    elif text.lower() == "abort":
        exit()
    elif text.lower() != "stop":
        print("Unknown command")
        text = input("Now please type stop to stop the counter ")


EndTimeStruct = time.localtime()
      
diffotime = timediff(BeginTimeStruct, EndTimeStruct)



with open(Workfile,'r', newline='' ) as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        RowsThatWereAlreadyHere.append(row)
if len(RowsThatWereAlreadyHere) <= 1:
    FormatTheFile()

Appendition = [str(len(RowsThatWereAlreadyHere)),(str(BeginTimeStruct[2])+'/'+str(BeginTimeStruct[1])+'/'+str(BeginTimeStruct[0])), str(BeginTimeStruct[3])+':'+str(BeginTimeStruct[4]), str(EndTimeStruct[3])+':'+str(EndTimeStruct[4]), diffotime]
RowsThatWereAlreadyHere.append(Appendition)

with open(Workfile ,'w', newline='' ) as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(RowsThatWereAlreadyHere)

print(RowsThatWereAlreadyHere)