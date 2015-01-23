#!/usr/bin/env python

from flask import Flask
from flask import render_template
import requests


## configuration
token = ""
team = ""
user = ""


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
#- date math to replace static dates
#- proper goal display
@app.route("/dones")
def display_dones():
    url_today = "https://idonethis.com/api/v0.1/dones/?done_date=today&owner=%s&team=%s" % (user, team)
    dones_today = get_json_data(url_today)
    dones_today_text = []
    for done in dones_today:
        dones_today_text.append(done['raw_text'])
        #dones_today_text.append(done['markedup_text'])

    url_lastweek = "https://idonethis.com/api/v0.1/dones/?done_date_after=2015-01-15&done_date_before=2015-01-20&owner=%s&team=%s" % (user, team)
    dones_lastweek = get_json_data(url_lastweek)
    dones_lastweek_text = []
    for done in dones_lastweek:
        dones_lastweek_text.append(done['raw_text'])

    return render_template('dones.html', team=team, user=user, results_today=dones_today_text, results_week=dones_lastweek_text)


if __name__ == "__main__":
    app.run(debug=True)


## done data for reference ##

#done_date=`date '+%Y-%m-%d'`
#two_days_ago=`date -v -2d '+%Y-%m-%d'`
#eight_days_ago=`date -v -8d '+%Y-%m-%d'`

#{
    #"comments": [],
    #"created": "2015-01-14T20:12:15.446",
    #"done_date": "2015-02-16",
    #"goal_completed": true,
    #"id": 17387024,
    #"is_goal": false,
    #"likes": [],
    #"markedup_text": "<a href=\"/hashtags/witc/#tags/vacation\" rel=\"nofollow\">#vacation</a> day off, returning from skiing",
    #"meta_data": {},
    #"owner": "smalter",
    #"permalink": "https://idonethis.com/done/17387024/",
    #"raw_text": "#vacation day off, returning from skiing",
    #"tags": [
        #{
            #"id": 91336,
            #"name": "vacation"
        #}
    #],
    #"team": "https://idonethis.com/api/v0.1/teams/witc/",
    #"team_short_name": "witc",
    #"updated": "2015-01-14T20:12:15.530",
    #"url": "https://idonethis.com/api/v0.1/dones/17387024/"
#}
