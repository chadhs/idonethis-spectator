#!/usr/bin/env python

#import json
import requests

## temporary info ##

#user="chadhs"
#done_date=`date '+%Y-%m-%d'`
#base_uri="https://idonethis.com/api/v0.1"
#two_days_ago=`date -v -2d '+%Y-%m-%d'`
#eight_days_ago=`date -v -8d '+%Y-%m-%d'`
#curl -H "Content-type:application/json" -H "Authorization: Token ${api_token}" ${base_uri}/dones/?page_size=100

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

## vars

token = ""
team="witc"

def get_json_data(url):
    headers = {'content-type': 'application/json', 'authorization': 'token %s' % (token)}
    r = requests.get(url, headers=headers)
    data = r.json()
    dones = data['results']
    return dones

def display_dones_today():
    #url = "https://idonethis.com/api/v0.1/dones/?page_size=20"
    url = "https://idonethis.com/api/v0.1/dones/?done_date=today&owner=chadhs&team=witc"
    dones = get_json_data(url)
    print 'today\n'
    for done in dones:
        print '- ',done['raw_text'],'\n'

def display_dones_lastweek():
    #url = "https://idonethis.com/api/v0.1/dones/?page_size=20"
    url = "https://idonethis.com/api/v0.1/dones/?done_date_after=2015-01-15&done_date_before=2015-01-20&owner=chadhs&team=witc"
    dones = get_json_data(url)
    print 'last week\n'
    for done in dones:
        print '- ',done['raw_text'],'\n'

display_dones_today()
display_dones_lastweek()
