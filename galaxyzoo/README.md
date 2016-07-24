# Galaxy Zoo 

This directory contains some utility methods for acquiring and structuring the [Galaxy Zoo](https://www.galaxyzoo.org) data
from [Kaggle](https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge) which was part of an ML competition run in 2013.

In this directory you will find a config_override json file for entering kaggle credentials and specifying the urls you wish to
download data from. Simply fill your credentials and urls in and remove the _override from the name. Run the code:
`python galaxy_zoo_utils.py` code to download the datasets to a directory called `datasets` relative to the current directory.

