import requests
import json
import hashlib

class Files():
    def __init__(self, filePath, apikey) -> None:
        self.MainURL = "https://www.virustotal.com/api/v3/files" # main url
        self.ScanFile = filePath # target url
        self.api = apikey


    def __str__(self) -> str:
        return "URL Module"


    def scanUpload(self):
        files = {"file": ("IoTArticle1.pdf", open(self.ScanFile, "rb"), "application/pdf")}
        headers = {
            "accept": "application/json",
            "x-apikey": self.api,
        }
        self.ScanResponse = requests.post(self.MainURL, files=files, headers=headers)
        return self.ScanResponse    


    def report(self):
        HashID = self.hashTheFile()
        reportURL = f"{self.MainURL}/{HashID}"
        print("Link: ", reportURL)
        headers = {
            "accept": "application/json",
            "x-apikey": f"{self.api}"
        }
        self.ReportResponse = requests.get(reportURL, headers=headers)
        return self.ReportResponse # In order to check the response you should use .text


    def hashTheFile(self):
        sha256_hash = hashlib.sha256()
        with open(self.ScanFile,"rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()