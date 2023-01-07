from src import BrowserGenerator, Files, URLs
from time import sleep
import os.path
import os 

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

    def ScanFiles(self, FilesPATH='DocToScan', MAX_SIZE=(5, 'MB')):

        ### Reading the Asked Directory for any files and folders
        folders = []
        files = []
        for entry in os.scandir(FilesPATH):
            if entry.is_dir():
                folders.append(entry.path)
            elif entry.is_file():
                files.append(entry.path)
        print('Folders:')
        for i in range(len(folders)):
            print("\t", folders[i])
            sleep(.05)
        print('Files:')
        for i in range(len(files)):
            print("\t", files[i])
            sleep(.05)
        ### Reading the Asked Directory for any files and folders
        

        ### Size Calculation for every file
        ConversionDictionary = {'byte': 1, 'kb': 1024, 'mb':1024**2, 'gb':1024**3, 'tb':1024**4}
        maxsize = MAX_SIZE[0] * ConversionDictionary[MAX_SIZE[1].lower()]
        for filepath in files:
            # Get the size of the file
            file_size = float(os.path.getsize(f'{filepath}'))
            for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
                if file_size < 1024.0:
                    file_size = (float("%3.1f" % file_size), x)
                    break
                file_size /= 1024.0
            # print(file_size)

            ## Ignoring files greater than 5 MG (Default Value)
            filesize = int(file_size[0]) * ConversionDictionary[file_size[1].lower()]
            if maxsize < filesize:
                # Ignore
                print(f'This {filepath} file Ignored!')
                ...
            else:
                # break
                # Scan the File
                fileObject = Files.Files(f'{filepath}', '51bd951cd29384782a40f883531b182a06adb725331ea8c38b7b1f00e45826ca')
                
                ### Scan the file
                print(f"Scanning {filepath} File....")
                ScanResponse = fileObject.scanUpload()
                ScanResponseText = ScanResponse.text # Turn response to text in order to show in output
                print(ScanResponseText)
                print("Scanning File finished!", "\n")

                ### Report the scanned file
                print("Reporting!")
                print(fileObject.report().text)
                print("Reported!", "\n")



if __name__ == '__main__':
    mainObject = main()
    # mainObject.ScanWebsite()
    mainObject.ScanFiles(FilesPATH='DocToScan', MAX_SIZE=(1.2, 'MB'))