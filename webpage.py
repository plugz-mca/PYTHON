
import urllib2          #module imported

web_address=raw_input("enter website address:")
response = urllib2.urlopen("http://"+web_address)           #open the URL
print response.info()
html = response.read()
page_source = response.read()
