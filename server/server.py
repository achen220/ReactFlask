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
    #get the string format of the page and parse it into html
    URL = "https://books.toscrape.com/catalogue/page-1.html"
    result = requests.get(URL)
    doc = BeautifulSoup(result.text, "html.parser")
    #find the maxpage so we can interate through them
    maxPage = int(doc.find(class_="current").text.strip().split(' ')[-1])
    #used to store all the infos
    infoStorage = []
    #iterate from first page to the maxpage storing all info into infoStorage
    for i in range(1,maxPage + 1):
      URL = f"https://books.toscrape.com/catalogue/page-{i}.html"
      result = requests.get(URL)
      doc = BeautifulSoup(result.text, "html.parser")
      booksInfo = doc.find_all(class_="product_pod")
      #iterating from all books in a page
      for book in booksInfo:
        info = {}
        title = book.find('h3').contents[0].get('title')
        info['title'] = title
        price = book.find(class_="price_color").text[2:len(book.find(class_="price_color").text)]
        info['price'] = price
        availability = book.find(class_="instock availability").text.strip()
        info['availability'] = availability
        infoStorage.append(info)
      with open('output.html', 'w',encoding = 'utf-8') as file:
        file.write(str(infoStorage))
  return render_template("index.html")

#only run server if this script is being ran in the file its created rather than imported
if __name__ == "__main__":
  app.run(debug=True)