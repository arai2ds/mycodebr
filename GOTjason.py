#!/usr/bin/python3
"""Author Anand | Leraning GOTjason.py"""
#pull in jason lib so we can parse out json
import json

def main():
    # open the jasonnow.jason file
    with open("jasonsnow.json","r") as gotdata:
        jonsnow = gotdata.read() # create a string of all the jason
        GOTpy = json.loads(jonsnow) # convert String to pythnic LISTs and DICTs
    print(GOTpy) # display the GOTpy data
    print(GOTpy["url"]) # display values assoc. with URL
    print(GOTpy["titles"][0])# display values assoc with titles
    
    #create aloop to move across aliasses
    for gotalias in GOTpy["aliases"]:
        print(gotalias)

    print(GOTpy["aliases"]) # display values assoc with aliases
    #print (jasonnow["url"])
        #parse the file for character name,alias/titles
    #display the API for ????



if __name__=="__main__":
    main()
