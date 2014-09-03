import urllib
from bs4 import BeautifulSoup

f = open('test.xml')
xml = f.read()  
soup = BeautifulSoup(xml)  
for node in soup.findAll('node'):  
    print "Node : "+node.string  
    print "Attr1 : "+node['attr1']