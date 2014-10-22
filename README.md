ETH_BBBigData
=============
##Goal##
1. Data Sources and Data Preparation
    - Original data sources description (source, attributes, features, size)
    
    - Identify the main issues experienced during importing, filtering and 
integrating the data sources
2. Design of your Solution
    - Choice of Analysis Tools / Models
    - Evaluation metrics, how to measure the quality for a solution for your task
3. Implementation and Results
    - The system architecture, used storage and analysis tools
    - Interpretation of Results, and choice of evaluation measure (for the chosen small subset of the real data) 
    - How much did you reduce the data size in order to make the analysis work?  Do you expect the results to improve if the data size would be increased (hypothetically)?
    - Scalability / Performance (Time and Memory): Identify the main bottlenecks of your proof-of-concept system if one would increase the data size.

##Useful Information:##

###Website:###

**ReadMe**: *http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/readme.txt*

**Another ReadMe**: *http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt*

**Data by year**: *http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/*

###Five core elements###
    PRCP = Precipitation (tenths of mm)

    SNOW = Snowfall (mm)

    SNWD = Snow depth (mm)

    TMAX = Maximum temperature (tenths of degrees C)

    TMIN = Minimum temperature (tenths of degrees C)

###Installation:###
1 Step 1: 
    - easy_install Werkzeug
    - easy_install jinja2
    - easy_install itsdangerous
    - easy_install flask
2 Step 2: 
    - Test on your own computer if "import flask" works.

###Usage:###
1. Run: python google_map.py

2. Open your browser, type address: http://127.0.0.1:5000

