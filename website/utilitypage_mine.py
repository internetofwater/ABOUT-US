#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:38:45 2020

@author: benwilliams
"""

from flask import Flask, request, send_from_directory, jsonify
from flask import render_template
from geopy.geocoders import Nominatim
import pandas as pd
import os
import geopandas as gpd
import geopy
from shapely.geometry import Polygon, Point, MultiPolygon
import shapefile
from matplotlib import pyplot as plt
from sqlalchemy import create_engine


from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import lxml.html as lh

app = Flask(__name__, static_url_path='')

@app.route('/')
def home_page():
    return render_template('Homepage.html')

@app.route('/utilityfinder')
def utiltyfinder():
    return render_template('utilityfinder.html')


@app.route('/graphpage')
def graphpage():
    #streamDataToPlot, graphTitle = graphThisData()
    return render_template('graphpage.html')  #sdtp=streamDataToPlot, gtt=graphTitle)

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
            utility = correct_utility_function(latitude, longitude)
            (utility3, link2) = utility
            # mockGageData = pd.read_csv(r"/Users/benwilliams/Documents/Data+/nwis_data_mock.csv", header=0, names=['date', 'value', 'data_type', 'nwis_site_no'])
            folder = 'C:\\Users\\wyseg\\'

            mockGageData = pd.read_csv(os.path.join(folder, 'nwis_data_mock.csv'), header=0, names=['date', 'value', 'data_type', 'nwis_site_no'])
        numberToName = pd.read_csv(os.path.join(folder, 'nwis_site_info.csv'))
        inputSite = '02043433'
        df2 = mockGageData[mockGageData['nwis_site_no']== inputSite]
        df3 = df2[['date', 'value']]
        sdtp = df3.to_csv(index=False)
        df4 = numberToName[numberToName['0']== inputSite]
        if df2.data_type[1] == 60:
            dataToPlot = sdtp.replace('value', 'height')
        elif df2.data_type[1] == 65:
            dataToPlot = sdtp.replace('value', 'flow rate')
        else:
            dataToPlot = sdtp.replace('value', 'precipitation')
        gageTitle = df4['1'][0]
        return render_template("search.html", lat=latitude, lon=longitude, ad=address, zipc=zipcode, st=state, uname=utility3, linkname=link2, dtp = dataToPlot, gtt = gageTitle)

@app.route('/nwis_data/<path:site_no>',methods=['GET'])
def send_data(site_no):
    query = """SELECT ts, signal FROM nwis.daily WHERE nwis_site_no = '{}'""".format(site_no)
    data = pd.read_sql_query(query, cnx)# get site_data from sql 
    data['ts'] = data['ts'].apply(lambda x: x.strftime("%Y-%m-%d") )
    # {"dates": [1,2,3,4], "signal": [1,2,3,4]}

    return jsonify(**data.to_dict('split'))

# use these when you need to create/alter tables. DO NOT allow them to be displayed/served on a webpage, or check them into git





@app.route('/node_modules/<path:path>')
def send_js(path):
    return send_from_directory('node_modules', path)

def graphThisData():
    mockGageData = pd.read_csv(r"/Users/benwilliams/Documents/Data+/nwis_data_mock.csv", header=0, names=['date', 'value', 'data_type', 'nwis_site_no'])
    numberToName = pd.read_csv(r"/Users/benwilliams/Documents/Data+/nwis_site_info.csv")
    inputSite = '02043433'
    df2 = mockGageData[mockGageData['nwis_site_no']== inputSite]
    df3 = df2[['date', 'value']]
    sdtp = df3.to_csv(index=False)
    df4 = numberToName[numberToName['0']== inputSite]
    if df2.data_type[1] == 60:
        dataToPlot = sdtp.replace('value', 'height')
    elif df2.data_type[1] == 65:
        dataToPlot = sdtp.replace('value', 'flow rate')
    else:
        dataToPlot = sdtp.replace('value', 'precipitation')
    gageTitle = df4['1'][0]
    return dataToPlot, gageTitle

locator = Nominatim(user_agent="otherGeocoder")

def geocode (addressfull):  #geocoder address to coordinates
    try: 
        location = locator.geocode(addressfull)
        if location is None:
            return 0, 0
        else:     
            return location.latitude, location.longitude
    except:
        return "Address Unclear", "Consider Rewriting"


hostname = 'rapid-1304.vm.duke.edu'
port = '5432'
username = 'group3_read'
password = 'water3all4me'
dbname = 'postgres'


postgres_str = 'postgresql://{username}:{password}@{hostname}:{port}/{dbname}'.format(hostname=hostname,
                                                                                 port=port,
                                                                                 username=username,
                                                                                  password=password,
                                                                                 dbname=dbname)
cnx = create_engine(postgres_str)


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

filepath = os.path.join('..','Boundaries', 'NC_statewide_CWS_areas.gpkg')
StateWide = gpd.read_file(filepath) #make large usable dataframe with both names and links
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


