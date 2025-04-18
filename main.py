import os
import sys
import keyboard
import configparser

# Variables
cfg_file_name = 'config.ini'
cfg_file_content = """# config file for Easy Hotkey Listener by Shadowdara
[hotkeys]
hotkey1 = ctrl+shift+q
hotkey2 = ctrl+shift+w
"""

# Functions
def create_config(path):
    """Creates a new config file with hotkeys."""
    try:
        with open(os.path.join(path, cfg_file_name), 'wt', encoding='UTF-8') as cfg_file:
            cfg_file.write(cfg_file_content)
        print("Config file successfully created!")

    except OSError as e:
        print(f'Error while creating the file! {e}')

def load_hotkeys(path):
    """Loads hotkeys from the config file."""
    hotkeys = []
    try:
        config = configparser.ConfigParser()
        config.read(os.path.join(path, cfg_file_name))

        # Read hotkeys from the config
        for key, value in config.items('hotkeys'):
            hotkeys.append((key, value))
    except Exception as e:
        print(f"Error loading hotkeys from config file: {e}")

    return hotkeys

def on_hotkey_pressed(hotkey_name, hotkey_combination):
    """Handle the hotkey press event."""
    print(f"{hotkey_name} pressed: {hotkey_combination}")

def watch_hotkeys(hotkeys):
    """Watch for hotkeys defined in the config file."""
    for hotkey_name, hotkey_combination in hotkeys:
        # Use a direct function reference instead of lambda
        keyboard.add_hotkey(hotkey_combination, on_hotkey_pressed, args=(hotkey_name, hotkey_combination))
    
    print("Watching hotkeys...")
    keyboard.wait('esc')  # Stop the program when 'esc' is pressed

# Main function
def main(path):
    error_shown = False
    config_loaded = False

    while not config_loaded:
        try:
            # Try to open the config file
            with open(os.path.join(path, cfg_file_name), 'r', encoding='UTF-8') as cfg_file:
                print("Config file found!")
                config_loaded = True

        except FileNotFoundError as e:
            if error_shown:
                print("Error: This does not work as intended!\nPlease report the error on GitHub!\n\nExiting now with Exit Code 1!")
                input('...')
                sys.exit(1)
            else:
                print(f"Error: {e} -> Config file not found!\nCreating a new one now...")
                create_config(path)
                error_shown = True

    # Load hotkeys from the config file
    hotkeys = load_hotkeys(path)

    # Now watch hotkeys
    watch_hotkeys(hotkeys)

# Run on execution
if __name__ == '__main__':
    print("Easy Hotkey Listener in Python by Shadowdara\n")

    file_path = os.path.dirname(os.path.abspath(__file__))

    main(file_path)
