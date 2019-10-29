"""
https://seleniumhq.github.io/selenium/docs/api/py/
Selenium WebDriver is often used as a basis for testing web applications.
"""

import unittest # unit testing framework
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
