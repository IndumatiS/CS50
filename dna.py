import pandas as pd
import re
import csv
from sys import argv
import sys

DNA_string = ""
strCounts_array = []
str_array = []
numTimesFileRead = 0

DNA_filename = sys.argv[2]
csv_filename = sys.argv[1]
data = pd.read_csv(csv_filename)
STR_string = ""
#print (type (STR_string))

def findSTR_position (DNA_filename,STR_string):
    position = 0
    file = open (DNA_filename, "r")
    for c in file:
        DNA_string = c
    matches =  re.search (STR_string , DNA_string)
    if matches:
        position += int (str(matches.start()))
   # all_matches = re.findall(STR_string, DNA_string)
    #if all_matches:
     #   print("All_matches", all_matches.start())
    return (position)
    file.close()


def matchSTRwithDNA (position):
    str_array = []
    str_count = 0
    str_countMax = 0
    file = open (DNA_filename, "r")
    for c in file:
       DNA_string = c
    for i in range (position, len(DNA_string)):
        if (DNA_string[position:(position+len(STR_string))] == STR_string):
            str_count += 1
            position = (position + len(STR_string))
        else:
            position+=1
            if (str_count > str_countMax):
                str_countMax = str_count
            str_count = 0

    #print ((STR_string))
    return (str_countMax)
    file.close()

#print (len(data.columns))
position = findSTR_position (DNA_filename, STR_string)
matchSTRwithDNA (position)

#Get counts of all STRs
for i in range (1, len(data.columns), +1):
    STR_string = data.columns[i]
    #print (STR_string)
    position = findSTR_position (DNA_filename, STR_string)
    strCounts_array.append(matchSTRwithDNA (position))

#print ("df_dimensions:", data.shape)
#print ("df type", type(data))
#print (strCounts_array)
#print (data.AGATC[0])
#print (data.AATG[0])
#print (len(data.columns))



def str_match():
    if(argv[1] == "databases/small.csv"):
        for i in range (0, 3,+1):
            if ((data.AGATC[i]==(strCounts_array[0])) & (data.AATG [i]==(strCounts_array[1])) & (data.TATC[i]==(strCounts_array[2]))):
               x = data [(data.AGATC==(strCounts_array[0])) & (data.AATG==(strCounts_array[1])) & (data.TATC==(strCounts_array[2]))]
               print (x.iloc[0,0])
               break
            else:
                if (i ==2):
                    print ("No match")
                else:
                    continue
    else:
        for i in range (0, 23,+1):
            if ((data.AGATC[i]==(strCounts_array[0]))
            & (data.TTTTTTCT [i]==(strCounts_array[1]))
            & (data.AATG[i]==(strCounts_array[2]))
            & (data.TCTAG[i]==(strCounts_array[3]))
            & (data.GATA[i]==(strCounts_array[4]))
            & (data.TATC[i]==(strCounts_array[5]))
            & (data.GAAA[i]==(strCounts_array[6]))
            & (data.TCTG[i]==(strCounts_array[7]))):
               x = data [(data.AGATC==(strCounts_array[0]))
               & (data.TTTTTTCT==(strCounts_array[1]))
               & (data.AATG==(strCounts_array[2]))
               & (data.TCTAG==(strCounts_array[3]))
               & (data.GATA==(strCounts_array[4]))
               & (data.TATC==(strCounts_array[5]))
               & (data.GAAA==(strCounts_array[6]))
               & (data.TCTG==(strCounts_array[7]))]
               print (x.iloc[0,0])
               break
            else:
                if (i ==22):
                    print ("No match")
                else:
                    continue

    #x = data [(data.AGATC==(strCounts_array[0])) & (data.AATG==(strCounts_array[1])) & (data.TATC==(strCounts_array[2]))]
    #print (x.iloc[0,0])
    #3print (type (data [(data.AGATC==(strCounts_array[0])) & (data.AATG==(strCounts_array[1])) & (data.TATC==(strCounts_array[2]))]))

str_match()



