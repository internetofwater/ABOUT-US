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

def geocode(address, zip_code, state):
    latitude = 1
    longitude = 1
    return latitude, longitude

@app.route('/search', methods=["GET", "POST"])
def search():
        if request.method == "POST":
            address = request.form["address"]
            zipcode = request.form["zipcode"]
            state = request.form["state"]
            latitude, longitude = geocode(address, zipcode, state)
            
            return render_template("search.html", lat=latitude, lon=longitude)