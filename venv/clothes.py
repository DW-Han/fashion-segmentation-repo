import json
from flask import Flask, render_template, url_for, request, redirect, session, jsonify

#lang = 'es'

app = Flask(__name__)

#@app.route("/fetch_image", methods=["POST"])
#def fetch_image():
    # Retrieve the image from the request
 #   image = request.files["image"].read()

@app.route("/") 
def default(): 
    return render_template('user-page.html')
 


if __name__ == "__main__":
    app.run(debug=True)
