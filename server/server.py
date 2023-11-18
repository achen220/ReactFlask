from flask import Flask, render_template, request
from flask_cors import CORS
import json

#__name__ determines the location of this file
app = Flask(__name__)
CORS(app)

@app.route("/api",methods=["GET","POST"])
def home():
  if request.method == 'POST':
    request_data = json.loads(request.data.decode('utf-8'))
    print(request_data.get('playlistLink' ))
  return render_template("index.html")

#only run server if this script is being ran in the file its created rather than imported
if __name__ == "__main__":
  app.run(debug=True)