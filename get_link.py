from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")


path_to_chromedriver = '/Users/ryancrenny/Documents/chs/chromedriver' # change path as needed
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

#browser = webdriver.Chrome(options=chrome_options)

def get_song(name):
    url_base="https://www.youtube.com/results?search_query="
    name_l=name.split(" ")
    for value in name_l:
        url_base=url_base+value+"+"
    search_results=url_base[:-1]

    browser.get(search_results)
    html=browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    obj=soup.find("a", {"class": "yt-simple-endpoint style-scope ytd-video-renderer"})
    l1=str(obj).split("href=")
    result=l1[1].split("id")[0][:-2]
    result=result[1:]


    return "youtube.com"+result

def download(url):
    os.system(f"youtube-dl -x --audio-format mp3 \"{url}\"")






