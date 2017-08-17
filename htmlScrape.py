from bs4 import BeautifulSoup
import sys
import re
import csv
import urllib2

def cell_text(cell):
    return " ".join(cell.stripped_strings)
url ="http://apps.fs.fed.us/Evalidator/batcheval.jsp?reptype=State&lat=0&lon=-0&radius=0&snum=Area%20of%20forest%20land,%20in%20acres&sdenom=No%20denominator%20-%20just%20produce%20estimate.&wc=92015&pselected=None&rselected=Forest%20type%20group&cselected=Ownership%20group&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom="
html = urllib2.urlopen(url).read()
soup =BeautifulSoup(html, "html.parser")
output = csv.writer(sys.stdout)

for table in soup.find_all('table'):
   # title=table.find('caption')
    title=table.b
    if(title != None):
        print(title.string.extract())

        for row in table.find_all('tr'):
            col = map(cell_text, row.find_all(re.compile('t[dh]')))
            output.writerow(col)
        output.writerow([])