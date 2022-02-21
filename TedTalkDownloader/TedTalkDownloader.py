from urllib import request
import requests

from bs4 import BeautifulSoup

import re

import sys

# Exception Handling
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

# url = "https://www.ted.com/talks/li_huei_tsai_are_brain_waves_the_secret_to_treating_alzheimer_s"

# url = "https://www.ted.com/talks/dustin_burke_how_to_fix_broken_supply_chains"

r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")

result = ''

for val in soup.findAll("script"):
    if(re.search("props", str(val))) is not None:
        result = str(val)
        print(f'\n------result----\n{result}\n-------end----\n')

result_mp4 = re.search("(?P<url>https?://[^\s]+.mp4)", result).group("url")
print(f'\n------result----\n{result_mp4}\n-------end----\n')

mp4_url = result_mp4.split('"')[0]

print("Downloading video from ....." + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in ..." + file_name)

r = requests.get(mp4_url)

with open(file_name, 'wb') as f:
    f.write(r.content)

# Alternate method
# urlretrieve(mp4_url, file_name)

print("Download Process finished")
