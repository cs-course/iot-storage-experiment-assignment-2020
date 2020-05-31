import boto3
import sys

if __name__ == "__main__":
    s3 = boto3.resource('s3',endpoint_url="http://127.0.0.1:9000")
    bucket = sys.argv[1]
    filepath = sys.argv[2]
    key = sys.argv[3]
    data = open(filepath,'rb').read()
    print(s3.Bucket(bucket).put_object(Key = key, Body = data))
    


