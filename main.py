import requests
import wget
import os
import zipfile
import pandas as pd
download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    # your code here
    download_dir = "download_dir"
    if not os.path.exists(download_dir):
        try:
            os.mkdir(download_dir)
        except:
            pass
    os.chdir(download_dir)
    for url in download_uris: 
        respone = requests.get(url)
        if respone.status_code == 200:
            zip_file = wget.download(url)
            zf = zipfile.ZipFile(zip_file)
            df = pd.read_csv(zf.open(zipfile.ZipFile.namelist(zf)[0]))
            df.to_csv(zipfile.ZipFile.namelist(zf)[0])
            abs_path = os.path.abspath(zip_file)
            os.remove(abs_path)



if __name__ == "__main__":
    main()