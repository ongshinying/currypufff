from flask import Flask,render_template,request
import google.generativeai as genai
import os
import numpy as np
import textblob

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))
 
@app.route("/subscription",methods=["GET","POST"])
def subscription():
    return(render_template("subscription.html"))

@app.route("/thankyou",methods=["GET","POST"])
def thankyou():
    return(render_template("thankyou.html",r=r))

if __name__ == "__main__":
    app.run()
