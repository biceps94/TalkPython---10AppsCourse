import os
import platform
import subprocess


import app6_module


def main():
    print_header()
    folder = get_or_create_output_folder()
    print("Found or created folder: " + folder)
    download_cats(folder)
    display_cats(folder)
    print('hello from main')


def print_header():
    print('-------------------------------')
    print('\t\t CAT FACTORY')
    print('-------------------------------')


def get_or_create_output_folder():
    #base_folder = os.path.dirname(__file__)
    base_folder = os.path.abspath(os.path.dirname(__file__))
    folder = 'cat_pictures'
    # full_path = os.path.abspath(os.path.join('.',folder))
    full_path = os.path.join(base_folder, folder)
    

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f"Creating new directory at {full_path}")
        os.mkdir(full_path)
    return full_path




def download_cats(folder):
    your_cat = app6_module.how_many()
    print('Contacting server to download cats... ')
    cat_count = your_cat
    for i in range(cat_count):
        name = f"lolcat {i + 1}"
        print('Downloading cat: ' + name)
        app6_module.get_cat(folder, name)
    print("Done!")

def display_cats(folder):
    # open folder
    print('Displaying cats in OS wwindow.')
    if platform.system() == 'Dwarwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())




if __name__ == '__main__':
    main()
