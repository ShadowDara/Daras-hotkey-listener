# script written by Shadowdara

import os
import sys
import keyboard
import configparser

# variables
cfg_file_name = 'config.ini'
cfg_file_content = """# config file for Easy Hotkey Listener by Shadowdara
[settings]
"""

# functions
def create_config(path):
    try:
        with open(os.path.join(path, cfg_file_name), 'wt', encoding = 'UTF-8') as cfg_file:
            cfg_file.write(cfg_file_content)
        print("Config file succesfully created!")

    except OSError as e:
        print(f'Error while creating the file! {e}')

def watch_hotkeys():
    pass

# main function
def main(path):
    while True:
        error_shown = False

        try:
            with open(os.path.join(path + cfg_file_name), 'r', encoding = 'UTF-8') as cfg_file:
                print("Config File found!")
                # read the config file
                break

        except NameError as e:
            if error_shown:
                print('Error: This does not work as intend!\Please report the Error to Github!\n\nExiting now with Exit Code 1!')
                input('... ')
                sys.exit(1)

            else:
                print(f'Error: {e} -> Config file not found!\n Creating a new one now!')
                create_config(path)
                error_shown = True
    
    # now watch the hotkeys!

    input()

# run on execution
if __name__ == '__main__':
    print("Easy Hotkey Listener in Python by Shadowdara\n")

    file_path = os.path.dirname(os.path.abspath(__file__))

    main(file_path)
