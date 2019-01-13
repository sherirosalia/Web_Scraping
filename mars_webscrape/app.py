

#import dependencies/libraries

from flask import Flask, render_template, redirect, jsonify
#?------>
# from flask.ext.pymongo import PyMongo 
from flask_pymongo import PyMongo
import scrape_mars
import os

# Create an instance of Flask
app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'mytestdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mytestdb'
mongo = PyMongo(app)
print(mongo.db.testcollection.find_one())

#another way: # scrape function # add this above @app.route from scrape_mars import scrape

@app.route('/')

def index():
	# Find one record of data from the mongo database
    mars = mongo.db.mars.find_one()
    print(mars)
    return render_template('index.html', mars=mars)


# Route that will trigger the scrape function
@app.route('/scrape')
# import scrape function from scrape_mars? 
def scrape():
    
    mars_info = scrape_mars.scrape()
    mongo.db.mars.update({}, mars_info, upsert=True)

    return redirect("http://localhost:5000/", code=302)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
















