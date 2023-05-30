"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3


bucket = s3.Bucket('my-bucket')
bucket = s3.Bucket('my-bucket-1')

pulumi.export('bucket_name', bucket.id)
