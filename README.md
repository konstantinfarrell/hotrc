[![Build Status](https://travis-ci.org/konstantinfarrell/hotrc.svg?branch=master)](https://travis-ci.org/konstantinfarrell/hotrc)
[![Coverage Status](https://coveralls.io/repos/github/konstantinfarrell/hotrc/badge.png?branch=master)](https://coveralls.io/github/konstantinfarrell/hotrc?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/konstantinfarrell/hotrc/badge.svg?branch=master)](https://coveralls.io/github/konstantinfarrell/hotrc?branch=master)

# HotRC

hotrc ("hot-are-see") is a python based command line utility that lets you add or remove an alias to/from your `.bashrc` file
without having to jump around between text editors, or restart the shell. It is advantageous to `alias` as the changes to `.bashrc`
are persistent and don't rely on the user session.

## Install

Clone this repo into a local directory, and install.

    git clone https://github.com/konstantinfarrell/hotrc.git ~/.hotrc
    cd ~/.hotrc
    make

## Run

When you run initially, you will be prompted for the location of your `.bashrc` file.
Any active, absolute path to a bash configuration file will work.

## API

Syntax is structured as follows

    hotrc command arg1 'arg2'

arg2 should be put in quotes if the alias command contains a space.

**Commands**

- `add`: Takes 2 arguments, `key` and `value` and constructs a `.bashrc` alias for them.
    If arguments arent provided, the user will be prompted for them.
- `list`: Takes no arguments. Lists all current aliases in the `.bashrc`
- `new`: Same as add.
- `remove`: Takes 1 or 2 arguments: `key`, or `key` and `value`, and removes the corresponding alias from the `.bashrc` file.
- `reset`: Deletes old entry and prompts the user for the path to the `.bashrc` file. Only absolute paths are accepted.
- `rm`: Same as remove.
