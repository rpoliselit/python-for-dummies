"""
https://seleniumhq.github.io/selenium/docs/api/py/
open a new Firefox browser
load the page at the given URL
and quit browser
"""

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')
browser.quit()
