#!/usr/bin/env python

import argparse
import os
import sys
import subprocess


class HotRC(object):

    ALIASES = dict()
    BASHRC = ''

    def __init__(self, *args, **kwargs):
        if 'bashrc' in kwargs:
            self.BASHRC = kwargs.pop('bashrc')
        self.ALIASES = self.get_aliases()

    def get_info(self, info_file=None):
        """
        Parse the info file for `.bashrc` location
        or prompt the user for input.
        """
        if info_file is None:
            info_file = '{}/info'.format(
                    os.path.dirname(__file__))  # pragma: no cover
        try:
            with open(info_file, 'r') as info:
                self.BASHRC = info.readline()
        except IOError as e:    # pragma: no cover
            with open(info_file, 'w') as info:  # pragma: no cover
                print("Bashrc not found. Specify path to bashrc.")  # pragma: no cover
                bashrc = str(input('BASHRC_PATH: '))    # pragma: no cover
                self.BASHRC = bashrc    # pragma: no cover
                info.write(bashrc)      # pragma: no cover

    def get_aliases(self, info_file=None):
        """
        Read all the aliases from the `.bashrc` file
        """
        # Get .bashrc location and read file contents.
        if self.BASHRC == '':
            self.get_info(info_file=info_file)
        contents = self.read_bashrc().split('\n')
        aliases = dict()
        for line in contents:
            if line.startswith('alias'):
                # Parse out all the lines beginning with 'alias'
                # and return them in a dictionary.
                line = line.replace('alias ', '')
                definition = line.split('=', 1)
                aliases[definition[0]] = definition[1]

        return aliases

    def create_alias(self, key, value):
        """
        Create a new alias and write it out to the `.bashrc` file
        """
        if value[0] is not "'" or value[0] is not '"':
            value = '"' + value + '"'
        try:
            if self.ALIASES[key] is not None:
                self.ALIASES[key] = value
        except KeyError:
            self.ALIASES[key] = value
            self.write_to_bashrc(key, value)

    def read_bashrc(self):
        """
        Read the entire `.bashrc` file.
        """
        contents = None
        with open(self.BASHRC, 'r') as rc:
            contents = rc.read()
        return contents

    def remove_alias(self, key):
        """
        Remove an alias from the `.bashrc` file if it exists.
        """

        bashrc = self.read_bashrc().split('\n')
        command = "alias "+str(key)+"="
        for line in bashrc:
            if command in line:
                del bashrc[bashrc.index(line)]
        bashrc = '\n'.join(bashrc)
        with open(self.BASHRC, 'w') as f:
            f.write(bashrc)
        script = '{}/unalias.sh'.format(os.path.dirname(__file__))
        subprocess.Popen([script, key],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         shell=False)

    def write_to_bashrc(self, key, value):
        """
        Format and write the key-value pair to the
        `.bashrc` file.
        """
        # Construct the bash command
        command = "alias "+str(key)+"="+str(value)
        with open(self.BASHRC, 'r') as file:
            contents = file.read()
            if "# HOTRC" not in contents:
                # Add the delimiting line if it's not already
                # in the `.bashrc` file.
                file.close()
                contents = open(self.BASHRC, 'a')
                contents.write("\n# HOTRC\n")
                contents.close()
                contents = self.read_bashrc()
        # Now insert the alias after the last line
        # of the HOTRC section.
        contents = contents.split('\n')
        d_range = self.get_index_range_of_definitions()
        contents.insert(d_range[1], command)
        contents = '\n'.join(contents)
        with open(self.BASHRC, 'w') as bashrc:
            bashrc.write(contents)

    def get_index_range_of_definitions(self):
        """
        Return the index of the `.bashrc` file where the
        HOTRC definitions begin and end.
        """
        bashrc = self.read_bashrc().split('\n')
        start = None
        end = None
        for line in bashrc:
            if line.startswith('# HOTRC'):
                start = bashrc.index(line)
                end = bashrc[start:].index('') + start
        if start:
            return (start, end)
        else:
            start = len(bashrc)
            end = len(bashrc)
        return (start, end)

def description():
    """Description for command line interface"""
    return ''

def start(args=None, rcfile=None):
    """ Controls the command line interface for hotrc """

    parser = argparse.ArgumentParser(description=description())
    subparsers = parser.add_subparsers()

    new_parser = subparsers.add_parser('new')
    new_parser.set_defaults(which='new')
    new_parser.add_argument('alias_key', type=str, help='Alias Key')
    new_parser.add_argument('alias_value', type=str, help='Alias Value')

    remove_parser = subparsers.add_parser('remove')
    remove_parser.set_defaults(which='remove')
    remove_parser.add_argument('alias_key', type=str, help='Alias Key')

    list_parser = subparsers.add_parser('list')
    list_parser.set_defaults(which='list')

    reset_parser = subparsers.add_parser('reset')
    reset_parser.set_defaults(which='reset')

    parsed_args = parser.parse_args(args)

    if rcfile is not None:
        h = HotRC(bashrc=rcfile)
    else:
        h = HotRC()  # pragma: no cover

    # Case 1: Create a new alias.
    if parsed_args.which == 'new':
        h.create_alias(parsed_args.alias_key, parsed_args.alias_value)
    # Case 2: Remove an old alias.
    elif parsed_args.which == 'remove':
        h.remove_alias(parsed_args.alias_key)
    # Case 3: List all defined aliases.
    elif parsed_args.which == 'list': # pragma: no cover
        print("\nAll Aliases")
        print("Key\tValue")
        print("===\t=====\n")
        for key, value in h.ALIASES.items():  # pragma: no cover
            s = key + '\t' + value      # pragma: no cover
            print(s)
        print('')
    # Case 4: Reset the bashrc file.
    elif parsed_args.which == 'reset': # pragma: no cover
        os.remove(os.path.dirname(__file__)+'/info')  # pragma: no cover
        h.get_info()                    # pragma: no cover


if __name__ == "__main__":
    start()
