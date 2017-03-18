#!/usr/bin/env python3

#################################################
#
# Name : Nasser Binshabeeb
# 
#
# Project Info : Python
#
#
#################################################

import sys
import re
from urllib.request import urlopen



def get_url(myFile):
    """
    Counts the occurences of the errors in a dictionary and prints the top 25 most common errors
    Args:
        myFile : a url string
    Return:
        None

    """
    record = {}
    lineList = []
    counter = 0
    

    #check regular expression
    with urlopen(myFile) as theFile:
        for S in theFile:
            dLine = re.search('(/(\w+))+(.?)(\w+)' ,S.decode("UTF-8"))
            if dLine is not None:
                dString = dLine.group()
            #print(dString)
            if not record.__contains__(dString):
                record[dString] = 1
            else:
                record[dString] += 1
        for item in sorted(record, key=record.get,reverse=True):
            print("Count : ", record[item],"Page : ", item)
            counter += 1
            if counter == 24:
                break



def help():
    """
    Help function:
    Args: None
    Return: None
    """

    print("Help function")
    print("bash Usage: ./nasser_binshabeeb.py <url>")

    print("python3 Usage: import nasser_binshabeeb ")
    print("then call nasser_binshabeeb.main()")
    exit(1)



#Main Function
def main():
    """
    Main function
    """

    url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test"
    #url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.full"
    if  len(sys.argv) >1 and len(sys.argv[1]) :
        url = sys.argv[1]
    
    get_url(url)



if __name__ == "__main__":
    # Call Main
    main()

    exit(0)



#exit(0)

