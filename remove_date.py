import os
import shutil
import time
path=input('path of the folder to sort')
days=30
deleted=0
seconds = time.time() - (days * 24 * 60 * 60)
print(seconds)
if(os.path.exists(path)):
    os.path.join()
    for(root_folder, folders, files in os.walk(path):
        if(seconds>=get_file_or_folder_age(root_folder)):
            os.remove(root_folder)
            deleted+=1