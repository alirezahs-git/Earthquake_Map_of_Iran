import requests


def api_url_all(startdate, enddate):
    return f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={startdate}&endtime={enddate}&minlatitude=28.251373&minlongitude=44.425491&maxlatitude=39.981287&maxlongitude=65.715857'


def api_url_point(startdate, enddate, latitude, longitude):
    return f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={startdate}&endtime={enddate}&latitude={latitude}&longitude={longitude}&maxradiuskm=1000'


def call_api(url):
    r = requests.get(url)
    return r.json()
