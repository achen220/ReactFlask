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
    spotifyURL = "https://open.spotify.com/playlist/1VfBi4EsHizXH7ZkjLuFVy?si=eb3aa52e84874a12&nd=1&dlsi=619f2092a8a04fb1"
    #
    result = requests.get(spotifyURL)
    doc = BeautifulSoup(result.text, "html.parser")
    # open the file in w mode 
    # set encoding to UTF-8 
    with open("output.html", "w", encoding = 'utf-8') as file: 

      # prettify the soup object and convert it into a string 
      file.write(str(doc.prettify())) 
    print(doc.prettify())
  return render_template("index.html")

#only run server if this script is being ran in the file its created rather than imported
if __name__ == "__main__":
  app.run(debug=True)