import ee
from IPython.display import Image
import os
import urllib
from os.path import expanduser
import argparse

# Initialize the Earth Engine API
ee.Authenticate()
ee.Initialize(project='ee-hollya')



def create_image():
    roi = ee.Geometry.Polygon(
        [[[-105.023104228107,40.49671745990021], [-105.023104228107,40.62452341627386], [-105.19751218709138,40.62452341627386], [-105.19751218709138,40.49671745990021]]]
    )

    # Define the date range
    start_date = '2019-07-01'
    end_date = '2020-07-01'

    # Create a Landsat 8 image collection and apply filters
    basemap = (
        ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA") \
        .filterBounds(roi) \
        .filterDate(start_date, end_date) \
        .filterMetadata("CLOUD_COVER", 'less_than', 1) \
        .mean()
    )
    L8 = (
        ee.ImageCollection('ECMWF/ERA5/DAILY')
        .filterBounds(roi)
        .select('total_precipitation')
        .filter(ee.Filter.date(start_date, end_date))
        .mean()
    )
    basemap = basemap.clip(roi)
    L8 = L8.clip(roi)
    visualization = basemap.visualize(bands=["B4", "B3", "B2"], min=0, max=0.3, gamma=1.4)

    #visualization = basemap.visualize(
    #    bands=["B4", "B3", "B2"],
    #    min=0,
    #    max=0.3,
    #    gamma=1.4
    #    ).blend(
    #        L8.visualize(
    #            min=0,
    #            max=0.002,
    #            palette= ['ffffff', '00ffff', '0080ff', 'da00ff', 'ffa400', 'ff0000']
    #        )
    #    )



    
    export_task = ee.batch.Export.image.toCloudStorage(
        image=visualization,
        description='exported_image',
        bucket="ee-hollya",
        fileNamePrefix="image",
        region=visualization.geometry().bounds(),
        scale=30  # Adjust the scale as needed
    )
    export_task.start()

    # Save the image to local machine
    local_image_path = os.path.expanduser('output.png')
    print("TESTING")
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

if __name__ == "__main__":
    create_image()
    #parser = argparse.ArgumentParser(description="This script runs inference on aois within a .csv file.")
    #parser.add_argument("-d", "--dataset_dir", type=str, required=True, help="Directory containing the hr_dataset, and lr_dataset, in the correct format(see worldstrat github)")
    #args = parser.parse_args()