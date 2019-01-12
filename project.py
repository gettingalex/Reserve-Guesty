#!/usr/bin/env python
# All modules needed for this app
from flask import (Flask, render_template,
                   request, redirect, jsonify, url_for, flash)
import httplib2
import json
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def checkDate():
    url = "https://api.guesty.com/api/v2/listings/"
    user = "***Removed***\"
    password = "***Removed***}"
    resp = requests.get(url, auth=HTTPBasicAuth('removed'\, 'removed'}))
    if resp.status_code != 200: 
        print('Status:', resp.status_code, 'Problem with the request. Exiting.')
        exit()
    data = resp.json()
    results = data['results']
    newList = []
    for i in results:
        newList.append(i['nickname'])
    return jsonify(newList)
    # newList=[]
    # for i in data:
    #    newList.append(data['results'][i]['_id'])
    # return jsonify(newList)

def listingList():
    return "test"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    #    app.secret_key = 'super_secret_key'