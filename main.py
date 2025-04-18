import os
import sys
import configparser

import watch_hotkey

# Variablen
cfg_file_name = 'config.ini'
cfg_file_content = """# config file for Easy Hotkey Listener by Shadowdara
[hotkeys]
hotkey1 = ctrl+shift+q
hotkey2 = ctrl+shift+w

[hotkey1]
action = Show message for hotkey1

[hotkey2]
action = Show message for hotkey2
"""

# Funktionen
def create_config(path):
    """Erstellt eine neue Konfigurationsdatei mit Hotkeys und Aktionen."""
    try:
        with open(os.path.join(path, cfg_file_name), 'wt', encoding='UTF-8') as cfg_file:
            cfg_file.write(cfg_file_content)
        print("Config file successfully created!")

    except OSError as e:
        print(f'Error while creating the file! {e}')

def load_hotkeys(path):
    """Lädt Hotkeys aus der Konfigurationsdatei."""
    hotkeys = []
    try:
        config = configparser.ConfigParser()
        config.read(os.path.join(path, cfg_file_name))

        # Debugging-Ausgabe
        print(f"Config sections: {config.sections()}")

        # Hotkeys aus der Konfigurationsdatei lesen
        if 'hotkeys' in config:
            for key, value in config.items('hotkeys'):
                hotkeys.append((key, value))
        else:
            print("No 'hotkeys' section found in the config file.")

    except Exception as e:
        print(f"Error loading hotkeys from config file: {e}")

    return hotkeys

def display_loaded_hotkeys(hotkeys):
    """Zeigt alle geladenen Hotkeys zu Beginn an."""
    if hotkeys:
        print("Loaded hotkeys:")
        for hotkey_name, hotkey_combination in hotkeys:
            print(f"{hotkey_name}: {hotkey_combination}")
    else:
        print("No hotkeys found in the config file.")

# Hauptfunktion
def main(path):
    error_shown = False
    config_loaded = False

    while not config_loaded:
        try:
            # Versuchen, die Konfigurationsdatei zu öffnen
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

    hotkeys = load_hotkeys(path)

    display_loaded_hotkeys(hotkeys)

    watch_hotkey.main(hotkeys, path, cfg_file_name)

# Ausführung starten
if __name__ == '__main__':
    print("Easy Hotkey Listener in Python by Shadowdara\n")

    file_path = os.path.dirname(os.path.abspath(__file__))

    main(file_path)
