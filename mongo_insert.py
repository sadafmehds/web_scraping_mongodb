import pymongo
import mars_scraper

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.mars
collection = db.mars_info

data=mars_scraper.Scraper()

collection.insert(data)