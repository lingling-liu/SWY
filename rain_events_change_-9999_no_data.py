from osgeo import gdal 
import os
from pathlib import Path

directory = "D:/My Drive/World Bank/Pakistan/SWY/inputs/rain_events/resize"
output = "D:/My Drive/World Bank/Pakistan/SWY/inputs/rain_events/nodata/"

translateoptions = gdal.TranslateOptions(gdal.ParseCommandLine("-ot Float32 -a_nodata -9999 COMPRESS=LZW"))

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f): 
        filename = Path(f).stem
        src = f
        dest = output + filename+"_nodata.tif"
        print(dest)
        print(src)
        ds = gdal.Translate(dest,src,options=translateoptions)