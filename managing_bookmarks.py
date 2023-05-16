from datetime import datetime as dt
from datetime import timedelta as td
import requests,boto3,os
from botocore.errorfactory import ClientError

os.environ.setdefault('AWS_PROFILE','itvgithub')

s3_client = boto3.client('s3')

bookmark_contents = '2021-01-02-0.json.gz'

try:
    bookmark_file = s3_client.get_object(Bucket='itv-github-gx',Key='sandbox')
    
    print(bookmark_file['Body'].read().decode('utf-8'))
    
    except ClientError as e:
        
        if e.response['Error']['Code'] == 'NoSuchKey':
            prev_file = baseline_file
        else:
            raise
        
    dt_part = next_file.split('.')[0]
    next_file = f"{dt.strftime(dt.strptime(dt_part,'%Y-%M-%d-%H')+td(hours=1),'%Y-%M-%d-%-H')}"
    res = requests.get(f'https://data.gharchive.org/{next_file}')
    
    if res.status_code != 200:
        break
    
    print(f'The status_code for {next_file} is {res.status_code}')
    
    bookmark_contents = next_file
    
    '''s3_client.put_object(
        Bucket = 'itv-github-gx',
        Key = 'sandbox',
        Body = bookmark_contents.encode('utf-8'))
        
except:
    
    print('except '+baseline_file)