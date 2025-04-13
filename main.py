# script written by Shadowdara

import os
import sys
import keyboard

# functions
def create_config():
    pass

# main function
def main(path):
    file_name = os.path.basename(__file__)

    while True:
        x = 0
        try:
            with open(os.path.join(path, file_name + '.ini'), 'r', encoding = 'UTF-8') as cfg_file:
                break
                # read the config file

        except NameError as e:
            if x == 1:
                print('Error: This does not work as intend!\Please report the Error to Github!\n\nExiting now with Exit Code 1!')
                input('... ')
                sys.exit(1)

            else:
                print(f'Error: {e} -> Config file not found!\n Creating a new one now!')
                create_config()
            x = 1
    
    # now watch the hotkeys!

# run on execution
if __name__ == '__main__':
    print("Easy Hotkey Listener in Python by Shadowdara")

    file_path = os.path.abspath(__file__)

    main(file_path)
