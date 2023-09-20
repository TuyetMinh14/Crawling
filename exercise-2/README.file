# Exercise 2 - WebScraping and File Downloading with Python.

Extend upon the idea of downloading files from HTTP sources with Python, but add a twist.

I will have to "web scrap" a HTML page looking for a date, and identifying the correct file to build a URL with which I can download said file.

## Set up
1. Change directories at the command line to be inside the exercise-1 folder `cd exercise-2`
2. There is a file called `main.py` in the `exercise-2` directory
3. Create a virtual enviroment for this excersie
```
```
```
python3 -m venv .venv #create virtual enviroment

source .venv/bin/activate # activate the virtual enviroment
```
```
```
4.. Install required-package in requirement.txt : 
```pip install requirement.txt```

## Solution 
I download a file of weather data from a government website. files that are sitting at the following specified location:

https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/

1. Check if the url is valid
2. Use BeautifulSoup to parse the HTML content of the webpage:
3. Find the HTML table element on the webpage
4. Find all the HTML `tr` (table row) elements within the table
5. Iterate through each row in the table, find all the HTML `td` (table data/cell) elements within the row
6. Get the `href` attribute from the `a` element to construct the download URL
7. Read the CSV data from the download URL into a Pandas DataFrame, extract the maximum value from the 'HourlyDryBulbTemperature' column of the DataFrame and append it to the `max_value` list
8. Print the maximum value from the `max_value` list:
