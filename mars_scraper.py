

import pandas as pd
import numpy as np
import datetime
import time

import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from flask import Flask, render_template

import pymongo

def Scraper():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')

    print(soup.prettify())



    news_title=soup.find('div',class_='content_title').get_text()
    news_paragraph=soup.find('div',class_='article_teaser_body').get_text()


    news_title

    news_paragraph


    # **JPL FEATURED IMAGE**

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')

    images=soup.footer.find('a',class_='button fancybox')['data-fancybox-href']
    url2='https://www.jpl.nasa.gov'
    actual_url=url2+images
    


    # **MARS WEATHER TWEETS**

    executable_path={'executable_path':'chromedriver.exe'}
    browser=Browser('chrome',**executable_path,headless=False)

    url='https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')


    relevant_tweets=soup.find_all('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

    relevant_tweets

    weather_tweet=relevant_tweets[7].get_text()
    weather_tweet


    # **MARS FACTS**

    url='https://space-facts.com/mars/'
    tables=pd.read_html(url)
    tables


    df=tables[0]
    df


    df=df.rename(columns={0:'Charactristic',1:'Value'})

    df.set_index('Charactristic')

    final_fact_table=df.to_html(classes='Striped-table')
    final_fact_table


    # **MARS HEMISPHERES**


    executable_path={'executable_path':'chromedriver.exe'}
    browser=Browser('chrome',**executable_path,headless=False)

    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')


    titles=[]
    hemi_titles=soup.find_all('h3')

    for i in hemi_titles:
        x=i.get_text()
        titles.append(x)

    titles


    links=[]

    for j in titles:
        browser.visit(url)
        browser.click_link_by_partial_text(j)
        browser.click_link_by_text('Sample')
        html=browser.html
        soup=bs(html,'html.parser')

        link=soup.find('div',class_='downloads').find('a')['href']

        links.append(link)

    links


    # mars_hemis={}
    # for m,k in zip(titles,links):
    #     mars_hemis[m]=k
    mars_hemis=[]
    for m,k in zip(titles,links):
        mars_hemis.append({"title":m,"link":k})


    data={"news_title":news_title,
    "news_paragraph":news_paragraph,
    "actual_url":actual_url,
    "weather_tweet":weather_tweet,
    "final_fact_table":final_fact_table,
    "mars_hemis":mars_hemis}


    # data={"Latest Mars News Headline":news_title,
    # "Latest Mars News":news_paragraph,
    # "Featured Image":image_url,
    # "Latest Mars Weather Update":weather_tweet,
    # "Mars Fun Facts":final_fact_table,
    # "Mars Hemispheres":mars_hemis}

    return data