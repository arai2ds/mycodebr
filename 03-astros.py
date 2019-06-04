#!/usr/bin/python3
""" learning about json from api"""

import json
import urllib.request

MAJORTOM = "http://api.open-notify.org/astros.json"





def main():
    # make request
    resp = urllib.request.urlopen(MAJORTOM)
    print(dir(resp))
    # make python striop JSON data FROM the 200 response
    jstring = resp.read()


    # convert string data to JSON
    # print (jstring) # display jstring currently 
    # print(type(jstring)) # what class is jstring from ?
    # print(dir(jstring)) # methods avail to jstring
    pyj = json.loads(jstring.decode('utf-8'))


    # pparse out JSON we stripped off response
    astrocosmo = pyj.get("people")


    # display  selected data on screen - name of the people in space
    print("CURRENTLY in SPACE:")
    for spaceperson in astrocosmo:
        print(spaceperson["name"])



if __name__=="__main__":
    main()







