from .utils import Browser, Files, URLs
from time import sleep

class main():
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass
    
    def ScanWebsite():
        browser = Browser.SafeBrowse('firefox') # We open firefox as our browser other options:'chrome'/'zope.testbrowser'
        
        #### Run and open google.com in the Tab
        browser.runBrowser()
        browser.startBrowing()
        #### A tab with google.com must be opened till here
        while True:
            if browser.currentURL_is != browser.previousurl:
                print("Current URL is: ", browser.currentURL_is, "\n")
                currenturl = browser.currentURL_is # Here we have the current URL
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