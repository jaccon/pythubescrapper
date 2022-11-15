# -*- coding: utf-8 -*-

# Packages
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

csvSeparator = "; "
extractionFile = "./grid.html";

urls = 'IgrejaBatistaUnidadoBrás'

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/c/{}/videos?view=0&sort=p&flow=grid'.format(urls))
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
itens = driver.find_elements(By.ID, "video-title-link") 

htmlTemplate = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title> Grid Extraction </title>
  <style>
    html { 
      font-size: 12px;
      font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif
    }
    body { 
      padding: 1rem; 
    }
    .card {
      background-color: #fff;
      color: #000;
      padding: 1rem;
      /* max-width: 200px; */
      max-height: auto;
    }
    .gridThumb {
      border-radius: 5px 5px;
      width: 95%;
    }
    .cards {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-gap: 1rem;
    }
    @media (min-width: 600px) {
      .cards { grid-template-columns: repeat(2, 1fr); }
    }
    @media (min-width: 900px) {
      .cards { grid-template-columns: repeat(4, 1fr); }
    }
    a {
    text-align: left;
    text-decoration: none !important;
    color: #000;
    font-size: 9px !important;
    font-weight: normal !important;
    }
  </style>
</head>
<body>
  <div class="cards">
    <!--  -->
    
    <!--  -->
"""

fileWrite = open(extractionFile, "a")
fileWrite.write(htmlTemplate)
fileWrite.close()

for item in itens:
  
    videoTitle = item.get_attribute("aria-label")
    videoLink = item.get_attribute("href")
    url = videoLink
    parsed = url.split("?v=")
    videoId = parsed[1]
    videoThumbnail = "https://img.youtube.com/vi/" +videoId+ "/0.jpg"
    
    htmlCard = """
    <div class="card">
    <a href="""""+videoLink+"""" target="_blank">
      <img src="""""+ videoThumbnail +""" alt="title" class="gridThumb" />
      <h2 class="gridTitle"> 
       """""+ videoTitle + """
      </h2>
    </a>
    </div>
    """
    
    fileWrite = open(extractionFile, "a")
    fileWrite.write(htmlCard)
    fileWrite.close()
    
htmlTemplate = """
    </div>
  </body>
</html>
"""

fileWrite = open(extractionFile, "a")
fileWrite.write(htmlTemplate)
fileWrite.close()