import requests

def download_file(file):
    
    res = requests.get(f'https://data.gharchive.org/{file}')
    
    return res
    
res = download_file('2021-01-29-0.json.gz')
print(res.status_code)