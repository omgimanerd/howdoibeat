#!/usr/bin/python
# This class handles the analysis of the data fetched from the Riot Games API.
# Author: alvin.lin.dev@gmail.com (Alvin Lin)

from riot_api import RiotApi
from util import Util

import json

class DataAnalyzer():

    def __init__(self, static_data):
        self.static_data = static_data

    @staticmethod
    def create():
        with open("./static/champions.json") as champions_file:
            champions = json.loads(champions_file.read())
        return DataAnalyzer({
            "champions": champions
        })

    def get_summoner_mastery_info(self, summoner_name):
        summoner_id = RiotApi.get_summoner_id(summoner_name)
        if not summoner_id:
            return None
        mastery = RiotApi.get_champion_mastery_data(summoner_id)
        for champion in mastery:
            champion_id = str(champion["championId"])
            champion["champion"] = self.static_data["champions"][champion_id]
        return mastery

if __name__ == "__main__":
    d = DataAnalyzer.create()
    print Util.json_dump(d.get_summoner_mastery_info("omgimanerd"))
