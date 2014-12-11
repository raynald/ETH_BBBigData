ETH_BBBigData
=============
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
1. Run: python google_map.py *year_number*

2. Open your browser, type address: http://127.0.0.1:5000

###Useful notes###
  - An Introduction to boto's Elastic Mapreduce Interface [boto1]
  - An Introduction to boto's S3 interface [boto2]

[boto1]: https://boto.readthedocs.org/en/latest/emr_tut.html
[boto2]: https://boto.readthedocs.org/en/latest/s3_tut.html
