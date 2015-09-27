__author__ = 't35khan'

from urllib import request
import json
from getmyapi import GetAPI

google_api_key = GetAPI.getapi('google_api_key')

class GetCountry:
    def getcountry(city):
        link = "https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}".format(city,google_api_key)
        data_json = (request.urlopen(link).read())
        data_json = data_json.decode('utf-8')
        data_json = json.loads(data_json)
        country = []
        if data_json:
            for entry in data_json['results']:
                country.append(entry['formatted_address'].split(", ")[-1])
            if len(country)>1:
                country = GetCountry.bestcountry(country)
                return country
            else:
                return country[0]
        else:
            return False

    def bestcountry(country_list):
        country_dict = {}
        for country in country_list:
            try:
                country_dict[country] += 1
            except:
                country_dict[country] = 1
        country_dict = sorted(country_dict.items(), key=lambda x: x[1], reverse=True)
        return country_dict[0][0]




