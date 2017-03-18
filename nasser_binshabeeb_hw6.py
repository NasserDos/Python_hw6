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
    Gets the file from the url
    """
    record = {}
    lineList = []

    with urlopen(myFile) as theFile:
        for S in theFile:
            dLine = re.search('/.*' ,S.decode("UTF-8"))
            print(dLine.group())
            if record.get(dLine.group()) is None:
                record[dLine.group()] = 1
            else:
                record[dLine.group()] = record[dLine.group()] + 1
        print(max(record),record[max(record)])
        
         




def help():
    """
    Help function:
    Args: None
    Return: None
    """

    print("Help function")
    exit(1)










#Main Function
def main():
    """
    Main function
    """
    url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test"
    get_url(url)



if __name__ == "__main__":
    # Call Main
    main()

    exit(0)



#exit(0)

