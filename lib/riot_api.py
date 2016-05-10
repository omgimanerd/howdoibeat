#!/usr/bin/python
# This class handles the sending of requests to Riot's servers for data and
# handles all errors, such as rate limiting.
# Author: alvin.lin.dev@gmail.com (Alvin Lin)

from util import Util
from decorators import cache

import json
import os
import requests
import time

BASE_URL = "https://na.api.pvp.net"

RATE_LIMIT_EXCEEDED_RESPONSE = 429

class RiotApi():

    @staticmethod
    @cache
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
        path = "/api/lol/static-data/na/v1.2/champion"
        params = {
            "dataById": True,
            "champData": "tags",
            "api_key": RiotApi.get_api_key()
        }
        champions = RiotApi.get(path, params)
        return champions.get("data")

    @staticmethod
    def get_summoner_spells():
        path = "/api/lol/static-data/na/v1.2/summoner-spell"
        params = {
            "dataById": True,
            "api_key": RiotApi.get_api_key()
        }
        spells = RiotApi.get(path, params)
        return spells.get("data")

    @staticmethod
    @cache
    def get_summoner_id(summoner_name):
        summoner_name = summoner_name.replace(" ", "").lower()
        path = "/api/lol/na/v1.4/summoner/by-name/%s" % (summoner_name)
        params = { "api_key": RiotApi.get_api_key() }
        summoner = RiotApi.get(path, params)
        return summoner.get(summoner_name, {}).get("id")

    @staticmethod
    def get_champion_mastery_data(summoner_id):
        path = "/championmastery/location/na1/player/%s/champions" % (
            summoner_id
        )
        params = { "api_key": RiotApi.get_api_key() }
        mastery = RiotApi.get(path, params)
        return mastery

    @staticmethod
    def get_current_game_data(summoner_id):
        path = "/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/%s" % (
            summoner_id
        )
        params = { "api_key": RiotApi.get_api_key() }
        current_game_data = RiotApi.get(path, params)
        if current_game_data.get("status", {}).get("status_code") == 404:
            return None
        return current_game_data

if __name__ == "__main__":
    print RiotApi.get_summoner_id("leotam1234")
