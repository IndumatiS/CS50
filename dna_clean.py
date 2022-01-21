import pandas as pd
import re
import csv
from sys import argv
import sys


#create a global variables

DNA_seq_filename = ""
STR_csv_filename = ""

DNA_sequence = "" #contains the dna sequence that has been read from the file
STR_dataframe = pd.DataFrame()

STR_count_dict = dict()
person_found = "invalid"


#funciton to read DNA_String
def readDNASeq ():
    global DNA_seq_filename
    global DNA_sequence
    #print ("Reading DNA Sequence into a string variable")
    DNA_seq_filename = sys.argv[2]
    DNA_seq_file = open (DNA_seq_filename, "r")
    for c in DNA_seq_file:
        DNA_sequence = c
    DNA_seq_file.close
    return


#function to read csv file and build dataframe
def readSTRcsv ():
    global STR_csv_filename
    global STR_dataframe
    #print ("Reading the STR CSV file into a dataframe")
    STR_csv_filename = sys.argv[1]
    STR_dataframe = pd.read_csv(STR_csv_filename)
    #print(type(STR_dataframe), ":", STR_dataframe.shape)
    #print("Testing Looping through dataframe")
    #for row in STR_dataframe.iterrows():
    #    print(str(row))
    #print(type(STR_dataframe), ":", STR_dataframe.shape)
    return

#function to build str dictionary from dataframe header
def buildSTRdict ():
    global STR_dataframe
    global STR_count_dict
    #print("Building STR Count Dictionary")
    #print(type(STR_dataframe), ":", STR_dataframe.shape)
    header_list = STR_dataframe.columns.to_numpy().tolist()
    #print(str(header_list))
    #firstone is name column, pop it
    header_list.pop(0)
    #print("Header List:", str(header_list))
    #loop through the list and build the dict with a default value of 0
    for item in header_list:
        STR_count_dict[item] = 0
    #print("STR Count Dictionary:", str(STR_count_dict))
    return


#function to get count for one str
def getSTRCountInDNASeq (STR_string):
    global DNA_sequence
    global STR_count_dict
    len_STR_string = len(STR_string)
    str_count = 0 #working count
    str_max_count = 0 #max count
    position = 0 #keeps track of the current position from which, to the end of DNA Sequence we have to find STR
    #print("Finding the Count for STR:", STR_string)
    # get the first match of the STR
    matches =  re.search(STR_string , DNA_sequence)
    position = position + int (str(matches.start()))
    for i in range (position, len(DNA_sequence), +1):
        if (DNA_sequence[position:(position + len_STR_string)] == STR_string and matches):
            str_count = str_count + 1
            position = (position + len_STR_string)
        else:
            position = position + len_STR_string
            if (str_count > str_max_count):
                str_max_count = str_count
            # Set things up for the next match,
            #   make count 0
            #   call search again in the substring of the DNA sequence
            #   Update position if found else break from loop
            str_count = 0
            # get the next match of the STR from the current position to the end
            matches =  re.search (STR_string , DNA_sequence[position:len(DNA_sequence)])
            if matches:
                # set position to the next match of the STR from the current position to the end
                position = position + int (str(matches.start()))
            else:
                break # no more matches, break out of the loop

    #set max count to the dictionary object
    STR_count_dict[STR_string] = str_max_count
    #print ("Count Found for ", STR_string, " : ", STR_count_dict)
    return


#function to match the str dictionary counts to the dataframe
def findPersonWithSTRCounts():
    global STR_count_dict
    global STR_dataframe
    global person_found

    #num_str_to_match = len(STR_count_dict)
    for index, row in STR_dataframe.iterrows():
        #print("matching for :", row['name'])
        #assume we are going to match
        person_found = row["name"]
        for key in STR_count_dict:
                #print("Key:",key , " Row Value:",row[key] ,  "  Counted:", STR_count_dict[key] )
                if not row[key] == STR_count_dict[key]:
                  person_found = "invalid"
                  break
        #check if assumption person matched is true and break
        if not person_found == "invalid":
            break
    return

#main code to call the functions
readDNASeq()
readSTRcsv()
buildSTRdict()
#print(str(STR_dataframe))
for key in STR_count_dict:
    getSTRCountInDNASeq (key)
#print()
#print(str(STR_count_dict))
#print()
findPersonWithSTRCounts()
print(person_found)


