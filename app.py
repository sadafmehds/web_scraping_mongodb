from flask import Flask, render_template, jsonify,redirect
from flask_pymongo import PyMongo
import pymongo
import mars_scraper


app=Flask(__name__)

conn='mongodb://localhost:27017/'

client = pymongo.MongoClient(conn)
db=client["mars"]
collection = db["mars_info"]
# db=client.mars
# collection = db.mars_info


@app.route('/')
def index():
    data = collection.find_one()
    return render_template("index.html",data=data)


@app.route('/scrape')
def scraping():
    updated_data=mars_scraper.Scraper()

    collection.insert_one(updated_data)
    return redirect("/",code=302)

if __name__=="__main__":
    app.run(host='127.0.0.1',port=800,debug=True)


# contl shift r