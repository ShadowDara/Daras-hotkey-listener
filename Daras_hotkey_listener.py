import os
import sys
import configparser
import subprocess
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text
from time import sleep

import watch_hotkey

console = Console()

# Variablen
cfg_file_name = 'config.ini'
cfg_file_content = """# config file for Easy Hotkey Listener by Shadowdara
[hotkeys]
hotkey1 = strg+t
hotkey2 = ctrl+shift+w

[hotkey1]
run = sta.cmd

[hotkey2]
run = start msedge
"""

# Funktionen
def create_config(path):
    """Erstellt eine neue Konfigurationsdatei mit Hotkeys und Aktionen."""
    try:
        with open(path, 'wt', encoding='UTF-8') as cfg_file:
            cfg_file.write(cfg_file_content)
        console.print("[bold green]Config file successfully created![/bold green]")

    except OSError as e:
        console.print(f'[bold red]Error while creating the file! {e}[/bold red]')

def load_hotkeys(path):
    """Lädt Hotkeys aus der Konfigurationsdatei."""
    hotkeys = []
    try:
        config = configparser.ConfigParser()
        config.read(path)

        console.print(f"[bold cyan]Config sections:[/bold cyan] {config.sections()}")

        # Hotkeys aus der Konfigurationsdatei lesen
        if 'hotkeys' in config:
            for key, value in config.items('hotkeys'):
                hotkeys.append((key, value))
        else:
            console.print("[bold yellow]No 'hotkeys' section found in the config file.[/bold yellow]")

    except Exception as e:
        console.print(f"[bold red]Error loading hotkeys from config file: {e}[/bold red]")

    return hotkeys

def display_loaded_hotkeys(hotkeys):
    """Zeigt alle geladenen Hotkeys zu Beginn an."""
    if hotkeys:
        table = Table(title="Loaded Hotkeys", border_style="blue")
        table.add_column("Hotkey Name", style="bold yellow")
        table.add_column("Hotkey Combination", style="bold green")

        for hotkey_name, hotkey_combination in hotkeys:
            table.add_row(hotkey_name, hotkey_combination)

        console.print(table)
    else:
        console.print("[bold red]No hotkeys found in the config file.[/bold red]")

def get_config_path():
    """Gibt den Pfad zur Konfigurationsdatei im Unterordner des EXE-Namens zurück."""
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    exe_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]

    config_folder = os.path.join(base_path, exe_name)

    if not os.path.exists(config_folder):
        os.makedirs(config_folder)

    return os.path.join(config_folder, cfg_file_name)

def main():
    config_file_path = get_config_path()

    error_shown = False
    config_loaded = False

    while not config_loaded:
        try:
            with open(config_file_path, 'r', encoding='UTF-8') as cfg_file:
                console.print("[bold green]Config file found![/bold green]")

                config_loaded = True

        except FileNotFoundError as e:
            if error_shown:
                console.print("[bold red]Error: This does not work as intended! Please report the error on GitHub![/bold red]")
                input('[bold red]Press Enter to exit...[/bold red]')
                sys.exit(1)
            else:
                console.print(f"[bold red]Error: {e} -> Config file not found! Creating a new one now...[/bold red]")
                create_config(config_file_path)
                error_shown = True

    hotkeys = load_hotkeys(config_file_path)

    display_loaded_hotkeys(hotkeys)

    watch_hotkey.main(hotkeys, config_file_path)

if __name__ == '__main__':
    console.print("[bold cyan]Easy Hotkey Listener in Python by Shadowdara[/bold cyan]\n")

    main()
