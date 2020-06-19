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
            utility = convertUtility(latitude, longitude)

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
StateWide.geometry = StateWide.geometry.to_crs(epsg="4326")
polygons = StateWide['geometry']
utility = StateWide['SystemName']

def find_utility_function(latitude, longitude):   #section coverts coordinates to utility
    coordinate = Point(longitude, latitude)
    for i in range(len(StateWide)):
        if polygons.iloc[i].contains(coordinate):
            return (utility.iloc[i])


def convertUtility(latitude, longitude):
    utilitytemp = find_utility_function(latitude, longitude)
    UtilityCloser = utilitytemp.replace('_', ' ')   #make the utility readable
    UtilityCloser = UtilityCloser.replace('\'', '')
    UtilityCloser = UtilityCloser.replace('\"', '')
    UtilityList = list(UtilityCloser.split(" "))
    for k in range(len(UtilityList)):
        UtilityList[k] = UtilityList[k].replace(' ', '')
        if 'Town' == UtilityList[0] or 'City' == UtilityList[0]:
            return(UtilityCloser)
        else:
            if 'Town of' in UtilityCloser or 'Town Of' in UtilityCloser or 'City Of' in UtilityCloser or 'City of' in UtilityCloser or 'Village of' in UtilityCloser or 'Village Of' in UtilityCloser:
                if len(UtilityList) == 3:
                    myorder = [1, 2, 0]
                    UtilityTown = [UtilityList[i] for i in myorder]
                    return(' '.join(UtilityTown[0 : 3]))
                else:
                    if len(UtilityList) == 4:
                        myorder = [2, 3, 0, 1]
                        UtilityTown = [UtilityList[i] for i in myorder]
                        return(' '.join(UtilityTown[0 :5]))
                    else:
                        if '' in UtilityList[2]:
                            myorder = [3, 4, 0, 1]
                            UtilityTown = [UtilityList[i] for i in myorder]
                            return(' '.join(UtilityTown[0 :5]))
                        else:
                            myorder = [1, 2, 0, 3, 4]
                            UtilityTown = [UtilityList[i] for i in myorder]
                            return(' '.join(UtilityTown[0 :6]))
            else:
                UtilityJoin = list(UtilityCloser.split(" "))
                return(' '.join(UtilityJoin[0 : 6]))
    else:
        if ',' in utility.iloc[i]:
            UtilityCloser = utility.iloc[i].replace(',', '')
            UtilityList = list(UtilityCloser.split(" "))
            if len(UtilityList) == 3:
                myorder = [1, 2, 0]
                UtilityTown = [UtilityList[i] for i in myorder]
                return(i, ' '.join(UtilityTown[0 : 3]))
            elif len(UtilityList) == 4:
                myorder = [2, 3, 0, 1]
                UtilityTown = [UtilityList[i] for i in myorder]
                return(i, ' '.join(UtilityTown[0 :5]))
            else:
                myorder = [3, 4, 0, 1, 2]
                UtilityTown = [UtilityList[i] for i in myorder]
                return(i, ' '.join(UtilityTown[0 :6]))
        else:
            return(i, utility.iloc[i])

