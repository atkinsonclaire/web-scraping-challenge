import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    browser=init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

#Scrape Mars News Site

    url = 'https://redplanetscience.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find_all('div', class_='content_title')
    summary = soup.find_all('div', class_='article_teaser_body')
    return title, summary
    
#Scrape Mars Featured Image Page

    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = soup.find_all('img', class_='headerimage fade-in')
    browser.quit()
    return featured_image_url

#Scrape Mars Facts Table

    url = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(url)
    df=tables[1]
    html_table = df.to_html()
    browser.quit()
    return html_table

#Scrape Mars Hemispheres

    url = 'https://marshemispheres.com'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_images = soup.find_all('img', class_='thumb')
    mars_images

    hemisphere_image_urls = []
    
    links = browser.find_by_css('a.product-item img')
    
    for i in range(len(links)):
        hemisphere = {}
        
        browser.find_by_css('a.product-item img')[i].click()
        
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
        
        hemisphere['title'] = browser.find_by_css('h2.title').text
        
        hemisphere_image_urls.append(hemisphere)
        
        browser.quit()

    return hemisphere_image_urls


