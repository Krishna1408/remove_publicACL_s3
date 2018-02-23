# remove_publicACL_s3
## Remove public ACL of S3 bucket via a lambda job in AWS

Steps:
1. Create a lambda job in aws for any region of your choice. For scripting language use python 3.6
2. Once lambda is created copy paste the code from main.py to your lambda.
3. create a enviornment variable named "s3_bucket_name" and enter all the s3 buckets names (separated by comma )for which public ACL should be removed. 
```YAML
     Example:
     s3_bucket)name = bucket1,bucket2,bucket3
```
4. Run the lambda.
