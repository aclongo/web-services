# The program will prompt for a URL,
# read the JSON data from that URL using urllib 
# and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file and enter the sum below:

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try: # prompt the user for a url location and read it with urllib
        url = input('Enter location: ')
        js = urllib.request.urlopen(url, context=ctx).read()
        break
    except: # prevent invalid urls from crashing the program
        print('Invalid url. Try again.')
        continue