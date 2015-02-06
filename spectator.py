#!/usr/bin/env python

from flask import Flask
from flask import render_template
import requests
import datetime
import config


## configuration
token = config.token
team = config.team
user = config.user
idturl= "https://idonethis.com"


## the app
app = Flask(__name__)


## helpers
def get_json_data(url):
    headers = {'content-type': 'application/json', 'authorization': 'token %s' % (token)}
    r = requests.get(url, headers=headers)
    data = r.json()
    dones = data['results']
    return dones


## urls
@app.route("/")
def display_dones():
    startdate = datetime.date.today() - datetime.timedelta(1)
    enddate = datetime.date.today() - datetime.timedelta(7)

    url_today = "https://idonethis.com/api/v0.1/dones/?done_date=today&owner=%s&team=%s&page_size=100" % (user, team)
    dones_today = get_json_data(url_today)
    for done in dones_today:
        done['markedup_text'] = done['markedup_text'].replace("/hashtags","%s/hashtags" % (idturl))
        done['markedup_text'] = done['markedup_text'].replace("/cal","%s/cal" % (idturl))

    url_lastweek = "https://idonethis.com/api/v0.1/dones/?done_date_after=%s&done_date_before=%s&owner=%s&team=%s&page_size=100" % (enddate, startdate, user, team)
    dones_lastweek = get_json_data(url_lastweek)
    for done in dones_lastweek:
        done['markedup_text'] = done['markedup_text'].replace("/hashtags","%s/hashtags" % (idturl))
        done['markedup_text'] = done['markedup_text'].replace("/cal","%s/cal" % (idturl))

    return render_template('dones.html', team=team, user=user, dones_today=dones_today, dones_lastweek=dones_lastweek)


## run app
if __name__ == "__main__":
    app.run(debug=True)
