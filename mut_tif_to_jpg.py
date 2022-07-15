# Rasterio
from itertools import product
import rasterio as rio
from rasterio import windows
import numpy
import glob 
import os
from natsort import natsorted



tif_dir = 'F:/IMAGE_CLASSIFICATION/STEP_3/TIF'
tif_lst = natsorted(list(glob.glob(os.path.join(tif_dir, '*.tif'))))
print(tif_lst)


for i in range(0, len(tif_lst)):

    n = i+1
    n=str(n)    
    # Tif to jpg

    #img = image.load_img(img_path)
    #to display RGB
    dataset = rio.open(tif_lst[i])
    data = dataset.read([1,2,3])
    #print(dataset.profile)
    height=dataset.height
    width=dataset.width

    def normalize(x, lower, upper):
        """Normalize an array to a given bound interval"""

        x_max = numpy.max(x)
        x_min = numpy.min(x)

        m = (upper - lower) / (x_max - x_min)
        x_norm = (m * (x - x_min)) + lower

        return x_norm

    # Normalize each band separately
    data_norm = numpy.array([normalize(data[i,:,:], 0, 255) for i in range(data.shape[0])])
    data_rgb = data_norm.astype("uint8")

    outpath="F:/IMAGE_CLASSIFICATION/STEP_3/JPG/" + n + ".jpg"
    data_rgb = data.astype("uint8")
    with rio.open(outpath, 'w',height=height,width=width,dtype='uint8',driver='JPEG',count=3) as outds:
        outds.write(data_rgb)