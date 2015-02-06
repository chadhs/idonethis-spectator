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
idturl = "https://idonethis.com"
api_dones_url = idturl + '/api/v0.1/dones/?'

## the app
app = Flask(__name__)


## helpers
def get_json_data(url):
    """
    fetch dones from the iDoneThis api, return list of dones from the json response
    """
    headers = {'content-type': 'application/json', 'authorization': 'token %s' % (token)}
    r = requests.get(url, headers=headers)
    data = r.json()
    dones = data['results']
    return dones

def fix_rel_url(dones):
    """
    replace relative urls in markedup_text with absolute urls
    """
    for done in dones:
        done['markedup_text'] = done['markedup_text'].replace("/hashtags","%s/hashtags" % (idturl))
        done['markedup_text'] = done['markedup_text'].replace("/cal","%s/cal" % (idturl))
    return dones


## urls
@app.route("/")
def display_dones():
    startdate = datetime.date.today() - datetime.timedelta(1)
    enddate = datetime.date.today() - datetime.timedelta(7)

    url_today = "%sdone_date=today&owner=%s&team=%s&page_size=100" % (api_dones_url, user, team)
    dones_today = get_json_data(url_today)
    dones_today = fix_rel_url(dones_today)

    url_lastweek = "%sdone_date_after=%s&done_date_before=%s&owner=%s&team=%s&page_size=100" % (api_dones_url, enddate, startdate, user, team)
    dones_lastweek = get_json_data(url_lastweek)
    dones_lastweek = fix_rel_url(dones_lastweek)

    return render_template('dones.html', team=team, user=user, dones_today=dones_today, dones_lastweek=dones_lastweek)


## run app
if __name__ == "__main__":
    app.run(debug=True)
