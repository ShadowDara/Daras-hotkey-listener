# easy-hotkey-listener

a python programm to create your own custom hotkeys easily!

## How

When you run the Programm for the First Time, it will generate a `config.ini`
file, which will look like this

```ini
# config file for Easy Hotkey Listener by Shadowdara
[hotkeys]
hotkey1 = strg+t
hotkey2 = ctrl+shift+w

[hotkey1]
run = sta.cmd

[hotkey2]
run = start msedge
```

Under the section `[hotkeys]`, you can add new hotkeys to the programm,
then create a new section for the hotkey with same name (`[hotkey1]`)
and add your commands which be executed on the hotkey run.

`run =` is equal to a terminal run

Other options will be added soon!

## Logic

I would recommend to use this tool to run another script on a hotkey press
and not save to much data into the `config.ini` file.

## Contribute
feel free to contribute to this Repository
