# Exercise 1 - Downloading files.

Download the file and unzip the file.

## Set up
1. Change directories at the command line to be inside the exercise-1 folder `cd exercise-1`
2. There is a file called `main.py` in the `exercise-1` directory
3. Create Virtual-Enviroment 
```
python3 -m venv .venv #create virtual enviroment

source .venv/bin/activate # activate the virtual enviroment
```
3. Install required-package in requirement.txt : 
```
pip install requirement.txt
```

## Solution 
1. Check if the download_dir was exist or not, if not, create a download_dir
2. loop the url in list download_uris for checking if url is valid or not
3. down load the valid url
4. split out the filename from the uri, so the file keeps its original filename.
5. use zipfile to unzip the zipfile, then delete the zip file
