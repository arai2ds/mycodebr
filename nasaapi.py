#!/usr/bin/python3
""" author: anand rai || learning about nasa APIs and dev keys """

import requests
from pprint import pprint as pp

MYAPI = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key="

def keyharvester():
    with open("/home/student/nasa.key","r") as keyfile:
        mykey = keyfile.read()
        mykey = mykey.rstrip('\n')
      #  print(mykey)
        return mykey

def main():
    # harvest our key from /home/student/nasa.key
      nasakey = keyharvester()
      

    # append our key to MYAPI
    # call the API
      resp = requests.get(MYAPI + nasakey)

      #print(resp)
      asteroidz = resp.json()
      #print(asteroidz)

    # parse json #pp(asteroidz["near_earth_objects"])
      for bigrock in asteroidz["near_earth_objects"]:
          #print(bigrock["is_potentially_hazardous_asteroid"])
          if bigrock["is_potentially_hazardous_asteroid"]:
              print("Name -",bigrocki["name"]))
          else:
              #print('not found')
              pass
    # decode json - loop across "neasr_earth_objects" to reveal asteriods
    # only display those that may pose a danger to Zach  having a good weekend
    # 





if __name__ == "__main__":
    main()


