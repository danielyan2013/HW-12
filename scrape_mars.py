from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    news_title, news_p = mars_news(browser)

      results = {
      "title": first_title,
      "paragraph": first_paragraph,
      "image_url": mars_image(browser),
      "weather": mars_weather(browser),
      "facts": mars_facts(),
      "hemispheres": mars_hemis(browser),
    }
    browser.quit()
    return results

def mars_news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    return news_title, news_p

def mars_image(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    browser.click_link_by_partial_text('more info')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    feat_img_url = image_soup.find('figure', class_='lede').a['href']
    feat_img_full_url = f'https://www.jpl.nasa.gov{feat_img_url}'
    return feat_img_full_url

def mars_weather(browser):
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_weather = soup.find('p', class_='TweetTextSize').text
    return mars_weather

def mars_facts():
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df = df[['Mars - Earth Comparison', 'Mars']]
    df.columns = ['Property', 'Mars']
    df.set_index('Property', inplace=True)
    return df.to_html()

def mars_hemis(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemi_texts = []
    links = soup.find_all('h3')

    for hemi in links:
        hemi_texts.append(hemi.text)

    hemisphere_image_urls = []

    for hemi in hemi_texts:
        hemi_dict = {}
        browser.click_link_by_partial_text(hemi)
        hemi_dict["title"] = hemi
        hemi_dict["img_url"] = browser.find_by_text('Sample')['href']
        hemisphere_image_urls.append(hemi_dict)
        pprint(hemisphere_image_urls)
        browser.back()

    return hemisphere_image_urls
