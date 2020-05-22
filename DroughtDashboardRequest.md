![](RackMultipart20200522-4-1cv0mcx_html_cac2e8208ac978d2.png) ![](RackMultipart20200522-4-1cv0mcx_html_497be7d2f66bd0bd.jpg)

# Triangle Drought/Water Supply Dashboard

May 5, 2020

Organized into user stories below

# What is the water supply status for my utility?

## Question 1: Who provides my water?

The user will click on search bar and enter location. Map will zoom to address. If the address is located within a utility, the user will see which utility covers their area. The user clicks on the utility.

**Data:** service area boundaries (shp, kml, geoJSON)

**Outcome** : User knows which utility provides water to their area.

**Add On.** The utility also provides the sources of water: reservoir, stream, groundwater wells. Draw the watershed boundary for the water supply region.

**What this can look like on dashboard:**

- Users can select through drop down menu (county, utility) or by clicking on map.
- Once a utility is selected, we can provide
  - a list with icons for reservoir, stream groundwater, another utility and the name of that entity.
  - They can show up on the map
- Other

## Question 2: What is the water conservation status of my utility?

The user will be able to see any water shortage response plans and water conservation status associated with the utility. This is truly a &quot;what can I, as a person in my utility do? type of question. Each utility has a water shortage response plan defining what is permissible at different conservation levels.

Water shortage plans are not always tied to drought status (less than 10% use drought as a trigger to water shortage responses and instead use reservoir levels, streamflow, etc). We need to be clear in the dashboard what each of those means. The general public likely cares about the conservation status. Water utility managers are interested in seeing both and a drought status should be included if we do two dashboards (one for public and one for utilities).

**Additional Data:** utilities will need to provide this information. If the utilities are unable to supply these data, we can pull from NCDEQ: [https://www.ncwater.org/Drought\_Monitoring/statusReport.php](https://www.ncwater.org/Drought_Monitoring/statusReport.php). Discussions indicated that these data are sporadically updated. They are only regularly updated in times of drought when legislation is triggered. DEQ is interested in revamping some aspects of their website and could be interested in updating the data flows for utilities to report their water conservation and weekly updates (currently data entry is manual). This might be a better place for the dashboard to pull data from rather than having utilities use two different systems.

The data included in these reports are: conservation status, weekly water use, water sales, and purchases.

**Outcome:** User will know if there are any drought related policies and the drought status for the utility. User will be able to see their current drought status per utility definition (Figure 1).

**Challenge:** Each utility&#39;s water shortage plan differs in terms of what a conservation stage entails, thresholds, used, etc. One thought is that users will click on their utility and it will tell them the conservation status. Then they click on a link that takes them to their water shortage plan. The challenge is this is not very user friendly. One option, may be for a student to take the work done by the Triangle Water Supply Partnership to create a standardized table. This way, a person can click on their utility, see their status, and see what rules apply for them with the current status. Sarah will provide the current tables.

**What this can look like on dashboard:**

- User sees their conservation status and
  - A link taking them to the water conservation / water shortage plans that they peruse to find what the current conservation status means for them
  - The team creates a standardized table that links together conservation status with action steps for individuals.

## Question 3: What is the current water supply status of my utility?

There was a lot of conversation around what metrics are appropriate since utilities use different metrics depending on their water source.

**Utility Metrics**

- Utilities primarily relying on reservoirs may use days of supply remaining. Some utilities find their customers like this number while others have found it creates confusion as the number may fluctuate widely depending on precipitation, conservation efforts, finding new water sources and so on. There was also concern that it provides the worst case scenario and creates undue alarm (assumes no rain and no conservation). Some utilities have moved away and use percent of storage volume in reservoir remaining. The method for estimating days of supply remaining also vary considerably between utilities.
  - Raleigh – uses percent remaining in Falls Lake based on Corps probabilistic models
  - Durham uses the OASIS model
  - Cary uses 30 days of previous month&#39;s production.

- One suggested method for helping to reduce confusion if we want to use number of days of supply remaining is to offer scenarios:
  - Estimated number of days with current demand
  - Estimated number of days if demand is reduced by x%
  - Estimated number of days if demand is reduced by xx%
- This approach could be helpful in that it communicates to residents that their conservation efforts _ **do** _ have an impact.

- Utilities relying on surface water do not use number of days of supply remaining. The further down the watershed, the more complicated the picture as different areas of the watershed may be in different drought conditions.
- The bottom line is that if we use utility based metrics, the utilities will have to provide those metrics each week and there will be no ability to compare between utilities.

**More standardized metrics**

- Many of the utilities thought it would be nice to have a semi-standardized metric to compare with others.
- One suggestion was to look at trends… are we getting more or less water? Are we going in a good or bad direction. This could be as simple as showing the utilities goal for water levels (be it a reservoir or streamflow or groundwater, and what levels have been doing for the past XXX months or year).
- Another suggestion that could be applied to all sources of water is calculating the current groundwater level, streamflow, or reservoir level compared to the median for this time of year. This would require utilities to provide a historic dataset for their wells and gages. Again, the outcome will vary based on how many years of data are provided (5 years compared to 50 years compared to 100 years).
  - This approach would require building a data flow for utilities to share those information.
  - Ideally this would not be a &quot;utility&quot; metric but would exist for each water source a utility uses.
- A similar method suggested was to look at the 25th, 50th and 75th percentile for that time of year. Trending could be seen on this type of plot if extend beyond a year.

- The above illustrate the supply side of the equation. The demand side can also be provided by utilities to show trends and if conservation is &quot;working&quot;, if demand is going up or down. This number would need to normalized to gallons / day / account. A historic record would be great. Users could adjust the range of years because demand patterns have changed a lot. They might also want to see demand during past drought years only.
  - This could become a fun way for customers to compare how they are doing with nearby utilities. Might incentivize more conservation.
  - Could also be a loose equation (like a game) where we have the supply side and assume no more water and then show what percent they will be at in a month given current demand… if they reduce their use by x%.

**Additional Data:**

- Utilities can provide their metric for estimating water supply status be it Corps estimates, number of days of supply remaining, etc.
- Utilities can supply the gage data they use for measuring supply
  - This can be external (USGS, Corps) or it could be internal (their own reservoir levels, gw well levels, or streamflow gage).
  - A comparative metric can be estimated relative to the data provided.
    - The comparison will of course vary based on how long of a record each utility provides (so if some only have data from 2010 onwards they will be missing severe droughts and floods that could change the summary statistics a bit).
- Utilities can provide monthly demand data and number of accounts (needed for the game if we want to do that).

**Outcome:** User will have situational awareness about supply and demand.

**What this can look like on dashboard:**

- Several liked the idea of a map showing current conditions compared to historic. Something similar to the USGS.

![](RackMultipart20200522-4-1cv0mcx_html_471838810d93b85a.png)

- Then if a user clicks on a point you can see more details – a time series that shows trend and compares with historic record or within a time period selected by the user. There are two plots that come immediately to mind as shown below. Depending on years of data available from utilities, the top graph may be better so folks can see how much data is being considered.
- Showing the current year in bold with previous years of data in light gray lines. Certain historic lines could be colored (such as the 2007-2008 or 2000-2002 droughts).

![](RackMultipart20200522-4-1cv0mcx_html_21557dc83756bb60.jpg)

- Showing current year in bold with previous years summarized in a boxplot (blue line is median – could get rid of this and just show current year instead), dark shaded area is 25-75%, light shaded area is 10-90% and dashed lines are min and max for Falls Lake (1984-2014). This shows how full the reservoir is according to its guide curve (at 100% the multi-purpose pool is full, above 100% the flood control pool is filling, and below 100% is summer/drought). I just drew a thick red line to show what that you could draw the current year on the plot and see what happens.

![](RackMultipart20200522-4-1cv0mcx_html_36517c9d459a4e38.gif)

- We can do something similar with demand and/or create a kind of game.

## Question 4: How does this drought compare with other droughts for my water utility?

Utilities noted that droughts are incredibly unique. They intensify at different paces, come at different times of year, and last for different lengths. They were not sure how helpful drought indicators would be. That said, some do look at drought data and would be interested in seeing it. There was a desire to see not just the map, but also what drought is doing over time.

There was a conversation around resident memory – the last major drought was 2007-2008. There has been a lot of turnover in residents since then. Will folks remember those older droughts? Perhaps it would be helpful to see the last time a water supply got to some critical level in a historic context. Some way to communicate to residents the level of concern they should be experiencing.

**Outcome:** User knows how the impacts of this drought compare with previous droughts.

**What this can look like on dashboard:**

It was unclear if folks wanted to see drought metrics on the dashboard. However, we could link to or maybe embed within the dashboard a link to Esri&#39;s drought dashboard. They do a pretty slick job.

Esri has a pretty nice drought tracker that shows current drought status and lets you click on a county to see a time series of drought. [https://livingatlas.arcgis.com/drought/](https://livingatlas.arcgis.com/drought/)

![](RackMultipart20200522-4-1cv0mcx_html_3b478ca817863f85.png)

## Question 5: Where does the water in my utility come from?

The utility will need to provide information on their water supply service area. Ideally, this will be a HUC (HUCs), list of rivers, reservoirs, aquifers, and/or interconnections. Utilities thought this should be simple. They like the idea of drawing the watershed boundary for their water supply but did not want to use the boundary for locating data.

**Additional Data:**

- water supply service area boundaries (shp, kml, geoJSON) or the location (lat longs) of water supply sources. If these data do not exist, a list of HUCs feeding into the system can suffice.
- List of interconnections that includes at a minimum the pwsid, sells/purchases, etc. Will need the water supply of the interconnected system as well. Can pull from LWSPs.

**Outcome:** User knows the water supply service area and associated data to pull from to understand water supply conditions.

# What is the water supply status for regional area?

## Question 6: What is the general water condition outside of my utility (regionally)?

Current meteorological and hydrological conditions can be mapped relative to historic conditions. This can be done for the water supply basins or beyond.

**Additional Data:**

- Stream gages (relative to &#39;normal&#39;): Federal, State, Utility
- Groundwater monitoring levels (relative to &#39;normal&#39;): USGS, State, Utility
- Precipitation (relative to &#39;normal&#39;): Federal, State, Other
- Reservoir levels (relative to &#39;normal&#39;): Federal, State, Utility

**Outcome:** User will see where the current conditions sit relative to historic conditions. Particular droughts and periods can be highlighted to provide additional context. The data can be shown for the entire region or for a particular utilities water supply sources.

**What this can look like on dashboard:**

This would look similar to what was articulated in question 3 with a map showing colored dots relative to historic conditions and a way of showing time series data. Folks recommended checking out the State Climate Office graphs. The map could have a check box option to turn on/off precipitation, streamflow, and reservoir data.

## Question 7: What do forecasts predict for future conditions?

Is rain predicted in the near or long-term future? While we will not model those outcomes, we can pull in NOAA predicted forecasts for precipitation and temperature… primarily will it be dry, wet, hot, and so on. The group tended to look 8 to 14 days out in terms of forecasts and they use NOAA&#39;s . NOAA climate precip and look at temp and precipitation. They look at 8-14 days out. Tend to trust those more. Longer ones are less helpful.

[https://www.cpc.ncep.noaa.gov/products/predictions/short\_range/NAEFS/Outlook\_D264.00.php](https://www.cpc.ncep.noaa.gov/products/predictions/short_range/NAEFS/Outlook_D264.00.php)

  - Cary – likes quantitative forecast tool and likes that a lot (QPF) for shorter term: [https://www.wpc.ncep.noaa.gov/qpf/qpf2.shtml](https://www.wpc.ncep.noaa.gov/qpf/qpf2.shtml)
- Some utilities look at 3 months out precipitation forecast just as a up or down.
- Most do not find these forecasts to be reliable, but there is often a desire from the public and press to be able to know if it is likely to rain soon.

**What this can look like on dashboard:**

We can simply show the image as a link or pull it into the dashboard. Or better yet, the State Climate Office has been doing work around how to communicate forecasts better and can provide some guidance on what that might look like.

5 | Page
