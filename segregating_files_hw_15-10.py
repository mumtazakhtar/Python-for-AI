import os
import shutil

# Defining the source folder
source_folder = os.path.expanduser('~/Downlaods') #tilde (~) in file paths to the full path of the user's home directory.

# Defining a dict for different file types
file_folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt','.pptx', '.doc'],
    'Audio': ['.mp3']
}

# creating folders
def create_folder_if_doesnot_exist(folder):
    if not os.path.exists(folder):
        os.mkdirs(folder)

def move_file(file_path,destination_folder):
    if not os.path.exists(destination_folder):
        os.mkdirs(destination_folder)

    file_name = os.path.basename(file_path)
    shutil.move(file_path, os.path.join(destination_folder,file_name))
    print(f'Moved {file_name} to {destination_folder}')

# Organize the files by their type in different folders
def organize_files_by_type(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)

        if os.path.isdir(file_path):
            continue

        name,extension = os.path.splitext(file_name) 

        for folder_name, file_extensions in file_folders.items():
            if extension.lower() in file_extensions:
                destination_folder = os.path.join(folder,folder_name)
                move_file(file_path, destination_folder)
                moved = True
                break
    
if __name__ == "__main__":
    print(f'organizing files in {source_folder}')
    organize_files_by_type(source_folder)
    print("Organized the files by their file type")
