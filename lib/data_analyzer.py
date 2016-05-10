#!/usr/bin/python
# This class handles the analysis of the data fetched from the Riot Games API.
# Author: alvin.lin.dev@gmail.com (Alvin Lin)

from riot_api import RiotApi
from util import Util

import json

class DataAnalyzer():

    def __init__(self, champions, summoner_spells):
        self.champions = champions
        self.summoner_spells = summoner_spells

    @staticmethod
    def create():
        return DataAnalyzer(
            RiotApi.get_champions(),
            RiotApi.get_summoner_spells()
        )

    def get_summoner_mastery_info(self, summoner_name):
        summoner_id = RiotApi.get_summoner_id(summoner_name)
        if not summoner_id:
            return None
        mastery = RiotApi.get_champion_mastery_data(summoner_id)
        return mastery

    def get_main_role_analysis(self, mastery_data):
        main_role = {}
        for champion in mastery_data:
            champion_info = self.champions[str(champion["championId"])]
            champion["champion"] = champion_info
            for tag in champion_info["tags"]:
                if tag in main_role:
                    main_role[tag] += champion["championPoints"]
                else:
                    main_role[tag] = champion["championPoints"]
        return sorted(main_role, key=main_role.get)[::-1]

    def get_current_game_data(self, summoner_name):
        summoner_id = RiotApi.get_summoner_id(summoner_name)
        if not summoner_id:
            return None
        current_game = RiotApi.get_current_game_data(summoner_id)
        if current_game:
            players = current_game.get("participants")
            for player in players:
                del player["masteries"]
                del player["runes"]
                del player["profileIconId"]
                player["champion"] = self.champions[str(player["championId"])]
                player["spell1"] = self.summoner_spells[str(player["spell1Id"])]
                player["spell2"] = self.summoner_spells[str(player["spell2Id"])]
        return current_game

if __name__ == "__main__":
    d = DataAnalyzer.create()
    mastery = d.get_summoner_mastery_info("omgimanerd")
    roles = d.get_main_role_analysis(mastery)
    print roles
    cgame = d.get_current_game_data("Voyboy")
    print cgame
