import os
import keyboard
import configparser

def execute_action_for_hotkey(path, hotkey_name, cfg_file_name):
    """Führt die Aktion aus, die in der entsprechenden Sektion für den Hotkey definiert ist."""
    config = configparser.ConfigParser()
    config.read(os.path.join(path, cfg_file_name))

    if hotkey_name in config:
        action = config.get(hotkey_name, 'action', fallback=None)
        if action:
            print(f"Action for {hotkey_name}: {action}")
        else:
            print(f"No action defined for {hotkey_name}")
    else:
        print(f"No section found for {hotkey_name}")

def on_hotkey_pressed(hotkey_name, hotkey_combination, path, cfg_file_name):
    """Verarbeitet den Hotkey-Druck und führt die entsprechende Aktion aus."""
    print(f"{hotkey_name} pressed: {hotkey_combination}")
    execute_action_for_hotkey(path, hotkey_name, cfg_file_name)

def main(hotkeys, path, cfg_file_name):
    """Überwacht die definierten Hotkeys."""
    for hotkey_name, hotkey_combination in hotkeys:
        # Funktion für den Hotkey-Druck registrieren
        keyboard.add_hotkey(hotkey_combination, on_hotkey_pressed, args=(hotkey_name, hotkey_combination, path, cfg_file_name))
    
    print("Watching hotkeys...")
    keyboard.wait('esc')
