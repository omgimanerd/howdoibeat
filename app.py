#!/usr/bin/python

from flask import Flask
from flask import redirect, render_template, request

BASE_APP_PATH = os.path.dirname(os.path.realpath(__name__))

app = Flask(__name__)
app.secret_key = "secret"

# Homepage
@app.route("/")
def index():
  user = session.get("user", None)
  return render_template("index.html")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Runs the server.")
  parser.add_argument("--debug", default=False, action="store_true")
  args = parser.parse_args()
  app.debug = "debug" in args
  app.run()
