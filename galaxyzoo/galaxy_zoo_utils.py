import os
import download_kaggle_data

training_images_url = \
    'https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/download/images_training_rev1.zip'
training_solutions_url = \
    'https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/download/training_solutions_rev1.zip'
test_images_url = \
        'https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/download/images_test_rev1.zip'

def load_galaxy_zoo(root_dir):
    training_images_path = os.path.join(root_dir, 'images_training_rev1')
    training_solutions_path = os.path.join(root_dir,
                                           'training_solutions_rev1.csv')
    test_images_path = os.path.join(root_dir, 'images_test_rev1')

    if not os.path.exists(training_images_path):
        print "%s path not found, downloading data..." % training_images_path
        download_kaggle_data.download_data(training_images_url, username,
                                           'password', root_dir)
    if not os.path.exists(training_solutions_path):
        print "%s path not found, downloading data..." % training_solutions_path
        download_kaggle_data.download_data(training_solutions_url,
                                           'username',
                                           'password', root_dir)
    if not os.path.exists(test_images_path):
        print "%s path not found, downloading data..." % test_images_path
        download_kaggle_data.download_data(test_images_url, 'username',
                                           'password', root_dir)

    print "All required data downloaded"

if __name__ == "__main__":
    load_galaxy_zoo('datasets/galaxyzoo')
