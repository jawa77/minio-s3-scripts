import os
import subprocess

# Endpoint file paths provided
file_paths = [
    "/pub/files1/a.txt",
    "..."
    "file location"

]





# Folder distribution as provided

# folder one hold first7 file and fold2 hold next 3
folder_distribution = {
    'folder1': 7, 'folder2': 3, 'folder3': 29, 'folder4': 3, 'folder5': 4,
    'folder6': 12, 'folder7': 14, 'folder8': 8, 'folder9': 7, 'folder10': 6,
    'folder11': 11, 'folder12': 14, 'folder13': 4, 'folder14': 3
}

## Function to escape spaces in the file path
def escape_spaces(path):
    return path.replace(" ", "\\ ")

# Function to download the file using scp
def download_file(remote_path, local_path):
    try:
        escaped_remote_path = escape_spaces(remote_path)
        cmd = f'scp username@domain.com:"/home/server_folder_location/domain.com{escaped_remote_path}" {local_path}'
        subprocess.run(cmd, shell=True, check=True)
        print(f"Downloaded: {local_path}")
    except subprocess.CalledProcessError as e:
        print(f"--------- Error downloading file: {local_path}. Error: ")

# Create the folders and download files into the appropriate folder
folder_limits = list(folder_distribution.values())
folder_names = list(folder_distribution.keys())
folder_index = 0
file_count = 0

for path in file_paths:
    if folder_index >= len(folder_names):
        print("No more folders defined. Exiting.")
        break

    current_folder = folder_names[folder_index]
    
    if not os.path.exists(current_folder):
        os.makedirs(current_folder)
        print(f"Created folder: {current_folder}")

    local_file_path = os.path.join(current_folder, os.path.basename(path).replace(' ', '_'))
    download_file(path, local_file_path)

    file_count += 1
    if file_count >= folder_limits[folder_index]:
        folder_index += 1
        file_count = 0

print("Files downloaded and organized into folders.")