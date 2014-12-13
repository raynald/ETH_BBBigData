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


###Demo Video###
[youtube]

###File List###
    Folders: 
        - report_milestone1: Report of Milestone1
        - report_milestone2: Report of Milestone2
        - report_milestone3: Report of Milestone3
        - report_milestone4: Report of Milestone4
        - static: 300 different colors for representing different clusters
        - templates: Source code for calling Google Map API
    .gitignore: Git ignore file
    EMR.py: Python code for using Amazon EMR service
    README.md: This file
    S3.py: Python code for using API of S3 storage
    clustering.py: K-means clustering 
    features_with_missingvalues.py: Generating features with missing values
    final_new.py: Generating final features
    find_geoloc_by_id.py: Finding geo-location by station ID
    ghcnd-stations.txt: List of ghcnd stations
    global_meanvar_mapper.py: Mapper for calculating global mean and variance
    global_meanvar_reducer.py: Reducer for calculating global mean and variance
    google_map.py: Python interface for drawing on Google Map
    mapper_prediction.py: Mapper of prediction the cluster id for each station in each year
    reducer_prediction.py: Reducer of prediction the cluster id for each station in each year
    mapper_sampling.py: Mapper of coreset sampling
    reducer_sampling.py: Reducer of coreset sampling
    meanvar_mapper2.py: Mapper for calculating mean and variance 
    meanvar_reducer2.py: Reducer for calculating mean and variance
    raw_to_stations.py: Raw data to stations
    stations_to_features_new.py: Stations to features
    test.py: Getting the cluster id of a specific year
    upload_raw_data.py: Uploading all the raw dataset to S3
    video_creater.py: Creating a video from images by Python
    
[youtube]: https://www.youtube.com/watch?v=xQfEk978IE4&list=UUkzQg0KkXhibidSnmizd4Vg&index=2
[boto1]: https://boto.readthedocs.org/en/latest/emr_tut.html
[boto2]: https://boto.readthedocs.org/en/latest/s3_tut.html
