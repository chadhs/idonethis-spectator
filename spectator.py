#!/usr/bin/env python

from flask import Flask
from flask import render_template
import requests
import datetime


## configuration
token = ""
team = ""
user = ""
idturl= "https://idonethis.com"


## the app
app = Flask(__name__)


def get_json_data(url):
    headers = {'content-type': 'application/json', 'authorization': 'token %s' % (token)}
    r = requests.get(url, headers=headers)
    data = r.json()
    dones = data['results']
    return dones


@app.route("/")
def hello():
    return "Hello there."


## TODO
# - load variables from config file
@app.route("/dones")
def display_dones():
    startdate = datetime.date.today() - datetime.timedelta(1)
    enddate = datetime.date.today() - datetime.timedelta(7)

    url_today = "https://idonethis.com/api/v0.1/dones/?done_date=today&owner=%s&team=%s&page_size=100" % (user, team)
    dones_today = get_json_data(url_today)
    dones_today_text = []
    for d in dones_today:
        done = d['markedup_text']
        goal = d['goal_completed']
        done = done.replace("/hashtags","%s/hashtags" % (idturl), 1)
        done = done.replace("/cal","%s/cal" % (idturl), 1)
        dones_today_text.append((done,goal))

    url_lastweek = "https://idonethis.com/api/v0.1/dones/?done_date_after=%s&done_date_before=%s&owner=%s&team=%s&page_size=100" % (enddate, startdate, user, team)
    dones_lastweek = get_json_data(url_lastweek)
    dones_lastweek_text = []
    for d in dones_lastweek:
        done = d['markedup_text']
        goal = d['goal_completed']
        done = done.replace("/hashtags","%s/hashtags" % (idturl), 1)
        done = done.replace("/cal","%s/cal" % (idturl), 1)
        dones_lastweek_text.append((done,goal))

    return render_template('dones.html', team=team, user=user, results_today=dones_today_text, results_week=dones_lastweek_text)


if __name__ == "__main__":
    app.run(debug=True)
