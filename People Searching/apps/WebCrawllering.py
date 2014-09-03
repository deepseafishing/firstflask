#people's_name searching
import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://people.joins.com/search/Ranking.aspx?jc=06&t=d"

urls = [url] # stack of urls to scrape
visited = [url] # historic record of urls

while len(urls)>0:
    try:
        htmltext = urllib.urlopen(urls[0]).read()
    except:
        print urls[0]
    soup = BeautifulSoup(htmltext)

    urls.pop(0)

    for tag in soup.findAll('img', alt=True):
        print tag['alt']


    '''
        for tag2 in soup.findAll('a', title=True):
            print tag2
            tag['href'] = urlparse.urljoin(url, tag['href'])
            print tag['href']
    '''
    '''
        if url in tag['href'] and tag['href'] not in visited:
            urls.append(tag['href'])
            visited.append(tag['href'])
    '''
#print visited