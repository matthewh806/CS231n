import os
import json
import download_kaggle_data

def load_galaxy_zoo(root_dir):
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
    kaggle_data = data["kaggle"]
    username = kaggle_data["username"]
    password = kaggle_data["password"]
    urls = kaggle_data["data_urls"]

    for url in urls:
        # Check if file / dir name exists 
        name = os.path.splitext(url.split("/")[-1])[0] 
        path = os.path.join(root_dir, name)
        if not os.path.exists(path):
            print "%s path not found, downloading data..." % path
            download_kaggle_data.download_data(url, username,
                                           password, root_dir)
    print "All required data downloaded"

if __name__ == "__main__":
    load_galaxy_zoo('datasets')
