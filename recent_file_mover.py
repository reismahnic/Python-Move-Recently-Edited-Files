import shutil
import os
import datetime as dt

#List the source folder and destination folder
source = 'C:\Users\Reis\Desktop\Folder A'
destination = 'C:\Users\Reis\Desktop\Folder B'

#Define the current time and the time period we want to look back at
now = dt.datetime.now()
before = now - dt.timedelta(hours=24)

#Print the list of file names
files = os.listdir(source)

for root,dirs,files in os.walk('C:\Users\Reis\Desktop\Folder A'):  
    for file_name in files:
        path = os.path.join(root,file_name)
        st = os.stat(path)    
        mod_time = dt.datetime.fromtimestamp(st.st_mtime)
        if mod_time > before:
            #Move all files in Folder A to Folder B
            shutil.move(os.path.join(root, file_name), destination)
