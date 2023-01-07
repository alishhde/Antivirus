from splinter import Browser
from time import sleep

class SafeBrowse():
    def __init__(self, browser) -> None:
        self.browser = Browser(browser) # Run the browser

    def __str__(self) -> str:
        return f"You are working wth {self.browser} "

    def currentURL_is(self):
        # (self.browser.url)
        return self.browser.url
    
    def startBrowing(self):
        self.previousurl = 'https://www.google.com/'
        self.browser.visit(self.previousurl)

    def reloadCurrentPage(self):
        self.browser.reload()

