import boto3
import os

def lambda_handler(event, context):
    # Create an S3 client
    s3 = boto3.client('s3')
    #Fetch the list of buckets from lambda enviornment variable
    buckets_list = os.environ['s3_bucket_name']

    for bucket in buckets_list.split(','):
        print("\nSetting the private permissions only for bucket: ", bucket)
        response = s3.put_bucket_acl(
            ACL='private',
            Bucket=bucket
        )
        result = s3.get_bucket_acl(Bucket=bucket)
        print("the new permissions for bucket {0} is {1}".format(bucket, result['Grants']))






