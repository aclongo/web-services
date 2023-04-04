# The program will prompt for a URL, 
# read the XML data from that URL using urllib 
# and then parse and extract the comment counts from the XML data, 
# compute the sum of the numbers in the file and enter the sum
#   <comment>
#     <name>Matthias</name>
#     <count>97</count>
#   </comment>
# http://py4e-data.dr-chuck.net/comments_42.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try:
        url = input('Enter location: ')
        xml = urllib.request.urlopen(url, context=ctx).read()
        break
    except:
        print('Invalid url. Try again.')
        continue

print('Retrieving', url)
print('Retrieved', len(xml), 'characters')

tree = ET.fromstring(xml)
lst = tree.findall('comments/comment')
print(lst)
print('Comment count:', len(lst))

sum = 0
for item in lst:
    count = item.find('count').text
    sum += int(count)

print('The sum of all comments is:', sum)
