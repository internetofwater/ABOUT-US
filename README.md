# ABOUT-US
Repo for managing ABOUT-US and related projects

The ```Boundaries``` [directory](Boundaries) contains the boundary data for this project and associated documentation. 


# Asks from NC-DENR 

1. Create a tool to allow utility managers to update boundaries using either geospatial data uploads or map-based point-and-click polygon editing/drawing. (Probably based on GeoNode or some custom combination of leaflet, GeoGig, PostGIS and Geoserver). **This is probably NOT in scope for Data+, but if any students are interested, they can take a crack at it.**

2. A visualization tool to visualize sociodemographic information relevant to infrastructure cost and affordability. Data flows to consider include
 
 ## Social Data Sources
  - U.S. Census block-group level income, race, employment, education, renter v owner, SFR/multifamily. [Portal](https://data.census.gov/cedsci/) and [APIs](https://www.census.gov/data/developers/data-sets.html)
      - [R client package](https://github.com/walkerke/tidycensus)
      - [Python client library](https://jtleider.github.io/censusdata/)
  - Prevalence of commercial and industrial facilities (e.g. ReferenceUSA)
  - Water rate data [UNC Environmental Finance Center NC rate tables](https://efc.sog.unc.edu/resource/north-carolina-rates-resources#tables)
  
  # Asks from Triangle Water Supply Partnership (Water Utilities of Chapal Hill/Carrboro, Durham, Raleigh, Cary, Fayetteville)

1. A visualization tool to visualize climate data relevant to utilities, where utilities can visualize the status of water supply of their immediate environment and that of their neighbors. This ask is descibed in more detail in [DroughtDashboardRequest.md](DroughtDashboardRequest.md) See [this presentation](/img/nighthawk_presentation.pptx) for some background and design mockups

## Environmental Data Sources
(will provide links to descriptions, API documentation, any client libraries)

1. Service Area [Boundaries](Boundaries) of 532 water utilities in North Carolina.
2. [USGS National Hydrography Dataset](https://www.usgs.gov/core-science-systems/ngp/national-hydrography/national-hydrography-dataset?qt-science_support_page_related_con=0#qt-science_support_page_related_con), vector geospatial data charcterizing watersheds, waterbodies, and streams.
3. USGS Streamgages. Read about streamgages [here](https://www.usgs.gov/mission-areas/water-resources/science/streamgaging-basics?qt-science_center_objects=0#qt-science_center_objects). Familiarize yourself with the USGS streamgage data web services [here](https://waterservices.usgs.gov/).
     - [R client package dataRetrieval](https://usgs-r.github.io/dataRetrieval/)
     - [Python client library HydroData](https://hydrodata.readthedocs.io/en/latest/)
4. USGS Monitoring Wells. Read about groundwater monitoring [here](https://water.usgs.gov/ogw/networks.html). Read about groundwater data web services [here](https://water.usgs.gov/ogw/networks.html)
5. State Stream Gages
6. US Army Corps of Engineers [Corps Water Management System](https://www.hec.usace.army.mil/cwms/) and [data services](https://water.usace.army.mil/dist/docs/#api-_). Mostly relevant for [Jordan Lake](https://deq.nc.gov/about/divisions/water-resources/planning/basin-planning/map-page/cape-fear-river-basin-landing/jordan-lake-water-supply-allocation/jordan-lake-water-supply-allocation-background-info) and Falls Lake (main water supply for Raleigh). The Corps runs it and many Triangle Water Utilties source a lot of their water based on legal-operational "allocations" from Jordan Lake. 
7. NOAA weather stations. [Data](https://www.ncdc.noaa.gov/cdo-web/) and [web services](https://www.ncdc.noaa.gov/cdo-web/webservices/v2).
      - [R client package](https://ropensci.org/tutorials/rnoaa_tutorial/)
      - [Python client library](https://github.com/paulokuong/noaa)
8. [PRISM](http://www.prism.oregonstate.edu/) (for gridded temperature and precipitation data)
9. Daymet
10. US Drought Monitor. [Explanation](https://droughtmonitor.unl.edu/About/WhatistheUSDM.aspx) and [Web Services](https://droughtmonitor.unl.edu/WebServiceInfo.aspx)
11. NC State Climate Office [data service](https://climate.ncsu.edu/cronos)






![](/img/duke.png?s=10) ![](/img/iow.jpg?s=10)
