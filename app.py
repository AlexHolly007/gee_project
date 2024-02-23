from flask import Flask, request, render_template, jsonify
from ee_script import create_image
import json, requests
import os
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def main():
    return


@app.route('/getTimelapse', methods=['GET'])
def timelapse():
    lon = request.args.get('lon')
    lat = request.args.get('lat')
    miles = request.args.get('miles')
    for i in range(39):
        if i == 27 or i == 28:
            continue
        start = datetime(1985+i,1,2)
        end = datetime(1986+i,1,1)
        create_image(start_date=start,end_date=end,long=lon,lat=lat,miles=miles,count=i)
        print("start:",start)
    return



if __name__ == '__main__': 
    app.run(debug=True, port=60061)
