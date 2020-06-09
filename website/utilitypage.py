#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:38:45 2020

@author: benwilliams
"""

from flask import Flask, request
from flask import render_template
from geopy.geocoders import Nominatim
import pandas as pd
import os
import geopandas as gpd
import geopy
from shapely.geometry import Polygon, Point, MultiPolygon
import shapefile
from matplotlib import pyplot as plt
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
            lista = []
            address = request.form["address"]
            zipcode = request.form["zipcode"]
            state = request.form["state"]
            lista.append(address)
            lista.append(zipcode)
            lista.append(state)
            addressfull = ', '.join(lista)
            latitude, longitude = geocode(addressfull)
            utility = find_utility_function(latitude, longitude)

            return render_template("search.html", lat=latitude, lon=longitude, ad=address, zipc=zipcode, st = state, ut=utility)


locator = Nominatim(user_agent="otherGeocoder")

def geocode (addressfull):
    try: 
        location = locator.geocode(addressfull)
        if location is None:
            return 0, 0
        else:     
            return location.latitude, location.longitude
    except:
        return "Address Unclear", "Consider Rewriting"


StateWide = gpd.read_file(r"../Boundaries/NC_statewide_CWS_areas.gpkg")
polygons = StateWide['geometry']
utility = StateWide['SystemName']

def find_utility_function(latitude, longitude):
    coordinate = Point(longitude, latitude)
    for i in range(len(StateWide)):
        if polygons.iloc[i].contains(coordinate):
            return (utility.iloc[i])
