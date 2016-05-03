#!/usr/bin/python
# This class handles the sending of requests to Riot's servers for data and
# handles all errors, such as rate limiting.
# Author: alvin.lin.dev@gmail.com (Alvin Lin)

import json
import os
import requests
import time

BASE_URL = "https://na.api.pvp.net"

RATE_LIMIT_EXCEEDED_RESPONSE = 429

class RiotApi():

    @staticmethod
    def get_api_key():
        api_key = os.environ.get("RIOT_API_KEY", None)
        if api_key:
            return api_key
        else:
            raise ValueError("API key not found. Did you forget to . ./setup?")

    @staticmethod
    def get(path, params):
        response = requests.get("%s%s" % (BASE_URL, path), params=params)
        while response.status_code == RATE_LIMIT_EXCEEDED_RESPONSE:
            print "Rate limit exceeded during query, waiting 2 seconds!"
            time.sleep(2)
            response = requests.get("%s%s" % (BASE_URL, path), params=params)
        return json.loads(response.text)

    @staticmethod
    def get_champions():
        request_path = "/api/lol/static-data/na/v1.2/champion"
        request_params = {
            "dataById": True,
            "api_key": RiotApi.get_api_key()
        }
        champions = RiotApi.get(request_path, request_params)
        return champions.get("data")

    @staticmethod
    def get_summoner_id(summoner_name):
        request_path = "/api/lol/na/v1.4/summoner/by-name/%s" % (summoner_name)
        request_params = { "api_key": RiotApi.get_api_key() }
        summoner = RiotApi.get(request_path, request_params)
        return summoner.get(summoner_name, {}).get("id")

    @staticmethod
    def get_champion_mastery_data(summoner_id):
        request_path = "/championmastery/location/na1/player/%s/champions" % (
            summoner_id
        )
        request_params = { "api_key": RiotApi.get_api_key() }
        mastery = RiotApi.get(request_path, request_params)
        return mastery

if __name__ == "__main__":
    print RiotApi.get_summoner_id("asasdhe9hr")
