import pandas as pd
import numpy as np
import requests
import json
import hashlib
import timeit

class GeoEtl(object):
    def __init__(self):
        pass

    def _getRegions(self):
        URL = "https://restcountries-v1.p.rapidapi.com/all"
        HEADERS = {
            'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
            'x-rapidapi-key': "729324cea1mshc6255d3b0979a04p1d233ejsnbb643168d529"
        }
        response = requests.get(URL, headers=HEADERS)
        response_dict = json.loads(response.text)
        regions_df = pd.DataFrame(response_dict).replace(r'^\s*$', np.nan, regex=True)
        regions = regions_df['region'].unique()
        mask = pd.isnull(regions)
        regions = regions[~mask]
        return regions

    def _getCountryByRegion(self, region=''):
        URL = "https://restcountries.eu/rest/v2/region/{0}".format(region.lower())
        r = requests.get(URL)
        country = json.loads(r.text)[0]
        language = country['languages'][0]['name']
        encrypted_language = hashlib.new("sha1", language.encode())
        required_data = {
            'region': region,
            'country': country['name'],
            'language': str(encrypted_language.hexdigest())
        }
        return required_data

    def obtainData(self):
        regions = self._getRegions()
        data = pd.DataFrame()
        for region in regions:
            startime = timeit.default_timer()
            country_data = self._getCountryByRegion(region)
            country_data['time'] = timeit.default_timer() - startime
            data = data.append(country_data, ignore_index=True)
        self.dataframe = data

    def getDataKpis(self):
        print(self.dataframe.describe(include=np.number))
            