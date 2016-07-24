import os
import json
import download_kaggle_data
import csv
from scipy.misc import imread

def load_kaggle_data(file):
    with open(file) as json_data_file:
        data = json.load(json_data_file)
    kaggle_data = data["kaggle"]
    username = kaggle_data["username"]
    password = kaggle_data["password"]
    urls = kaggle_data["data_urls"]
    training_size = kaggle_data["training_size"]
    test_size = kaggle_data["test_size"]

    json_data_file.close()

    return (username, password, urls, training_size, test_size)

def download_galaxy_zoo_data(root_dir):
    
    username, password, urls, _, _ = load_kaggle_data('config.json')
    for url in urls:
        # Check if file / dir name exists 
        name = os.path.splitext(url.split("/")[-1])[0] 
        path = os.path.join(root_dir, name)
        if not os.path.exists(path):
            print "%s path not found, downloading data..." % path
            download_kaggle_data.download_data(url, username,
                                           password, root_dir)
    print "All required data downloaded"

def load_galaxy_zoo_data(root_dir):
    # Image data
    _, _, _, training_size, test_size = load_kaggle_data('config.json')
    for f in os.listdir(root_dir):
        path = os.path.join(root_dir, f)

        if os.path.isdir(path):
            # We've found image/traning data directory!
            # Should contain a bunch of images
            print path
            num_imgs = len(os.listdir(path))

            if(num_imgs == test_size):
                print "Found test images directory!"
            elif(num_imgs == training_size):
                print "Found training images directory!"
            #for img_file in os.listdir(path):
                # img_path = os.path.join(path, img_file)
                # #img_path relative to root dir
                # img = imread(img_path)

        elif os.path.isfile(path) and path.endswith('csv'):
            # We've found our answers in csv format
            print "Found csv file"
            with open(path, 'rb') as csvfile:
                reader = csv.reader(csvfile)
                training_solutions = list(reader)

            csvfile.close()
    #return (test_data, training_data)

if __name__ == "__main__":
    download_galaxy_zoo_data('datasets')
    load_galaxy_zoo_data('datasets')
