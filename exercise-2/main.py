import requests
import pandas as pd 
from bs4 import BeautifulSoup

url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
def main():
    # your code here
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        if columns and columns[1].text.strip() == '2022-02-07 14:03':
            file_link = columns[0].find('a')
            link_url = file_link.get('href')
            download_url = url + link_url
            df = pd.read_csv(download_url,low_memory=False)
            #csv_file = requests.get(download_url).content
            max_value = [] 
            max_value.append(df['HourlyDryBulbTemperature'].max())
    print(max(max_value))
    
            
    



if __name__ == "__main__":
    main()
