
#import dependencies
from bs4 import BeautifulSoup
import pymongo
import requests
import time
import pandas as pd
from splinter import Browser
from selenium import webdriver


#splinter browser for mac
def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

#define "program module(?)"" to be imported into app.py later
def scrape():
    #from above
    browser = init_browser()
    #dictionary for data
    mars_info = {}

    #first website to visit for data source for mars_info
    url = 'https://mars.nasa.gov/news/'
    #use splinter to open 
    browser.visit(url)

    #BeautifulSoup website object assigned variable, convert to html with BS4
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #optional:
    #print html & id classes for title and paragraph
    #print(soup.prettify())

    #Latest Mars News:
    #check for title
    soup.find_all('div', class_='content_title', limit=2)

    #check for paragraph
    soup.find_all('div', class_= 'rollover_description_inner', limit=2)

    news_title = soup.find('div', class_= 'content_title').find('a').text
    print(news_title)

    #extract paragraph object, assign variable

    news_par = soup.find('div', class_= 'rollover_description_inner').text
    print(news_par)

    #add data to dictionary
    mars_info["news_title"]= news_title
    mars_info["news_paragraph"]= news_par

    #optional:  
    #print(mars_info)


    #Featured Image from JPL Mars Space Images

    #splinter, visit url
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)

    #navigate to the button and click on text "full image"
    browser.click_link_by_id('full_image')
    #give it some time to load
    time.sleep(2)
    
    #clik on second link to retrieve full image
    browser.click_link_by_partial_text('more info')
    #load time
    time.sleep(2)

    #scrape into soup using class 'lede'
    jpl_html = browser.html
    jpl_soup = BeautifulSoup(jpl_html, 'html.parser')
    link = jpl_soup.find('figure', class_='lede').a['href']
    link

    #save image to variable "featured_image_url"
    base_url = 'https://www.jpl.nasa.gov/'
    featured_image_url = base_url + link
    mars_info["featured_image_url"]=featured_image_url

    #optional:
    #print(mars_info)


    #Mars Weather (twitter sentiment) 
    #splinter, visit
    sentiment_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(sentiment_url)

    #use same variable, just reassign new info
    sentiment_html = browser.html
    
    #scrape with soup
    sentiment_soup = BeautifulSoup(sentiment_html, 'html.parser')
    #assign variable to dictionary
    mars_weather = sentiment_soup.find("p", class_= "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    #optional:
    # print(mars_weather)

    #add to dictionary
    mars_info["mars_weather"]= mars_weather

    #optional:
    #print(mars_info)

    #Mars Facts Table
    #site
    url_mars_facts = 'https://space-facts.com/mars/'

    #parse site 
    mars_facts_table = pd.read_html(url_mars_facts)
    mars_facts_table[0]

    #optional:
    #type(mars_facts_table)

    #dataframe
    mars_facts_df = mars_facts_table[0]
    mars_facts_df.columns = ['Labels','Values']
    mars_facts_df

    #optional:
    #type(mars_facts_df)

    # convert to html, so we can make a table
    mars_facts_html = mars_facts_df.to_html(classes='table', header = False, index = False)
    mars_facts_html
    mars_facts_html.replace('\n', '')



    #optional:
    # print(mars_facts_html)

    #optional:
    # type(mars_facts_html)

    #add to dictionary
    mars_info["mars_facts_table"]= mars_facts_html
    browser.quit()
    return mars_info

    #optional:
    # mars_info


