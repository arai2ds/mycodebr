#!/usr/bin/python3

""" Author Anand Rai : sample flask script """

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/admin") # when you goto the ROOT of your server.... do the following
def hello_admin():
    return "Hello admin !"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello {} Guest ".



if __name__=="__main__":
    app.run(port=5006) # run on port 5006

    
