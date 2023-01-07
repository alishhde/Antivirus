from src import BrowserGenerator, Files, URLs, USBDetector
from time import sleep
import os.path
import os 

class main():
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass
    
    def runProgram(self):
        devicedetector = USBDetector.DeviceDetector()
        devicedetector.newDeviceDetector()  

        while True:
            # sleep(1)
            print('Running. . . .')
            newDrives = devicedetector.newDeviceDetector()
            if len(newDrives) > 0:
                self.ScanForFilesFolders(FilesPATH=newDrives, Drive=True)
            # self.ScanForFilesFolders()


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

    def ScanForFilesFolders(self, FilesPATH='DocToScan', MAX_SIZE=(5, 'MB'), Drive=False):
        if Drive:
            FilesPATH = f'{FilesPATH[0]}:\\img'
            print("This directory added and must scan", FilesPATH)

        self.files, self.folders = self.fileFolderFinder(FilesPATH) 
        ## self.files consists of a paths to files existing in that given path(Directory), self.folders Directory existing in the given directory 
        print('This is self.files: ', self.files, '\nThis is self.folders: ', self.folders, '\n\n')
        
        ### Size Calculation for every file
        ConversionDictionary = {'byte': 1, 'kb': 1024, 'mb':1024**2, 'gb':1024**3, 'tb':1024**4}
        maxsize = MAX_SIZE[0] * ConversionDictionary[MAX_SIZE[1].lower()]

        def scanFiles():
            for file in self.files:
                # Get the size of the file
                print('We are checking ', file, ' this file.\n')
                file_size = float(os.path.getsize(f'{file}'))
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
                    print(f'This {file} file Ignored!\n')
                    ...
                else:
                    # break
                    # Scan the File
                    fileObject = Files.Files(f'{file}', '51bd951cd29384782a40f883531b182a06adb725331ea8c38b7b1f00e45826ca')
                    
                    ### Scan the file
                    print(f"Scanning '{file}' File....")
                    ScanResponse = fileObject.scanUpload()
                    ScanResponseText = ScanResponse.text # Turn response to text in order to show in output
                    print(ScanResponseText)
                    print("Scanning File finished!", "\n")

                    ### Report the scanned file
                    print("Reporting!")
                    # print(fileObject.report().text)
                    print("Reported!", "\n")
                    
        # def recursionCheckingFolders():
        #     for folder in self.folders:
        #         print("\#\#\#\#\# Looking for folders ...")
        #         self.files, self.folders = self.fileFolderFinder(folder)
        #         print("\#\#\#\#\# Looking for folders DONE.")

        checkFile_flag = True
        CheckFolder_flag = True
        if len(self.files) > 0 and checkFile_flag:
            scanFiles()
            checkFile_flag = False
            print('file finisheddddd\n\n')

        if len(self.folders) > 0:
            for folder in self.folders:
                print(f"We are checking '{folder}' folder!")
                self.ScanForFilesFolders(FilesPATH=folder)
            CheckFolder_flag = False
            print('Folder finisheddddd\n\n')

        if not(CheckFolder_flag):
            print("This directory checked completely!")

                
                                   
        

    def fileFolderFinder(self, FilesPATH):
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
        return files, folders


if __name__ == '__main__':
    mainObject = main()
    # mainObject.ScanWebsite()
    # mainObject.ScanForFilesFolders(FilesPATH='DocToScan', MAX_SIZE=(1.2, 'MB'))
    mainObject.runProgram()