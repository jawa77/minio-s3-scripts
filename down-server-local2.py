import os
import subprocess

# Endpoint file paths provided with double backslashes for escaping
file_paths = [
  "list/your/files",
  "",
  "/fold/a.txt"
]


# Folder name for downloaded files
download_folder = 'adition'

# Function to download the file using scp
def download_file(remote_path, local_path):
    try:
        cmd = f'scp username@domain.com:"/home/server_folder_location/domain.com{escaped_remote_path}" {local_path}'
        subprocess.run(cmd, shell=True, check=True)
        print(f"Downloaded: {local_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading file: {local_path}. Error: {e}")

# Ensure the download folder exists
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    print(f"Created folder: {download_folder}")

# Download the files
for path in file_paths:
    local_file_name = os.path.basename(path).replace('\\ ', '_').replace('\\&', '_').replace('\\(', '_').replace('\\)', '_')
    local_file_path = os.path.join(download_folder, local_file_name)
    download_file(path, local_file_path)

print("Files downloaded and organized into the folder 'advanceb2'.")
