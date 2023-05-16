# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line
 
import os
import shutil

# 1
base_path = os.getcwd()
cache_path = os.path.join(base_path, "cache")
data_path = os.path.join(base_path, "data.zip")

def clean_cache():
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
    os.mkdir("cache") 



