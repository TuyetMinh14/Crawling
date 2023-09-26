import boto3
import os
import pandas as pd 
import json

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
            for file in files:
                yield os.path.join(root, file)

def main():
    # your code here
    abpath = ""
    os.chdir(abpath)
    for file_path in list_files(abpath):
        if file_path.split('.')[-1] == "json":
            try:
                os.chdir(file_path)
                with open(file_path.split("/")[-1],'r') as file:
                    data = json.load(file)
                    df = pd.json_normalize(data)
                df.to_csv(file_path.split('.')[-1].replace('json','csv'))
            except:
                print(f"Error processing {file_path}")
    pass


if __name__ == "__main__":
    main()