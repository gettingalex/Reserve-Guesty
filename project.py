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
@app.route('/reserver')
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
    newList = {}
    newList["listings"] = []
    listings = newList["listings"]
    for i in results:
        listings.append({'nickname' : i['nickname'], 'id': i['_id']})
    return render_template(
        'index.html', newList=newList
        )



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    #    app.secret_key = 'super_secret_key'