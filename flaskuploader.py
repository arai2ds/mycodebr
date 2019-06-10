# -*- coding: utf-8 -*-
#!/usr/bin/python3
import re
import json
import smtplib
from email.message import EmailMessage
# this works if you "python3 - m pip install flask"
from flask import Flask, render_template,request,redirect,url_for,send_file
from werkzeug import secure_filename
#import pandas as pd
#import numpy as np
import graphin


app = Flask(__name__)

@app.route("/upload")
def upload_file():
    return render_template("uploader.html")

@app.route("/uploader", methods = ["POST"])
def uploader():
    if request.method == "POST": # if we get a post
        mysteryfile = request.files["file"] # pull off the file attachment on the post
        mysteryfile.save(secure_filename(mysteryfile.filename)) # save the file
        if "cap" in mysteryfile.filename:
            return redirect(url_for("sip", filetoparse=mysteryfile.filename))
        elif "xlsx" in mysteryfile.filename:
            return redirect(url_for("excel", filetoparse=mysteryfile.filename))
        else:
            return "That format is not supported .Please check back soon ." + mysteryfile.filename
@app.route("/excel/<filetoparse>")
def excel(filetoparse):
    return send_file(graphin.pygraph(filetoparse), mimetype='image/png')
@app.route("/sip/<filetoparse>")
def sip(filetoparse):
        sipjson = []
        with open(filetoparse) as capture:
            for line in capture:
                mtchobj = re.search(r"sip:\+(\d+)@\[(.*)\]:?(\d+)",line)
                if mtchobj:
                    tinylist = []
                    tinylist.append(mtchobj.group())
                    tinylist.append(mtchobj.group(1))
                    tinylist.append(mtchobj.group(2))
                    tinylist.append(mtchobj.group(3))
                    sipjson.append(tinylist)
            return json.dumps(sipjson)
@app.route("/emailsender")
def emailsender():
    msg = EmailMessage()
    msg['Subject'] = "this is my subject line"
    msg['From'] = "pythonstudent01@mail.com"
    msg['To'] = "rzfeeserspam@gmail.com"
    msg.preamble = "Hey you just got a message from Zach Feeser"

    with open("/home/student/emailpassword.txt") as emailpass:
#        myemailpass = emailpass.read().rstrip().rstrip("\n")
         myemailpass = emailpass.read().rstrip('\n')
    mail = smtplib.SMTP("smtp.mail.com",587)
    mail.starttls()
    mail.login("pythonstudent01@mail.com",myemailpass)
    mail.sendmail("pythonstudent01@mail.com","rzfeeserspam@gmail.com",msg.as_string())
    mail.quit()
    return "Spammity spamcakes sent "



if __name__ == "__main__":
    app.run(port = 5006)
