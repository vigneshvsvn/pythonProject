"""
Web Scraping: collecting the data from websites.


"""

import re,urllib.request,pprint



site='https://www.durgasoftonline.com'
response=urllib.request.urlopen(site)          ## return <class 'http.client.HTTPResponse'>
text=response.read()
#print(text)
stext=str(text)
#print(stext)
pattern="[a-zA-Z0-9_.]+[@][a-zA-z]+[.]com"

match=re.findall(pattern,stext)
print(set(match))
