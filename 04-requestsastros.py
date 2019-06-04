#!/usr/bin/python3
""" learning about json from api"""

import requests

MAJORTOM = "http://api.open-notify.org/astros.json"





def main():
    # make request
    resp = requests.get(MAJORTOM)


    # convert string data to JSON
    pyj = resp.json()


    # pparse out JSON we stripped off response
    astrocosmo = pyj.get("people")


    # display  selected data on screen - name of the people in space
    print("CURRENTLY in SPACE:")
    for spaceperson in astrocosmo:
        print(spaceperson["name"])



if __name__=="__main__":
    main()







