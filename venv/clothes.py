import json
from flask import Flask, render_template, url_for, request, redirect, session, jsonify

#lang = 'es'

app = Flask(__name__)

#@app.route("/fetch_image", methods=["POST"])
#def fetch_image():
    # Retrieve the image from the request
 #   image = request.files["image"].read()
math = 10
@app.route("/") 
def default(): 
    data = {'name': 'John', 'age': math}
    return render_template('user-page.html',data=data)
 
@app.route('/add', methods=['POST'])
def add_numbers():
    a = request.json['a']
    b = request.json['b']
    print(a)

    with open('example.txt', 'w') as file:
        # Write some text to the file
        file.write('Hello, world!\n')
        file.write('This is an example file.\n')

    data = {'name': 'John', 'age': math}
    return render_template('user-page.html',data=data)

@app.route("/test/",methods = ["GET","POST"])
def test(): 
    print
    if request.method == "POST":
        return render_template('user-page.html',data=data)

if __name__ == "__main__":
    app.run(debug=True)
