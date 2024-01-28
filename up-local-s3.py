from minio import Minio
from minio.error import S3Error
import os
from datetime import timedelta
from urllib.parse import quote
import mimetypes

class MinioImageUploader:
    def __init__(self, endpoint, access_key, secret_key):
        # Initialize minio client with an endpoint and access/secret keys.
        self.client = Minio(endpoint,
                            access_key=access_key,
                            secret_key=secret_key,
                            secure=True)  # Change to True for HTTPS
    
    def get_image_url(self, bucket_name, object_name, expires=timedelta(days=1)):
        try:
            # Generate a presigned URL for the object.
            presigned_url = self.client.presigned_get_object(bucket_name, object_name, expires)
            return presigned_url
        except S3Error as exc:
            print("Error occurred while generating URL: ", exc)
            return None
        

    def upload_directory(self, bucket_name, folder_path, directory_path):
        # Ensure the bucket exists
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)

        uploaded_files_urls = []  # List to store URLs

        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            if os.path.isfile(file_path):
                object_name = f"{folder_path}/{file_name}"
                content_type = mimetypes.guess_type(file_path)[0] or 'application/octet-stream'
                try:
                    # Upload the file
                    self.client.fput_object(bucket_name, object_name, file_path, content_type=content_type)
                    # print(f"File {file_path} is successfully uploaded as {object_name}")

                    # Generate and store the URL
                    url = self.get_image_url(bucket_name, object_name)
                    if url:
                        uploaded_files_urls.append(url)

                except S3Error as exc:
                    print("Error occurred: ", exc)

        return uploaded_files_urls

# Usage example
uploader = MinioImageUploader('s3.domain.com', 'minioUSERNAME', 'password')
image_url = uploader.upload_directory("bucketname", "folderName_inside_bucket", "/home/jawa/data/folder")
for url in image_url:
    base_url = url.split('?')[0]
    print(base_url)
    print('\n')
