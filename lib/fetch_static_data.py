#!/usr/bin/python
# This executable fetches static data from the Riot API and stores it in
# lib/static.
# Author: alvin.lin.dev@gmail.com (Alvin Lin)

from riot_api import RiotApi
from util import Util

if __name__ == "__main__":
    with open("./static/champions.json", "w") as champions_file:
        champions_file.write(Util.json_dump(RiotApi.get_champions()))
    print "Wrote champions.json"
