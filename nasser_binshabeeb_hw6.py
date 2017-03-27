#!/usr/bin/env python3

#################################################
#
# Name : Nasser Binshabeeb
# 
#
# Project Info : Script to find the top 25 most common error pages
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
    record = {} #Will store the matches
    counter = 0 #Used for numbering top 25
    try:
        with urlopen(myFile) as theFile:
            print("Decoding and filtering through the file...")  
            for byteLine in theFile:
                #confirm the line contains the word error
                confirmError1 = re.search(r'(?=error)',byteLine.decode("UTF-8"))
                if confirmError1 is not None :
# / followed by a length 3~6 word, (a seperator or none)(words)once or more
                    dLine = re.search(r"/(\w{3,6})((\W?)(\w+))+" ,byteLine.decode("UTF-8"))
            

                    #Another failed attempt
                    #dLine = re.search(r"((/\w{6})|(/\w{3,4}/\w{3,7}(/(\W?\w+)+)))" ,byteLine.decode("UTF-8"))
                
                    #dictionary entries
                    if dLine is not None:
                        dString = dLine.group(0)
                        if dString not in record:
                            record[dString] = 1
                        else:
                            record[dString] += 1
            print("Decoding complete")
            print("Sorting dictionary")
            #These three caused problems
            record['/icarus.cs.weber.edu'] = 0
            record['/unix-directory returned invalid result code']= 0
            record['/var/www/html']=0
            
            #sort then print top 25
            print("*** Top 25 page errors ***")
            for item in sorted(record, key=record.get,reverse=True):
                print("Count :", record[item],"Page :", item)
                counter += 1
                if counter == 25:
                    break
    except ValueError:
        print("Exception handled : The url entered did not work")
        help()



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
    Calls other functions and checks for arguments, makes things more clear
    """


    if  len(sys.argv) > 1:
        url = sys.argv[1]
        get_url(url)
    else:
        help()


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)



#exit(0)

