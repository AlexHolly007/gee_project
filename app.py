from flask import Flask, request, render_template, jsonify
from ee_script import create_image
import json, requests, os
from datetime import datetime, timedelta
from flask_cors import CORS
from io import BytesIO
from PIL import Image
import base64


app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return


@app.route('/getTimelapse', methods=['GET', 'OPTIONS'])
def timelapse():

    if request.method == 'OPTIONS':
        response = jsonify(message='CORS preflight request successful')
        print("GOT THE PREFLIGHT REQUEST")
        return response


    lon = request.args.get('lon')
    lat = request.args.get('lat')
    miles = request.args.get('miles')
    result = []
    for i in range(5):#39
        if i == 27 or i == 28:
            continue
        start = datetime(1985+i,1,2)
        end = datetime(1986+i,1,1)
        image = create_image(start_date=start,end_date=end,long=lon,lat=lat,miles=miles,count=i)
        
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        image_data = base64.b64encode(buffered.getvalue()).decode('utf-8')
        result.append({'image': image_data})

    response = jsonify(result)
    return response



if __name__ == '__main__': 
    app.run(debug=True, port=60061)
