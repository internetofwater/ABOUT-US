#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:38:45 2020

@author: benwilliams
"""

from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('Homepage.html')

@app.route('/utilityfinder')
def utiltyfinder():
    return render_template('utilityfinder.html')



@app.route('/search', methods=["GET", "POST"])
def search():
        if request.method == "POST":
            address = request.form["address"]
            zipcode = request.form["zipcode"]
            state = request.form["state"]
            latitude, longitude = geocode(address, zipcode, state)


            return render_template("search.html", lat=latitude, lon=longitude)


locator = Nominatim(user_agent="otherGeocoder")

def geocode (address, zipcode, state):
    try: 
        location = locator.geocode(address, zipcode, state)
        if location is None:
            return 0, 0
        else:     
            return location.latitude, location.longitude
    except:
        return "Address Unclear", "Consider Rewriting"

                   