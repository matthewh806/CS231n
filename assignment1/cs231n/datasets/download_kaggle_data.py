import sys
import requests
import zipfile
import StringIO

"""
Download data sets from kaggle via the command line. 

Kaggle requires authentication to access its datasets. Its possible to 
sign up with Facebook / Google etc, this script doesn't support that. 
"""

def download_data(data_urls, username, password, output_dir):

    url_list = [data_url for data_url in data_urls.split(',')]

    if len(url_list) > 1:
        for data_url in url_list:
            download_data(data_url, username, password)

    print "Getting data for url: %s" % data_urls
    kagle_credentials = {'UserName': username, 'Password': password}

    r = requests.get(data_url)
    r = requests.post(r.url, data=kagle_credentials) 

    if r.ok:
        z = zipfile.ZipFile(StringIO.StringIO(r.content))
        z.extractall(output_dir)

def readCommand(args):
    import argparse

    parser = argparse.ArgumentParser(description="Download data sets from \
                                     kaggle")
    parser.add_argument('url', type=str, help='comma delimited list of urls\
                        of data set(s)')
    parser.add_argument('username', type=str, help='kaggle username')
    parser.add_argument('password', type=str, help='kaggle password')
    parser.add_argument('-o', '--output', default='.', type=str, help='output directory to \
                        unzip url contents. Relative to current directory')

    return parser.parse_args()

if __name__ == "__main__":
    print "download_kaggle_data"
    args = readCommand(sys.argv[1:])
    download_data(args.url, args.username, args.password, args.output)        
