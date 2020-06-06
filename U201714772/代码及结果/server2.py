import  boto3
import  sys

if __name__ == "__main__":
    s3 = boto3.resource('s3', endpoint_url = "http://127.0.0.1:9000")
    bucket = s3.Bucket('test1')
    for object in bucket.objects.all():
        print(object.key)
