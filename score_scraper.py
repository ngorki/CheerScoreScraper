from bs4 import BeautifulSoup
import csv
from html.parser import HTMLParser
import requests

def makeReadable(soup, newFilename):
    newFile = open(newFilename, "w+")
    newFile.write(soup.prettify())
    return newFile

def getLevelUrls(url, soup):
    newUrls = []
    levels = soup.find_all("option")
    for level in levels:
        if(url[:-5] + level['value'] != url):
            newUrls.append(url[:-5] + level['value'])
    return newUrls

def writeToCSV(csvwriter, scores, divisionQueue):
    if len(scores) < 3:
        print("No scores available")
    for data in scores:
        if data.previous.previous == "Day 2" or "Day" not in data.previous.previous: # close, perhaps check previous elements for patterns
            csvwriter.writerow(divisionQueue.pop(0))
        for row in data.contents[1:]:
            fields = []
            for field in row.contents:
                fields.append(field.text)
            csvwriter.writerow(fields)

url = "https://tv.varsity.com/results/7361971-2022-spirit-unlimited-battle-at-the-boardwalk-atlantic-city-grand-ntls/31220"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# file = open('original.htm', "r+")
# soup = BeautifulSoup(file.read(), "html.parser")
#file = makeReadable(soup, "updated.htm")

scores = soup.find_all(class_ = "full-content")
# currently, go to third child for tables
# TODO add discerning btwn days 1 and 2

newUrls = getLevelUrls(url, soup)
if len(scores) < 3:
    print("No scores available")

csvfile = open("scores.csv", "w")
csvwriter = csv.writer(csvfile)
csvInit = True

<<<<<<< HEAD
for newUrl in newUrls:
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, "html.parser")
    scores = soup.find_all(class_ = "full-content")
    divisionQueue = scores[2]("h2")
    scores = scores[2]("tbody")
    writeToCSV(csvwriter, scores, divisionQueue)

if(len(scores) < 3):
    divisionQueue = scores[2]("h2")
    scores = scores[2]("tbody")
    numRows = 0

    # TODO Fix printing day 1 and day 2
    csvwriter.writerow(divisionQueue.pop(0)) # print Level
    for data in scores:
        if data.previous.previous == "Day 2" or "Day" not in data.previous.previous: # close, perhaps check previous elements for patterns
            csvwriter.writerow(divisionQueue.pop(0))
        for row in data.contents[numRows:]:
            fields = []
            for field in row.contents:
                fields.append(field.text)
            csvwriter.writerow(fields)
            if(numRows == 0):
                numRows += 1