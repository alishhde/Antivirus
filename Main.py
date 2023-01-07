from src import BrowserGenerator, Files, URLs
from time import sleep

class main():
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass
    
    def ScanWebsite(self):
        browser = BrowserGenerator.SafeBrowse('firefox') # We run and open firefox as our browser other options:'chrome'/'zope.testbrowser'
        
        #### Open google.com in the Tab
        browser.startBrowing()
        #### A tab with google.com must be opened till here
        while True:
            print("Previous URL was: ", browser.previousurl)
            print("Current URL is: ", browser.currentURL_is(), "\n")
            sleep(2.5)

            if browser.currentURL_is() != browser.previousurl:
                currenturl = browser.currentURL_is() # Here we have the current URL
                browser.previousurl = currenturl 

                ######## Scan the URL and show it in output
                urlObject = URLs.Urls(currenturl, "51bd951cd29384782a40f883531b182a06adb725331ea8c38b7b1f00e45826ca")
                
                ## URL scanning starts here
                print("Scanning....")
                ScanResponse = urlObject.scan()
                ScanResponseText = ScanResponse.text # Turn response to text in order to show in output
                print(ScanResponseText)
                print("Scanning finished!", "\n")
                ## URL scanning finishes here
                ## Getting report information starts here
                print("Reporting!")
                print(urlObject.report().text)
                print("Reported!", "\n")
                ## Getting report information finishes here

                ######## URL scan completed and showed in terminal

if __name__ == '__main__':
    mainObject = main()
    mainObject.ScanWebsite()