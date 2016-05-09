# Hotrc

Hotrc is a nice little script that lets you add an alias to your .bashrc file.

## Run

The script can be run with 2 arguments. either `new` or `remove`.
These can optionalle be followed by the `[key]`, `[value]` pair you would like to define.

    python hotrc.py new
    python hotrc.py new home 'cd /home'

If you do not supply a `[key]`, `[value]` pair as arguments you will be prompted.
