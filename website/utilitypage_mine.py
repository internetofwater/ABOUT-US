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

from tkinter import messagebox
import functools

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import lxml.html as lh

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('Homepage.html')

@app.route('/utilityfinder')
def utiltyfinder():
    return render_template('utilityfinder.html')


@app.route('/search', methods=["GET", "POST"]) #POST requests that a web server accepts the data enclosed in the body of the request message
def search():
    if request.method == "POST":       #GET- retrieves information from the server
        address = request.form["address"]
        zipcode = request.form["zipcode"]
        state = request.form["state"]
        latitude, longitude, granularity = geocode(address, zipcode, state)
        if latitude == 0 and longitude ==0:
            return render_template("error_page.html", ad=address, zipc=zipcode, st=state)
        utility = correct_utility_function(latitude, longitude)
        (utility3, link2) = utility
        print(utility3)
        print(link2)
        #if geocode_zip.has_been_called = True
            #tkinter.messagebox.showinfo(title="Warning", message="Address was unreadable so displaying utilities based on zipcode")
            #return render_template("search.html", zip_lat= zip_latitude, zip_long= zip_longitude, ad= address, zipc=zipcode, st=state)
        return render_template("search.html", lat=latitude, lon=longitude, gran= granularity, ad=address, zipc=zipcode, st=state, uname=utility3, linkname=link2)
    else:
        return render_template("interactive_map.html")


locator = Nominatim(user_agent="otherGeocoder")

def geocode (address, zipcode, state):  #geocoder address to coordinates
    lista = []
    lista.append(address)
    lista.append(zipcode)
    lista.append(state)
    addressfull = ', '.join(lista)
    try: 
        location = locator.geocode(addressfull)
        if location is None:
            return geocode_zip (zipcode)
        else:     
            return location.latitude, location.longitude, "address_level"
    except:
        return 0,0, "failure" 


def geocode_zip (halfaddress):
    listb = []
    listb.append(zipcode)
    listb.append(state)
    halfaddress = ', '.join(listb)
    try:
        zip_middle = locator.geocode(halfaddress)
        return zip_middle.latitude, zip_middle.longitude, "zipcode_level"
    except:
        return 0,0, "failure"
'''
def display_message(geocode_zip):
    if geocode_zip.has_been_called = True:
        tkinter.messagebox.showinfo(title="Warning", message="Address was unreadable so displaying utilities based on zipcode")
        #return render_template("search.html", zip_lat= zip_latitude, zip_long= zip_longitude, ad= address, zipc=zipcode, st=state)
'''


response = requests.get('https://www.ncwater.org/Drought_Monitoring/statusReport.php/')  #conservation status info webscraping
stored_contents = lh.fromstring(response.content)
table_elements = stored_contents.xpath('//tr')
col=[]
i=0
for t in table_elements[0]:
    i+=1
    name=t.text_content()
    col.append((name,[]))
for j in range(1,len(table_elements)):
    T=table_elements[j]
    if len(T)!=7:
            break
    i=0
    for t in T.iterchildren():
        data=t.text_content() 
        if i>0:
            try:
                data=int(data)
            except:
                pass
        col[i][1].append(data)
        i+=1
Dict ={title:column for (title,column) in col}
Newest_Updates =pd.DataFrame(Dict)
Newest_Updates = Newest_Updates[~Newest_Updates['PWSID'].astype(str).str.startswith('PWSID')]


html_page = urlopen("https://www.ncwater.org/Drought_Monitoring/statusReport.php") #grab the links in a usable format
soup = BeautifulSoup(html_page, features="lxml")
ev_list = []
for tag in soup.find_all('tr'):
    Answer = tag.find_all('a')
    if Answer != []:
        ev_list.append(Answer[0]['href'])
    else:
        pass
Link_Dataframe = pd.DataFrame(ev_list)
Link_Dataframe.columns = ["External Links"]
Bigger_Dataframe = pd.merge(Newest_Updates, Link_Dataframe, left_index=True, right_index=True)
Bigger_Dataframe

StateWide = gpd.read_file(r"/Users/benwilliams/Documents/Data+/ABOUT-US/Boundaries/NC_statewide_CWS_areas.gpkg") #make large usable dataframe with both names and links
StateWide.geometry= StateWide.geometry.to_crs(epsg="4326")
Combined_Utility = pd.merge(Bigger_Dataframe, StateWide, 'right', on="PWSID")

polygons = Combined_Utility['geometry'] #return utility name and link
utility1 = Combined_Utility['Water System']
utility2 = Combined_Utility['SystemName']
link = Combined_Utility['External Links']

def missing_utility(i):
    UtilityCloser = utility2.replace('_', ' ')   #make the utility readable
    UtilityCloser = UtilityCloser.replace('\'', '')
    UtilityCloser = UtilityCloser.replace('\"', '')
    UtilityList = list(UtilityCloser.split(" "))
    for k in range(len(UtilityList)):
        UtilityList[k] = UtilityList[k].replace(' ', '')
        if 'Town' == UtilityList[0] or 'City' == UtilityList[0]:
            return(UtilityCloser, "No link provided by utility company")
        elif 'Town of' in UtilityCloser or 'Town Of' in UtilityCloser or 'City Of' in UtilityCloser or 'City of' in UtilityCloser or 'Village of' in UtilityCloser or 'Village Of' in UtilityCloser:
                if len(UtilityList) == 3:
                    myorder = [1, 2, 0]
                    UtilityTown = [UtilityList[i] for i in myorder]
                    return(' '.join(UtilityTown[0 : 3]), "No link provided by utility company")
                elif len(UtilityList) == 4:
                    myorder = [2, 3, 0, 1]
                    UtilityTown = [UtilityList[i] for i in myorder]
                    return(' '.join(UtilityTown[0 :5]), "No link provided by utility company")
                else:
                    if '' in UtilityList[2]:
                        myorder = [3, 4, 0, 1]
                        UtilityTown = [UtilityList[i] for i in myorder]
                        return(' '.join(UtilityTown[0 :5]), "No link provided by utility company")
                    else:
                        myorder = [1, 2, 0, 3, 4]
                        UtilityTown = [UtilityList[i] for i in myorder]
                        return(' '.join(UtilityTown[0 :6]), "No link provided by utility company")
        else: 
            if ',' in utility.iloc[i]:
                UtilityCloser = utility.iloc[i].replace(',', '')
                UtilityList = list(UtilityCloser.split(" "))
                if len(UtilityList) == 3:
                    myorder = [1, 2, 0]
                    UtilityTown = [UtilityList[i] for i in myorder]
                    return(' '.join(UtilityTown[0 : 3]), "No link provided by utility company")
                elif len(UtilityList) == 4:
                    myorder = [2, 3, 0, 1]
                    UtilityTown = [UtilityList[i] for i in myorder]
                    return(' '.join(UtilityTown[0 :5]), "No link provided by utility company")
                else:
                    myorder = [3, 4, 0, 1, 2]
                    UtilityTown = [UtilityList[i] for i in myorder]
                    return(' '.join(UtilityTown[0 :6]), "No link provided by utility company")
            else:
                return(utility2.iloc[i], "No link provided by utility company")

def correct_utility_function(latitude, longitude):
    coordinate = Point(longitude, latitude)
    for i in range(len(Combined_Utility)):
        if polygons.iloc[i].contains(coordinate):
            if pd.isnull(utility1.iloc[i]):
                return missing_utility(i)
            else:
                return(utility1.iloc[i], link.iloc[i])

    return None, None

