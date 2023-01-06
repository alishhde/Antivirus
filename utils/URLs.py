import requests
import urllib.parse
import json
import base64

class Urls():
    def __init__(self, url, apikey) -> None:
        self.MainURL = "https://www.virustotal.com/api/v3/urls" # main url
        self.ScanURL = url # target url
        self.api = apikey


    def __str__(self) -> str:
        "URL Module"


    def scan(self):
        ParsedURL = urllib.parse.quote(self.ScanURL, safe="") # by default safe skip '/' so we needed to emptied it
        payload = f"url={ParsedURL}"
        headers = {
            "accept": "application/json",
            "x-apikey": f"{self.api}",
            "content-type": "application/x-www-form-urlencoded"
        }
        self.ScanResponse = requests.post(self.MainURL, data=payload, headers=headers)
        return self.ScanResponse # In order to check the response you should use .text


    def rescan(self):
        self.RescanURL = f"{self.MainURL}/{self.id}/analyse"
        headers = {
            "accept": "application/json",
            "x-apikey": f"{self.api}"
        }
        self.ReScanResponse = requests.post(self.RescanURL, headers=headers)
        return self.ReScanResponse # In order to check the response you should use .text


    def report(self, FirstScan=True):
        if FirstScan:
            # First we get the ID from the scan's response output
            self.id = json.loads(self.ScanResponse.text)['data']['id']
        else:
            self.id = json.loads(self.ReScanResponse.text)['data']['id']
        self.id = base64.urlsafe_b64encode("self.id".encode()).decode().strip("=")
        reportURL = f"{self.MainURL}/{self.id}"
        print(reportURL)
        headers = {
            "accept": "application/json",
            "x-apikey": f"{self.api}"
        }
        self.ReportResponse = requests.get(reportURL, headers=headers)
        return self.ReportResponse # In order to check the response you should use .text



########################## Start ##########################
urlObject = Urls('https://www.google.com/', '51bd951cd29384782a40f883531b182a06adb725331ea8c38b7b1f00e45826ca')

print("Scanning....")
ScanResponse = urlObject.scan()
ScanResponseText = ScanResponse.text # Turn response to text in order to show in output
print(ScanResponseText)
print("Scanning finished!", "\n")

# Turn text to json to access the parameteres 
print("Converting to JSON!", "\n")
ScanResponseTextJSON = json.loads(ScanResponseText)
print(ScanResponseTextJSON) 
print(ScanResponseTextJSON['data']['id']) # Access a special data from JSON
print("Converted to JSON!", "\n")


print("Reporting!")
print(urlObject.report().text)
print("Reported!", "\n")


print("Rescanning!")
print(urlObject.rescan().text)
print("Rescan finished!", "\n")