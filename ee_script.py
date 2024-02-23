import ee
from IPython.display import Image
import os
import urllib
from os.path import expanduser
import argparse
from datetime import datetime
import requests
from io import BytesIO
from PIL import Image

# Initialize the Earth Engine API
ee.Authenticate()
ee.Initialize(project='ee-hollya')



def create_image(start_date, end_date, long, lat, miles, count):

    miles = (float(miles)/2)
    deg_long = (float(miles)/55)
    deg_lat = (float(miles)/69)
    lat=float(lat)
    long=float(long)
    count=int(count)

    TL = [long+deg_long, lat-deg_lat]
    TR = [long+deg_long, lat+deg_lat]
    BL = [long-deg_long, lat+deg_lat]
    BR = [long-deg_long, lat-deg_lat]
    roi = ee.Geometry.Polygon(
        [[TL, TR, BL, BR]]
    )


    range_1_start = datetime.strptime("2014-01-01", "%Y-%m-%d")
    range_1_end = datetime.strptime("2021-01-03", "%Y-%m-%d")

    range_2_start = datetime.strptime("2022-01-01", "%Y-%m-%d")
    range_2_end = datetime.strptime("2024-01-03", "%Y-%m-%d")

    range_3_start = datetime.strptime("1985-01-01", "%Y-%m-%d")
    range_3_end = datetime.strptime("2011-01-03", "%Y-%m-%d")

    # Check the date range and perform actions accordingly
    if range_1_start <= start_date <= range_1_end:
        basemap = (
            ee.ImageCollection("LANDSAT/LC08/C02/T1_L2") \
            .filterBounds(roi) \
            .filterDate(start_date, end_date) \
            .filterMetadata("CLOUD_COVER", 'less_than', 1) \
            .mean()
        )
        basemap = basemap.clip(roi)
        visualization = basemap.visualize(bands=["SR_B4", "SR_B3", "SR_B2"], min=0, max=14000, gamma=.4)

    elif range_2_start <= start_date <= range_2_end:
        basemap = (
            ee.ImageCollection("LANDSAT/LC09/C02/T1_L2") \
            .filterBounds(roi) \
            .filterDate(start_date, end_date) \
            .filterMetadata("CLOUD_COVER", 'less_than', 1) \
            .mean()
        )
        basemap = basemap.clip(roi)
        visualization = basemap.visualize(bands=["SR_B4", "SR_B3", "SR_B1"], min=0, max=20000, gamma=0.5)

    elif range_3_start <= start_date <= range_3_end:
        basemap = (
            ee.ImageCollection("LANDSAT/LT05/C02/T1_L2") \
            .filterBounds(roi) \
            .filterDate(start_date, end_date) \
            .filterMetadata("CLOUD_COVER", 'less_than', 1) \
            .mean()
        )
        basemap = basemap.clip(roi)
       
        visualization = basemap.visualize(bands=["SR_B3", "SR_B2", "SR_B1"], min=0, max=15000, gamma=.5)




    L8 = (
        ee.ImageCollection('ECMWF/ERA5/DAILY')
        .filterBounds(roi)
        .select('total_precipitation')
        .filter(ee.Filter.date(start_date, end_date))
        .mean()
    )
    L8 = L8.clip(roi)



    
    #export_task = ee.batch.Export.image.toCloudStorage(
    #    image=visualization,
    #    description='exported_image',
    #    bucket="ee-hollya",
    #    fileNamePrefix=f"Timelapse/image",
    #    region=visualization.geometry().bounds(),
    #    scale=30  # Adjust the scale as needed
    #)
    #export_task.start()

    # Save the image to local machine
    local_image_path = os.path.expanduser(f'Timelapse/output{count}.png')
    
    urllib.request.urlretrieve(
                    visualization.getThumbURL(
                        params={
                            'region': roi.getInfo()['coordinates'],
                            'format': 'png',
                            'dimensions': 512
                        }
                    ),
                    local_image_path
    )

    print(f"Image saved locally at: {local_image_path}")

    url = visualization.getThumbURL(
    params={
        'region': roi.getInfo()['coordinates'],
        'format': 'png',
        'dimensions': 512
    }
    )

    # Make a request to the URL and return image
    response = requests.get(url)
    image_content = BytesIO(response.content)
    return(Image.open(image_content))

if __name__ == "__main__":
    start_date = datetime(2022,1,2)
    end_date = datetime(2023,1,1)
    lat = 40.5853
    long = -105.0844
    miles = 10
    image = create_image(start_date, end_date, long, lat, miles, 100)
    print(image)
    #parser = argparse.ArgumentParser(description="This script runs inference on aois within a .csv file.")
    #parser.add_argument("-d", "--dataset_dir", type=str, required=True, help="Directory containing the hr_dataset, and lr_dataset, in the correct format(see worldstrat github)")
    #args = parser.parse_args()