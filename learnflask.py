#!/usr/bin/python3

""" Author Anand Rai : sample flask script """

from flask import Flask
app = Flask(__name__)

@app.route("/") # when you goto the ROOT of your server.... do the following
def endoftheday():
    return "class is nearing the end of wednesday" # Return this if you goto ROOT



if __name__=="__main__":
    app.run(port=5006) # run on port 5006

    
