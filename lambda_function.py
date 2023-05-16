import json,os
from download import download_file
from upload2 import upload_s3

def lambda_handler(event,context):
    
    file = '2021-01-01-0.json.gz'
    download_res = download_file(file)
    bucket = os.environ.get('BUCKET_NAME')
    file_prefix = os.environ.get('FILE_PREFIX')
    #environ = os.environ.get('ENVIRON')
    #os.environ.setdefault('AWS_PROFILE','itvgithub')
    
    
    upload_res = upload_s3(
                      download_res.content,
                      bucket,
                      f'{file_prefix}/{file}'
        )
        
    return upload_res
    