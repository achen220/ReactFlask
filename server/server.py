from flask import Flask, render_template, request
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import json

#__name__ determines the location of this file
app = Flask(__name__)
CORS(app)

@app.route("/api",methods=["GET","POST"])
def home():
  if request.method == 'POST':
    #get the string format of the spotify playlist link
    #spotifyURL = json.loads(request.data.decode('utf-8')).get('playlistLink')
    URL = "https://books.toscrape.com/"
    #
    result = requests.get(URL)
    doc = BeautifulSoup(result.text, "html.parser")
    booksInfo = doc.find_all(class_="product_pod")
    #print(booksInfo[0].find('h3').contents[0].get('title'))
    infoStorage = []
    for book in booksInfo:
      info = {}
      title = book.find('h3').contents[0].get('title')
      info['title'] = title
      price = book.find(class_="price_color").text[2:len(book.find(class_="price_color").text)]
      info['price'] = price
      availability = book.find(class_="instock availability").text.strip()
      info['availability'] = availability
      infoStorage.append(info)
    print(infoStorage)
  return render_template("index.html")

#only run server if this script is being ran in the file its created rather than imported
if __name__ == "__main__":
  app.run(debug=True)