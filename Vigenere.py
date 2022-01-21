from cs50 import get_string
from sys import argv
import sys

plainText = input ("Enter plaintext to cypher:")
plainText_2= []
cypherKeyword = 0
cypherText = ""
alphaIndex= []
alphaPlainText = []


if len(argv) !=2:
    exit

def cypherKeywordConverted ():
    i = 0
    cypherKeyword = sys.argv[1].lower ()
    for c in cypherKeyword:
        alphaIndex.append (ord(c) - 97)
        i = i + 1
    return

def cypherMessage ():
    i = 0
    cypherText = ""
    for c in plainText:
        if not (plainText[i].isalpha()):
            cypherText += (plainText[i])

        if (plainText[i].isupper()):
           alphaPlainText.append (ord(c) - 65)
           cypherText += (chr (((alphaPlainText[i] + alphaIndex [i % (len (alphaIndex))]) %26 ) + 65))

        if (plainText[i].islower()):
           alphaPlainText.append (ord(c) - 97)
           cypherText+= (chr(((alphaPlainText[i] + alphaIndex [i % (len (alphaIndex))]) %26) + 97))

        print("ciphertext:",cypherText)
        i = i + 1


cypherKeywordConverted()
cypherMessage()
