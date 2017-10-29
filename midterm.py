from flask import Flask, request, render_template, make_response, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, Form
from wtforms.validators import Required
import requests
import json

# Tell grader
import tweepy

auth = tweepy.OAuthHandler("HMDEZrAd2HZaNmIypzJohbkCT", "EaqKH4HWP9749QAEQ6wIspK1awlKYYcKTzeeqPIdf3afZEra23")
auth.set_access_token("4854852197-8jZvoSQi6f7gl8U6w3BLrra3k2mCcCvVF0ssp27", "e232GRiCiMXz4BrKFFTXWyUT4eDzTeh4SvBmYqGEPGjiN")

api = tweepy.API(auth)


app = Flask(__name__)
app.debug = True 
app.config['SECRET_KEY'] = 'secret key!'

class LocationForm(Form):
    lat = StringField('Enter a location latitude: (Ann Arbor - 42.2808° N)')
    lng = StringField('Enter a location longitude: Ann Arbor - 83.7430° W)')
    submit = SubmitField('Submit')

@app.route('/')
def hello_world():
	response = make_response("This is Nate Wellek's Midterm")
	response.set_cookie("symbol", "Stock Market data")
	return response

@app.route('/map')
def image():
	return render_template('maps.html')		

@app.route('/locSearch')
def search():
	form = LocationForm()
	return render_template('locSearch.html', form = form)	

@app.route('/tweets-for-loc', methods = ["POST"])
def search_result():
	lat = request.form.get('lat')
	lng = request.form.get('lng')
	# twitter search
	lst_tweets = api.search(geocode=lat+","+lng+",100km")
	return render_template('nearbytweets.html', lst = lst_tweets)

@app.route('/user/<scren_name>')
def user(scren_name):
	tweets = api.user_timeline(scren_name)
	return render_template('tweetlist.html', Scren_name = scren_name, Tweets = tweets)	

@app.errorhandler(404)
def fouronefour(e):
	return render_template("404.html")

@app.errorhandler(405)
def fouronefive(e):
	return render_template("405.html")	

if __name__ == '__main__':
	app.run()