#!/usr/bin/python
# This is the app file that is run on the server.
# Author: alvin.lin.dev@gmail.com (Alvin Lin)

from flask import Flask
from flask import redirect, render_template, request

from lib.data_analyzer import DataAnalyzer
from lib.util import Util

import argparse
import os

BASE_APP_PATH = os.path.dirname(os.path.realpath(__name__))

app = Flask(__name__)
app.secret_key = "secret"
data_analyzer = DataAnalyzer.create()

# Homepage
@app.route("/")
def index():
    return render_template("index.html", summoner=None)

@app.route("/<summoner_name>", methods=["GET", "POST"])
def query_summoner(summoner_name):
    if request.method == "GET":
        return render_template("index.html", summoner=summoner_name)
    else:
        mastery_data = data_analyzer.get_summoner_mastery_info(summoner_name)
        main_roles = data_analyzer.get_main_role_analysis(mastery_data)
        current_game_data = data_analyzer.get_current_game_data(summoner_name)
        return Util.json_dump({
            "mastery": mastery_data,
            "main_role": main_roles,
            "current_game": current_game_data
        })

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Runs the server.")
    parser.add_argument("--debug", default=False, action="store_true")
    args = parser.parse_args()
    app.debug = args.debug
    print app.debug
    app.run()
