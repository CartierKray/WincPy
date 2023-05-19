# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line
 
import os
import shutil
import zipfile

# 1
base_path = os.getcwd()
cache_path = os.path.join(base_path,"files", "cache")
data_path = os.path.join(base_path, "data.zip")

def clean_cache():
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
    os.mkdir(cache_path)
clean_cache()




# 2
def cache_zip(zip_file_path, cache_dir_path):
    # Clean the cache directory
    if os.path.exists(cache_dir_path):
        shutil.rmtree(cache_dir_path)
    os.mkdir(cache_dir_path)
    
    # Extract the zip file into the cache directory
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)
    
    print("Zip file extracted successfully.")

zip_file_path = os.path.join(base_path, "files", "data.zip")
cache_dir_path = os.path.join(base_path, "files", "cache")

cache_zip(zip_file_path, cache_dir_path)




# 3
def cached_files():
    file_list = []
    for root, dirs, files in os.walk(cache_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_list.append(file_path)

    return file_list

cache_dir_path = os.path.join(base_path, "files", "cache")
cache_files = cached_files()
print(cache_files)




# 4
def find_password(cached_files):
    for file in cached_files:
        with open(file) as files:
            for line in files:
                if "password" in line:
                    split = line.split()
                    password = [x for x in split if 'password' in x]
                    return split[1]

if __name__ == "__main__":
    print([x for x in os.listdir() if os.path.isdir(x)])
    clean_cache()
    cache_zip(zip_file_path, cache_dir_path)
    cached_files()

    