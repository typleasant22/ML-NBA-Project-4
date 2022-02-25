# app.py

from flask import Flask, request , jsonify , render_template , redirect , url_for
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy 
import scrape_gambling
import pymongo
import HelperFunctions

url = "https://www.teamrankings.com/nba/trends/win_trends/"
url2 = "https://www.teamrankings.com/nba/trends/win_trends/?range=yearly_2020_2021"
url3 = "https://www.teamrankings.com/nba/trends/win_trends/?range=yearly_2019_2020"
url4 = "https://www.teamrankings.com/nba/trends/win_trends/?range=yearly_since_2018_2019"


# Crate flask
app = Flask(__name__)

# /calculations path:

# Win/Losses - determines number of wins, losses, and ties
# Win Percentage - percentage of time a team has won
# Previous Odds - 
# Margin of Victory (Average) - avg margin of victory

# Figuring out if it will be useful to rename and manipulate data here for a table? To get the results?
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), index=True)

# Home Page of website
@app.route('/')
def home():
	return render_template('index.html')

@app.route("/")
def index():

   # Find one record of data from the dataset
    gambling_dict = mongo.db.gambling_dict.find_one()

    # Return template and data
    return render_template("index.html", gambling_info = gambling_dict)

@app.route("/scrape")
def scrape():
    gambling_dict = mongo.db.gambling_dict

    # Run the scrape function
    gambling_data = scrape_gambling.scrape_info()

    # Update the Mongo database using update and upsert = True
    gambling_dict.update({}, gambling_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
    
# Route to calculate win-loss record
@app.route('/calculations/CalculateWinLoss', methods =['GET'])
def CalculateWinLoss():
 params = request.args['win_loss']
    params = params.split(',')
    win1,loss1 = (int(i) for i in params)
    win_loss = HelperFunctions.CalculateWinLoss(win1,loss1)
    return {"value": win_loss}

# Route to calculate Win percentage record

@app.route('/calculations/winpercentage', methods=['GET'])
def winpercentage():
    params = request.args
    if params['format'] == ':
        winpercentage = int(params['winpercentage'])
        resulting_percentage = HelperFunctions.(odds)
    else:
        winpercentage = float(params[''])
        resulting_percentage = HelperFunctions.(odds)
    return {"value": winpercentage}

# Route to calculate previous odds record
@app.route('/calculations/previousodds', methods=['GET'])
def previousodds():
    params = request.args
    if params['format'] == '':
        odds = int(params[''])
        new_odds = (previousodds)
    else:
        odds = float(params[''])
        new_odds = n(odds)
    return {"value":new_odds}

# Route to calculate Margin of Victory
@app.route('/calculations/marginofvictory', methods=['GET'])
def marginofvictory():
    params = request.args
    if params['format'] == '':
        marginofvictory = int(params[''])
        new_mov = .(odds)
    else:
        marginofvictory = float(params['marginofvictory'])
        new_mov = (odds)
    return {"value":new_odds}

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/"
mongo = PyMongo(app)

if __name__ == "__main__":
    app.run(debug=True)




# Questions I need answered:
# what math is being done to the variables?
# the HTML route Sarah is building
# which .py files do I need
# the if/else paths