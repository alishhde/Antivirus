from splinter import Browser
from time import sleep

class SafeBrowse():
    def __init__(self, browser) -> None:
        self.browser = browser

    def __str__(self) -> str:
        return f"You are working wth {self.browser} "

    def runBrowser(self):
        self.browser = Browser(f'{self.browser}')
    
    def currentURL_is(self):
        return self.browser.url
    
    def startBrowing(self):
        self.previousurl = 'http://www.google.com'
        self.browser.visit(self.previousurl)

    def reloadCurrentPage(self):
        self.browser.reload()

