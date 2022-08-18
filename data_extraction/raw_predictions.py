import json
import requests

def json_from_api(url,file_name,bucket):
    
    print("running")
    response = requests.request("GET",url)
    raw_json = response.json()
    
    print("information gathered")
    
    with open(f"../data/{file_name}", 'w', encoding="utf-8") as json_file:
    
        json.dump(raw_json, json_file, ensure_ascii=False, indent=4)
        
    print(f"information saved in file data/{file_name}")
    
    
json_from_api('https://www.predictit.org/api/marketdata/all/','predictit_market.json','data-mbfr')
    