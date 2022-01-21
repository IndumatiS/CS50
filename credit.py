from cs50 import get_int
import numpy as np

CC_number = 0
CC_number_multiplied = []
#David CC number:4003600000000014

CC_number= get_int("Enter Credit Card Number:")
print ("You Entered :", CC_number, end = "")

while not (isinstance (CC_number, int)):
    CC_number = get_int("Enter Credit Card Number:")
print()

CC_number = str(CC_number)
CC_number_array = []

for digit in CC_number:
    CC_number_array.append (int(digit)) #convert input CC number to list because I don't know how to directly covert the number to array
CC_number_array = np.asarray(CC_number_array)

#To check CC_number validity
#Make a temporary array and start with this
temp_array = CC_number_array
temp_array_multiplied = 0

for i in range (len(temp_array)-2, -1,-2): #gives me the second to last element of the array
        if temp_array [i] >= 5:
              temp_array_multiplied = temp_array_multiplied + ((temp_array [i] * 2) % 10) #multiplies and sums
              temp_array_multiplied = temp_array_multiplied + 1  #adds extra one
        else:
            temp_array_multiplied = temp_array_multiplied + ((temp_array [i]) * 2)

for i in range (len(temp_array)-1, -1,-2):
    temp_array_multiplied = temp_array_multiplied + temp_array [i]


#check the validity of credit card and return the type

if temp_array_multiplied % 10 == 0:
    if (len (CC_number_array) == 13 or 16):
        if (CC_number_array[0] == 4):
            print ("VISA")
    if (len (CC_number_array) == 15):
        if (CC_number_array [0] == 3 and CC_number_array [1] == 4 or CC_number_array [1] == 7):
            print ("AMEX")
    if (len (CC_number_array) == 16):
        if ((CC_number_array [0] == 5 and CC_number_array[1] == 1 or 2 or 3 or 4 or 5)):
            print ("MASTERCARD")
else:
    print ("INVALID")
