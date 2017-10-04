from urllib.request import urlopen
import boto3
import os
import boto3

def event_handler(event = None, context = None):
    s3_client = boto3.client("s3")
    handle = urlopen(os.getenv("CAMERA_URL"))
    s3_client.upload_fileobj(handle, os.getenv("BUCKET_NAME"),
                                     os.getenv("DESTINATION_FILENAME"),
                                     ExtraArgs={'ACL': 'public-read'})
