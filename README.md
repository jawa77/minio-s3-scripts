
## Download requirements

```
pip install minio
```


##  Download files from your ** server -----> local  using SCP

#### Use down-server-local.py or down-server-local2.py and replace this cmd

```
scp username@domain.com:"/home/server_folder_location/domain.com{escaped_remote_path}" {local_path}
```


## Upload files ** local ----> minio-s3 

#### Replace below this content in file

``` 
uploader = MinioImageUploader('s3.domain.com', 'minioUSERNAME', 'password')
image_url = uploader.upload_directory("bucketname", "folderName_inside_bucket", "/home/jawa/data/folder")
```


## download bucket of files from ** s3 ----> local

#### use this down-s3-local.py

```
downloader = MinioImageDownloader('s3.domain.com', 'minioUSERNAME', 'password')
downloader.download_bucket("bucketname", "/path/to/local/directory")
```

