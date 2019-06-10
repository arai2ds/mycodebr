#!/usr/bin/python3

import json,time,sqlite3,requests

def walmartlookup(walmarturl,mykey,upckey):
    try:
        walmarturlobj = requests.get(walmarturl + mykey +upckey)
        return walmarturlobj.json()
    except:
        return False

def trackmeplease(tracktime,trackprice):
    conn = sqlite3.connect('price.db')
    try:
        conn.execute("""Create tble price
        (time varachar2 primary key not null,
        price real not null);""")
    except:
       pass
    conn.execute("Insert into price(time,price) values(?,?)",(tracktime,trackprice))
    conn.commit()
    cursor = conn.execute("Select time,price from price")
    for row in cursor:
        print("TIME = ",row[0])
        print("PRICE = ",row[1])
    print("DATABASE OPERATION COMPLETE")
    conn.close()

def main():
    wurl = 'http://api.walmartlabs.com/v1/items?'
    wkey = '5mnbr76b2kshnsw2ex2vx6n8'
    wkey = 'apikey=' + wkey

    #wupc = "190198511270"# apple watch 
    wupc = "035000521019"# tooth paste

    wupc = "&upc=" + wupc
    print("Walmart query url is: " ,wurl,wkey,wupc,sep="")
  
    decodedwalmart = walmartlookup(wurl,wkey,wupc)

    if decodedwalmart:
      print("\nWalmart Price on " ,time.ctime(),":$",str(decodedwalmart['items'][0]['salePrice']))
      #if decodedwalmart.get(['items'][0]['msrp']):
       #  print("\nMSRP on  " ,time.ctime(),":$",str(decodedwalmart['items'][0]['msrp']))
      trackmeplease(time.ctime(),decodedwalmart['items'][0]['salePrice'])
    else:

      print("Something went wrong with the API lookup")

if __name__== '__main__':
    main()








