import datetime as dt
import pandas as pd
import requests

yesterday = dt.date.today() - dt.timedelta(days=1)
api = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
payload = {
    'format': 'geojson',
    'starttime': yesterday - dt.timedelta(days=30),
    'endtime': yesterday
}
response = requests.get(api, params=payload)

# let's make sure the request was OK
response.status_code

yesterday = dt.date.today() - dt.timedelta(days=1)
api = 'https://gis.tempe.gov/arcgis/rest/services/Open_Data/General_Offenses/FeatureServer/1/query'
payload = {
    'format': 'geojson',
    'starttime': yesterday - dt.timedelta(days=30),
    'endtime': yesterday
}
response = requests.get(api, params=payload)

# let's make sure the request was OK
response.status_code
