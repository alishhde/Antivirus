### Acknowledgement: The main idea of this Module adopted 
# from https://github.com/Ming-Shu/How-to-detect-USB-plug-in-on-Windows-using-Python 
# and I changed it for better

import os
import string
import  time
from ctypes import windll

class DeviceDetector():
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
         return "USB Detector"
    
    def get_driveStatus(self):
        devices = []
        # The GetLogicalDrives function retrieves a bitmask representing the currently available disk drives.
        record_deviceBit = windll.kernel32.GetLogicalDrives() 
                                                            
        for label in string.ascii_uppercase: # The uppercase letters 'A-Z'
            if record_deviceBit & 1:
                devices.append(label)
            record_deviceBit >>= 1
        return devices

    def newDeviceDetector(self):
            original = set(self.get_driveStatus())
            print ('Detecting...')
            time.sleep(3)
            add_device =  set(self.get_driveStatus()) - original
            subt_device = original - set(self.get_driveStatus())

            if (len(add_device)):
                print ("There were %d"% (len(add_device)))
                for drive in add_device:
                    print ("The drives added: %s." % (drive))
                    return list(drive)
            elif(len(subt_device)):
                print ("There were %d"% (len(subt_device)))
                for drive in subt_device:
                    print ("The drives remove: %s." % (drive))
                    return list(drive)
            return []