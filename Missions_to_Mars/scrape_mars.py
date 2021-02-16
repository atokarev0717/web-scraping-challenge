# Dependencies
import pandas as pd
import requests
import time
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'

    browser.visit(url)
    time.sleep(1)
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, "html.parser")

    # getting list of 5 most recent tiles
    titles = []
    for i in range (1,6):
        titles.append(soup.find_all('div', class_="content_title")[i].text)

    # brief paragraph dscription 
    paragraphs = []
    for i in range (0,5):
        paragraphs.append(soup.find_all('div', class_="article_teaser_body")[i].text)


    # visiting the url with images 
    url1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url1)
    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')


    browser.click_link_by_partial_text('McMurdo Crater')
    time.sleep(3)

    browser.click_link_by_partial_text('Download')
    time.sleep(3)
    html1 = browser.html
    image_soup = bs(html1, 'html.parser')

    featured_image_url=image_soup.find_all('img')[0]['src']

    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    time.sleep(1)

    tables = pd.read_html(facts_url)

    facts_df = tables[0]
    facts_df.columns = ['fact', 'value']
    facts_df['fact'] = facts_df['fact'].str.replace(':', '')

    facts_html = facts_df.to_html()

    astrogeology_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astrogeology_url)
    time.sleep(1)

    browser.click_link_by_partial_text('Cerberus')
    html1 = browser.html
    soup = bs(html1, 'html.parser')

    img_url_tail = soup.find_all('img', class_='wide-image')[0]['src']
    img_url_cerberus = f'https://astrogeology.usgs.gov{img_url_tail}'

    title_img_url_cerberus = soup.find_all('h2', class_='title')[0].text

    astrogeology_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astrogeology_url)
    time.sleep(1)

    browser.click_link_by_partial_text('Schiaparelli')
    html1 = browser.html
    soup = bs(html1, 'html.parser')

    img_url_tail = soup.find_all('img', class_='wide-image')[0]['src']
    img_url_schiaparelli = f'https://astrogeology.usgs.gov{img_url_tail}'

    title_img_url_schiaparelli = soup.find_all('h2', class_='title')[0].text

    astrogeology_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astrogeology_url)
    time.sleep(1)

    browser.click_link_by_partial_text('Syrtis')
    html1 = browser.html
    soup = bs(html1, 'html.parser')

    img_url_tail = soup.find_all('img', class_='wide-image')[0]['src']
    img_url_syrtis = f'https://astrogeology.usgs.gov{img_url_tail}'

    title_img_url_syrtis = soup.find_all('h2', class_='title')[0].text


    astrogeology_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astrogeology_url)
    time.sleep(1)

    browser.click_link_by_partial_text('Valles')
    html1 = browser.html
    soup = bs(html1, 'html.parser')

    img_url_tail = soup.find_all('img', class_='wide-image')[0]['src']
    img_url_valles = f'https://astrogeology.usgs.gov{img_url_tail}'

    title_img_url_valles = soup.find_all('h2', class_='title')[0].text

    hemisphere_image_urls=[
        {"title":title_img_url_cerberus,
        "img_url":img_url_cerberus},
        {"title":title_img_url_schiaparelli,
        "img_url":img_url_schiaparelli},
        {"title":title_img_url_syrtis,
        "img_url":img_url_syrtis},
        {"title":title_img_url_valles,
        "img_url":img_url_valles}
    ]


    mars_scrape = {
        "title": titles,
        'paraggraph': paragraphs,
        'featured_image_url': featured_image_url,
        'facts': facts_html,
        'hemisphere':hemisphere_image_urls
    }

    browser.quit()

    return mars_scrape



