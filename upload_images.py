import boto3
import os

bucket = os.environ["BUCKET_NAME"]

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
    region_name="ap-south-1"
)

folder = "images"

for file in os.listdir(folder):

    path = os.path.join(folder, file)

    print("Uploading", file)

    s3.upload_file(
        path,
        bucket,
        f"images/{file}",
        ExtraArgs={
            "ACL":"public-read"
        }
    )

print("Images Uploaded Successfully")