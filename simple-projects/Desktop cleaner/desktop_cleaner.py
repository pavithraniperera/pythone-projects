import os
import shutil


def create_sub_folder(folderPath, sub_folder_name):
    sub_folder_path = os.path.join(folderPath, sub_folder_name)
    if not os.path.exists(sub_folder_path):
        os.makedirs(sub_folder_path)
    return sub_folder_path


def clean_folder(folderPath):
    for filename in os.listdir(folderPath):
        if os.path.isfile(os.path.join(folderPath, filename)):
            print(os.path.join(folderPath, filename))
            file_extention = filename.split(".")[-1].lower()
            if file_extention:
                sub_folder_name = f"{file_extention.upper()} Files"
                sub_folder_path = create_sub_folder(folderPath, sub_folder_name)
                file_path = os.path.join(folderPath, filename)
                shutil.move(file_path, sub_folder_path)
                print(f"moved {filename} to {sub_folder_name}")


if __name__ == "__main__":
    print("Desktop cleaner script")
    folderPath = "/home/pavithrani/chat"
    if os.path.isdir(folderPath):
        clean_folder(folderPath)
        print("Cleaning complete")
    else:
        print("Invalid folder path. please enter correct folder path")
