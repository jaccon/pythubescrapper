# Packages
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

csvSeparator = "; "
extractionFile = "./extraction.csv";

urls = 'IgrejaBatistaUnidadoBrás'

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/c/{}/videos?view=0&sort=p&flow=grid'.format(urls))
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
itens = driver.find_elements(By.ID, "video-title-link") 

count = 0

header = "Title" + csvSeparator + " Description" + csvSeparator + "VideoId" + csvSeparator + "Thumbnail" + "\n"

fileWrite = open(extractionFile, "a")
fileWrite.write(header)
fileWrite.close()

for item in itens:
    count = int(count) + 1
    videoTitle = item.get_attribute("aria-label")
    videoLink = item.get_attribute("href")
    url = videoLink
    parsed = url.split("?v=")
    videoId = parsed[1]
    videoThumbnail = "https://img.youtube.com/vi/" +videoId+ "/0.jpg"
    csvString = ((videoTitle + csvSeparator + videoLink + csvSeparator + videoId + csvSeparator + videoThumbnail + "\n"))
    
    print(csvString)
    fileWrite = open(extractionFile, "a")
    fileWrite.write(csvString)
    fileWrite.close()