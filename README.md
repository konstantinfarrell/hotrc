# hotrc

hotrc is a nice little script that lets you add or remove an alias to/from your `.bashrc` file.

## Install

Clone this repo into a local directory, and install.

    git clone https://github.com/konstantinfarrell/hotrc.git
    cd hotrc
    python setup.py install

## Run

When you run initially, you will be prompted for the location of your `.bashrc` file.
Any active, absolute path to a bash configuration file will suffice.

The script can be run with 3 arguments. either `new`, `remove`, or 'list'.
The first two can optionally be followed by the `[key]`, `[value]` pair you would like to define.

    hotrc new
    hotrc new home 'cd /home'

If you do not supply a `[key]`, `[value]` pair as arguments you will be prompted.
