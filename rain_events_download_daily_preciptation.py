import os
import requests
import gzip

# URL of the folder containing the files
url = "https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/tifs/p05/2020/"

# Directory to download the files to
download_dir = "D:/My Drive/World Bank/Pakistan/SWY/inputs/rain_events/Daily_preciptation/"

# Make sure the download directory exists
os.makedirs(download_dir, exist_ok=True)

# Make a request to the URL to get the list of files
response = requests.get(url)
# print(response.status_code)
# print(response.content)

# Parse the HTML content of the response to get the filenames
filenames = []
for line in response.content.decode().splitlines():
    if "href" in line and 'tif.gz' in line:
        print(line)
        filenames.append(line.split('"')[11])
        print(filenames)

# Download each file
for filename in filenames:
    file_url = url + filename
    file_path = os.path.join(download_dir, filename[:-3])
    print(file_path)
    with open(file_path, "wb") as f:
        response = requests.get(file_url)
        f.write(gzip.decompress(response.content))