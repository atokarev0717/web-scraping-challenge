from flask import Flask, render_template, redirect
from pymongo import MongoClient
import scrape_mars

app = Flask(__name__)

# Use pymongo to set up mongo connection
mongo_url = "mongodb://localhost:27017"
client = MongoClient(mongo_url)
db = client.mars_db

@app.route("/")
def index():
    mars_scrape = db.mars_data.find_one()
    return render_template("index.html", mars_scrape=mars_scrape)


@app.route("/scrape")
def scraper():
    mars_scrape = db.mars_data
    mars_data_scraped = scrape_mars.scrape()
    mars_scrape.update({}, mars_data_scraped, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

