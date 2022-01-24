from bs4 import BeautifulSoup
import csv
from html.parser import HTMLParser

def makeReadable(soup, newFilename):
    newFile = open(newFilename, "w+")
    newFile.write(soup.prettify())
    return newFile


file = open('scream.htm', "r+")
soup = BeautifulSoup(file.read(), "html.parser")
#file = makeReadable(soup, "updated.htm")

scores = soup.find_all(class_ = "full-content")
# currently, go to third child for tables
# TODO add discerning btwn days 1 and 2

days = 1
csvfile = open("scores.csv", "w")
csvwriter = csv.writer(csvfile)
csvInit = True

divisionQueue = scores[2]("h2")
scores = scores[2]("tbody")
numRows = 0

# TODO Fix printing day 1 and day 2
for data in scores:
    csvwriter.writerow(divisionQueue.pop(0))
    for row in data.contents[numRows:]:
        fields = []
        for field in row.contents:
            fields.append(field.text)
        csvwriter.writerow(fields)
        currentDay += 1
        if(numRows == 0):
            csvwriter.writerow(divisionQueue.pop(0))
            currentDay -= 1
            numRows += 1
        
   