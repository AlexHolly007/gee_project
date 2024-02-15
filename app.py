from flask import Flask, request, render_template, jsonify
from ee_script import create_image
import json, requests
import os

app = Flask(__name__)

@app.route("/")
def main():
    return


@app.route("/request_timelapse")
def timelapse():
    
    return



if __name__ == '__main__': 
    app.run(debug=True, port=60061)
