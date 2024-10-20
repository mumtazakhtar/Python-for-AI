import os
import shutil


from_dir ="C:/Users/akhta/OneDrive/Desktop/python"
to_dir="C:/Users/akhta/OneDrive/Desktop/python/Downloadedfiles"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension=="":
       continue
    if extension in ['.gif','.png','.jpg','.jpeg']:
        path1= from_dir+ "/"+file_name
        path2=to_dir+"/"+"imagefiles"
        path3=to_dir+"/"+"imagefiles"+"/"+file_name
    
    if os.path.exists(path2):
        print("moving"+file_name+ "...")

        shutil.move(path1,path3)
    else:
        os.mkdir(path2)
        print("moving"+file_name+ "...")
        shutil.move(path1,path3)

###  Assignment: segregate the files into different folders based on file type