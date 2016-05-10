# hotrc

hotrc is a nice little script that lets you add or remove an alias to/from your `.bashrc` file.

## Run

When you run initially, you will be prompted for the location of your `.bashrc` file.
Any active, absolute path to a bash configuration file will suffice.

The script can be run with 3 arguments. either `new`, `remove`, or 'list'.
The first two can optionally be followed by the `[key]`, `[value]` pair you would like to define.

    python hotrc.py new
    python hotrc.py new home 'cd /home'

If you do not supply a `[key]`, `[value]` pair as arguments you will be prompted.
