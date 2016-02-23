import object_storage
import os
import time

DATAFILE = os.path.expanduser("~/onedrive/github/Berkeley_W251/googlebooks.csv")
googlefilesize = 1596  

# connect to storage account
sl_storage = object_storage.get_client('SLOS856755-2:SL856755',
                                       'cdc24208f9bb1aff86c22d9474b79b5333c654d96503ae9761979d5eb9650ae8', 
                                       datacenter='dal05')

try:
    sl_storage['week7']['googlebooks3.csv'].create()

except ResponseError:
    print ResponseError
    
try:
    uploadstart = time.time()
    fileUpload = sl_storage['week7']['googlebooks3.csv'].load_from_filename(DATAFILE)
except object_storage.errors.ResponseError:
    print ResponseError

uploadcomplete = time.time()

uploadtime = uploadcomplete - uploadstart
print "Total upload time " + str(uploadtime) + " seconds"
uploadspeed = googlefilesize/uploadtime
print "Upload speed = " + str(uploadspeed) + " MB/sec"