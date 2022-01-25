from bs4 import BeautifulSoup
import csv
from html.parser import HTMLParser
import os

def makeReadable(soup, newFilename):
    newFile = open(newFilename, "w+")
    newFile.write(soup.prettify())
    return newFile

file = open('original.htm', "r+")
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
csvwriter.writerow(divisionQueue.pop(0))
for data in scores:
    if data.previous.previous == "Day 2" or not "Day" in data.previous.previous: # close, perhaps check previous elements for patterns
        csvwriter.writerow(divisionQueue.pop(0))
    for row in data.contents[numRows:]:
        fields = []
        for field in row.contents:
            fields.append(field.text)
        csvwriter.writerow(fields)
        if(numRows == 0):
            numRows += 1
        
   