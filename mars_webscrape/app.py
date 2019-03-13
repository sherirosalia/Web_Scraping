from flask import Flask, render_template, redirect
#?------>
# from flask.ext.pymongo import PyMongo
from flask_pymongo import PyMongo
import scrape_mars
import os

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#app.config[‘MONGO_DBNAME’] = ‘mytestdb’
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info")

@app.route("/")
def index():
    # Find one record of data from the mongo database
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# Route that will trigger the scrape function
@app.route("/scrape")

def scrape():
   mars = mongo.db.mars
   #mongo.db.mars.update({“id”: 1}, {“$set: mars_info”}, upsert = True)
   #mars = mongo.db.mars
   mars_info = scrape_mars.scrape()
   mars.update({}, mars_info, upsert=True)

   return "Scraped successfully!"

   #return redirect(“/”, code=302)
   #return redirect(“http://localhost:5000/“, code=302)
   #return redirect(“http://127.0.0.1:5000/“)

if __name__ == "__main__":
   #app.run()
   app.run(debug=True)