import os
import subprocess
import keyboard
import configparser
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text
from time import sleep

console = Console()

def execute_action_for_hotkey(path, hotkey_name, cfg_file_name):
    """Führt die Aktion aus, die in der entsprechenden Sektion für den Hotkey definiert ist."""
    config = configparser.ConfigParser()
    config.read(os.path.join(path, cfg_file_name))

    if hotkey_name in config and 'run' in config[hotkey_name]:
        command = config[hotkey_name]['run']
        console.rule(f"[bold green]Hotkey Triggered: [cyan]{hotkey_name}[/cyan][/bold green]")
        console.print(f"[bold yellow]>>[/bold yellow] [white]{command}[/white]")
        try:
            subprocess.Popen(command, shell=True)
        except Exception as e:
            console.print(f"[red]Fehler:[/red] {e}")
    else:
        console.print(f"[red]Keine [run] Anweisung für [bold]{hotkey_name}[/bold] gefunden![/red]")

def on_hotkey_pressed(hotkey_name, hotkey_combination, path, cfg_file_name):
    """Verarbeitet den Hotkey-Druck und führt die entsprechende Aktion aus."""
    console.print(f"\n[bold magenta]{hotkey_name} pressed:[/bold magenta] {hotkey_combination}")
    execute_action_for_hotkey(path, hotkey_name, cfg_file_name)

def main(hotkeys, path, cfg_file_name):
    """Überwacht die definierten Hotkeys."""
    with Progress() as progress:
        task = progress.add_task("[green]Watching hotkeys...", total=len(hotkeys))
        for hotkey_name, hotkey_combination in hotkeys:

            keyboard.add_hotkey(hotkey_combination, on_hotkey_pressed, args=(hotkey_name, hotkey_combination, path, cfg_file_name))
            progress.update(task, advance=1)
        console.print("\n[bold cyan]Watching hotkeys... Press 'esc' to exit.[/bold cyan]")
        keyboard.wait('esc')  # Das Programm stoppen, wenn 'esc' gedrückt wird
