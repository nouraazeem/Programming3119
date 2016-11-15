"""
Class 9 

List, Tuple, Dictionary

"""

test3= ['a',1,('b',2)]
"""in order to just get the 'b' from the statement you can do the following:"""

print(test3[2][0])


using open()
handle=open(filename,mode)

-returns a handle use to manipulate the filename
-filename is a string
-mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file 

f_handle= open('mbox.txt', 'r')
print(f_handle)

open
read
write 
close
"""
"""
f_handle= open('mbox.txt', 'r')
print(f_handle)

stuff= 'Hello \n World!'
print(stuff)

stuff= 'X\nY'
print(stuff)

print(len(stuff))


xfile = open('mbox-short.txt')

for cheese in xfile:
	print(cheese) 



fhand = open('mbox.txt', 'r')
count=0
for line in fhand:
	count = count + 1
print('Line Count:', count)


fhand = open('mbox-short.txt')
inp= fhand.read()
print(len(inp))
print(inp[:20])

fhand= open('mbox-short.txt')
for line in fhand:
	line=line.rstrip()
	if line.startswith('From:'):
		print(line)

fhand= open('mbox-short.txt')
for line in fhand:
	line=line.rstrip()
	if not line.startswith("From:"):
		continue
	print(line)

fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not '@uct.ac.za' in line:
		continue
	print(line)



tel={"Rachel":2301,"Adam":3431,"Brett":2565}
for k in sorted(tel.keys()):
	print(tel[k],end=",")




"""

Web crawling

1. Check Web Info Structure

open web browser
"""

from urllib.request import urlopen
imdb_top_250 = "http://www.imdb.com/chart/top" 
page = urlopen(imdb_top_250)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "html.parser") 
print(soup.prettify()) 
soup.tables = soup.find_all('table')
len(soup.tables) 
movie_table = soup.find_all('table', class_='chart full-width')
len(movie_table) 
print(movie_table)
print(type(movie_table))
movie_tbody = movie_table[0].find_all('tbody', class_='lister-list') 
movie_tr = movie_tbody[0].find_all('tr')
print(len(movie_tr)) 
























