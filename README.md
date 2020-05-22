# ABOUT-US
Repo for managing ABOUT-US and related projects

The ```Boundaries``` [directory](Boundaries) contains the boundary data for this project and associated documentation. 


## Asks from NC-DENR 

1. Create a tool to allow utility managers to update boundaries using either geospatial data uploads or map-based point-and-click polygon editing/drawing. (Probably based on GeoNode or some custom combination of leaflet, GeoGig, PostGIS and Geoserver). **This is probably NOT in scope for Data+, but if any students are interested, they can take a crack at it.**

2. A visualization tool to visualize sociodemographic information relevant to infrastructure cost and affordability. Data flows to consider include
 
  - U.S. Census block-group level income, race, employment, education, renter v owner, SFR/multifamily
  - Prevalence of commercial and industrial facilities (e.g. ReferenceUSA)
  - Water rate data [UNC Environmental Finance Center NC rate tables](https://efc.sog.unc.edu/resource/north-carolina-rates-resources#tables)
  
  ## Asks from Triangle Water Supply Partnership (Water Utilities of Chapal Hill/Carrboro, Durham, Raleigh, Cary, Fayetteville)

1. A visualization tool to visualize climate data relevant to utilities, where utilities can visualize the status of water supply of their immediate environment and that of thier neighbors. This ask is descibed in more detail in [DroughtDashboardRequest.md](DroughtDashboardRequest.md)

## Data Sources
(will provide links to descriptions, API documentation, any client libraries)

1. Service Area [Boundaries](Boundaries) of 532 water utilities in North Carolina.
2. [USGS National Hydrography Dataset](https://www.usgs.gov/core-science-systems/ngp/national-hydrography), vector geospatial data charcterizing watersheds, waterbodies, and streams.
3. USGS Streamgages. Read about streamgages [here](https://www.usgs.gov/mission-areas/water-resources/science/streamgaging-basics?qt-science_center_objects=0#qt-science_center_objects). Familiarize yourself with the USGS streamgage data web services [here](https://waterservices.usgs.gov/).
     - [R client package dataRetrieval](https://usgs-r.github.io/dataRetrieval/)
     - [Python client package HydroData](https://hydrodata.readthedocs.io/en/latest/)
4. USGS Monitoring Wells. Read about groundwater monitoring [here](https://water.usgs.gov/ogw/networks.html). Read about groundwater data web services [here](https://water.usgs.gov/ogw/networks.html)
5. State Stream Gages
6. US Army Corps of Engineers Reservoir operations data
7. NOAA weather stations
8. PRISM
9. Daymet



![](/img/duke.png?s=10) ![](/img/iow.jpg?s=10)
