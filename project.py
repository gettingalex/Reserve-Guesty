#!/usr/bin/env python
# All modules needed for this app
from flask import (Flask, render_template,
                   request, redirect, jsonify, url_for, flash)
import httplib2
import json
import requests
import stripe
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

#Keys for Stripe
pub_key = 'pk_test_gQRV3GY6b5U8JWDUscP9QKUT'
secret_key_stripe = 'Removed'

stripe.api_key = secret_key_stripe

@app.route('/')
@app.route('/reserver')
def checkDate():
    url = "https://api.guesty.com/api/v2/listings/"
    user = "Removed"
    password = "Removed"
    resp = requests.get(url, auth=HTTPBasicAuth(user, password))
    if resp.status_code != 200: 
        print('Status:', resp.status_code, 'Problem with the request. Exiting.')
        exit()
    data = resp.json()
    results = data['results']
    global newList
    newList = {}
    newList["listings"] = []
    listings = newList["listings"]
    for i in results:
        listings.append({'nickname' : i['nickname'], 'id': i['_id']})
    return render_template(
        'index.html', newList=newList
    )

def listingName(unit):
    for i in newList["listings"]:
        if unit == i['id']:
            return i['nickname']

@app.route('/disponibilites', methods=['POST'])
def listingForm():
    unit = request.form['unit']
    nickname = listingName(unit)
    fromDate = request.form['from']
    toDate = request.form['to']
    url = "https://api.guesty.com/api/v2/listings/"+unit+"/calendar?from="+fromDate+"&to="+toDate
    user = "Removed"
    password = "Removed"
    resp = requests.get(url, auth=HTTPBasicAuth(user, password))
    if resp.status_code != 200: 
        print('Status:', resp.status_code, 'Problem with the request. Exiting.')
        exit()
    data = resp.json()
    DateList = {}
    DateList["listings"] = []
    listings = DateList["listings"]
    for i in data:
        listings.append({'date' : i['date'], 'status' : i['status'], 'price' : i['price']})
    period = listings.pop()
    allBooked = all(listing['status'] == 'booked' for listing in listings)
    allFree = all(listing['status'] == 'available' for listing in listings)
    #Return total price for selected date
    prices = []
    for i in listings:
        prices.append(i['price'])
    subTotal = sum(prices)
    stripeSubTotal = subTotal*100
    avgNight = 0
    if prices != []:
        avgNight = subTotal/len(prices)
        if allBooked == True:
            flash('Les dates que vous avez selectionnés ne sont pas disponibles.')
        if allFree == True:
            return render_template('booking.html', avgNight=avgNight, subTotal=subTotal, pub_key=pub_key, stripeSubTotal=stripeSubTotal, fromDate=fromDate, toDate=toDate, nickname=nickname)   
        if allBooked == False and allFree == False:

            flash('Certaines dates sélectionnés ne sont pas disponibles.')
    else: 
        flash("Les dates sélectionnés ne sont pas valides.")
    return redirect(url_for('checkDate'))

@app.route('/merci')
def merci():
    return render_template('merci.html')

@app.route('/pay/<int:stripeSubTotal>/', methods=['POST'])
def pay (stripeSubTotal):
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=stripeSubTotal,
        currency='usd',
        description='Reservation - Hebergement - Sejour de Reve',
        receipt_email='ar_creation@me.com'
        )

    return redirect(url_for('merci'))
    #for testing and see if the request was sent and return from stripe
    #print(request.form)
    #return ''

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)