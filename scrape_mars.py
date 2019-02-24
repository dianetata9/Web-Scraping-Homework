from splinter import Browser
from bs4 import BeautifulSoup
import time 
import pandas as pd


def init_browser():
    #pointing to the directory where chromedriver exists
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


# NASA Mars New


def mars_news_function():

    browser = init_browser()

   

    # Set Up for NASA Mars News
    url_Mars_News = "https://mars.nasa.gov/news/"

    browser.visit(url_Mars_News)
    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html,'html.parser')

    