import ee
from IPython.display import Image
import os
import urllib
from os.path import expanduser

# This is a test to see that my commits are being sent to the main branch - Cam

# Initialize the Earth Engine API
ee.Authenticate()
ee.Initialize(project='ee-hollya')

# Define your region of interest (ROI)
# Replace the coordinates with the geometry of your ROI
roi = ee.Geometry.Polygon(
    [[[-105.023104228107,40.49671745990021], [-105.023104228107,40.62452341627386], [-105.19751218709138,40.62452341627386], [-105.19751218709138,40.49671745990021]]]
)

# Define the date range
start_date = '2020-01-01'
end_date = '2021-01-01'

# Create a Landsat 8 image collection and apply filters
L8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA") \
    .filterBounds(roi) \
    .filterDate(start_date, end_date) \
    .filterMetadata("CLOUD_COVER", 'less_than', 1) \
    .mean()

# Clip the image to the ROI
L8_clip = L8.clip(roi)

# Display the image
visualization = L8_clip.visualize(bands=["B4", "B3", "B2"], min=0, max=0.3, gamma=1.4)
Image(url=visualization.getThumbURL())

# Save the image to local machine
local_image_path = os.path.expanduser('output.png')
visualization.getThumbURL(params={'region': roi.getInfo()['coordinates'], 'format': 'png', 'dimensions': 512})
urllib.request.urlretrieve(visualization.getThumbURL(params={'region': roi.getInfo()['coordinates'], 'format': 'png', 'dimensions': 512}),
                           local_image_path)

print(f"Image saved locally at: {local_image_path}")
