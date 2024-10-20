import os
import shutil
import time
import random  # For generating random numbers
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Paths
from_dir = "C:/Users/kajal/Downloads"
to_dir = "C:/Users/kajal/Documents/DownloadedFiles"

dir_tree = {
    "Image_files": [".jpg", ".jpeg", ".png"],
    "Video_files": [".mp4", ".mp3", ".mov"],
    "Document_files": [".ppt", ".csv", ".pdf"]
}

# Creating class FileMovementHandler and passing FileSystemEventHandler as a parameter
class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)

        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Downloaded " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                # Check if the directory exists
                if not os.path.exists(path2):
                    print("Making Directory..")
                    os.makedirs(path2)

                # Check if the file with the same name exists in the destination directory
                if os.path.exists(path3):
                    print(f"File {file_name} already exists. Renaming the file.")
                    
                    # Generate a random number and append it to the file name
                    random_num = random.randint(0,100)
                    new_file_name = os.path.splitext(file_name)[0] + "_" + str(random_num) + extension
                    path3 = to_dir + '/' + key + '/' + new_file_name

                print(f"Moving {file_name} to {path3}...")
                shutil.move(path1, path3)
                time.sleep(1)


# Initialize event handler class
event_handler = FileMovementHandler()
observer = Observer()
# Recursive=True to observe the changes in subfolders as well
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
