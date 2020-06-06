import  boto3
import  sys

if __name__ == "__main__":
    s3 = boto3.resource('s3', endpoint_url = "http://127.0.0.1:9000")
    bucket = sys.argv[1]
    key = sys.argv[2]
    filepath = sys.argv[3]
    print(bucket, key, filepath)
    with open(filepath, 'rb') as f:
        data = f.read()
    s3.Bucket(bucket).put_object(Key= key, Body= data)
    