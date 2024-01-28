from minio import Minio
from minio.error import S3Error

class MinioImageDownloader:
    def __init__(self, endpoint, access_key, secret_key):
        # Initialize minio client with an endpoint and access/secret keys.
        self.client = Minio(endpoint,
                            access_key=access_key,
                            secret_key=secret_key,
                            secure=True)  # Change to True for HTTPS

    def download_bucket(self, bucket_name, local_directory_path):
        # Rest of the download method...

# Usage example
downloader = MinioImageDownloader('s3.domain.com', 'minioUSERNAME', 'password')
downloader.download_bucket("bucketname", "/path/to/local/directory")
