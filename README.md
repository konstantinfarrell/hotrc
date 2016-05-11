# hotrc

hotrc ("hot-are-see") is a nice little script that lets you add or remove an alias to/from your `.bashrc` file.

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
For example:

    hotrc new
    hotrc new home 'cd /home'

If you do not supply a `[key]`, `[value]` pair as arguments you will be prompted.

## API

Syntax is structured as follows

    hotrc <command> [arg1] [arg2]

*Commands*

- add: Takes 2 arguments, `key` and `value` and constructs a `.bashrc` alias for them.
    If arguments arent provided, the user will be prompted for them.
- list: Takes no arguments. Lists all current aliases in the `.bashrc`
- new: Same as add.
- remove: Takes 1 or 2 arguments: `key`, or `key` and `value`, and removes the corresponding alias from the `.bashrc` file.
- reset: Deletes old entry and prompts the user for the path to the `.bashrc` file. Only absolute paths are accepted.
- rm: Same as remove.
