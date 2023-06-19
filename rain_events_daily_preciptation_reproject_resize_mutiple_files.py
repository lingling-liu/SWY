from osgeo import gdal 
import os
from pathlib import Path
import pygeoprocessing

directory = "D:/My Drive/World Bank/Pakistan/SWY/inputs/rain_events/Daily_preciptation/"
output = "D:/My Drive/World Bank/Pakistan/SWY/inputs/rain_events/resize/"

ref = "D:\My Drive\World Bank\Pakistan\SWY\inputs\clipPKS_HydCondi_DEM_90mete1r.tif"

vector_mask = "D:\My Drive\World Bank\Pakistan\SWY\inputs\PKS_Adm0_WGS_20kmbuff.shp"
ref_info = pygeoprocessing.get_raster_info(ref)
pixel_size  = ref_info['pixel_size']
bounding_box = ref_info['bounding_box']
print(bounding_box)
print(pixel_size)
pixel_size = [5000,-5000]
projection_wkt = ref_info['projection_wkt']


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(f)
    # checking if it is a file
    if os.path.isfile(f): 
        filename = Path(f).stem
        src = f
        dest = output + filename+"_reproject.tif"
        print(dest)
        print(src)
        pygeoprocessing.geoprocessing.align_and_resize_raster_stack([src], [dest],['near'],pixel_size,bounding_box,target_projection_wkt=projection_wkt)