#!/usr/bin/env python

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

    def get_info(self):
        """
        Parse the info file for `.bashrc` location
        or prompt the user for input.
        """
        try:
            with open(os.path.dirname(__file__)+'/info', 'r') as info:
                self.BASHRC = info.readline()
        except IOError as e:
            with open(os.path.dirname(__file__)+'/info', 'w') as info:
                print("Bashrc not found. Specify path to bashrc.")
                bashrc = str(input('BASHRC_PATH: '))
                self.BASHRC = bashrc
                info.write(bashrc)

    def get_aliases(self):
        """
        Read all the aliases from the `.bashrc` file
        """
        # Get .bashrc location and read file contents.
        if self.BASHRC == '':
            self.get_info()
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

    def remove_alias(self, key, value=None):
        """
        Remove an alias from the `.bashrc` file if it exists.
        """

        bashrc = self.read_bashrc().split('\n')
        if value is None:
            command = "alias "+str(key)+"="
        else:
            command = "alias "+str(key)+"=\""+str(value)+"\""
        for line in bashrc:
            if command in line:
                del bashrc[bashrc.index(line)]
        bashrc = '\n'.join(bashrc)
        with open(self.BASHRC, 'w') as f:
            f.write(bashrc)
        script = '{}/unalias.sh {}'.format(os.path.dirname(__file__), key)
        subprocess.call([script], shell=True)

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
                if start != len(bashrc):
                    end = bashrc[start:].index('') + start
                else:
                    start = end
        if start:
            return (start, end)
        else:
            start = len(bashrc)
            end = len(bashrc)
        return (start, end)


def start():
    h = HotRC()
    args = sys.argv[1:]
    try:
        # Case 1: Create a new alias.
        if args[0] == 'new' or args[0] == 'add':
            if len(args) == 3:
                h.create_alias(args[1], args[2])
            else:
                key = str(input("Alias Key: "))
                value = str(input("Alias Value: "))
                h.create_alias(key, value)
        # Case 2: Remove an old alias.
        elif args[0] == 'remove' or args[0] == 'rm':
            if len(args) > 1:
                try:
                    h.remove_alias(args[1], args[2])
                except IndexError as e:
                    h.remove_alias(args[1])
            else:
                key = str(input("Alias Key: "))
                value = str(input("Alias Value: "))
                h.remove_alias(key, value)
        # Case 3: List all defined aliases.
        elif args[0] == 'list':
            print("\nAll Aliases")
            print("Key\tValue")
            print("===\t=====\n")
            for key, value in h.ALIASES.items():
                s = key + '\t' + value
                print(s)
            print('')
        # Case 4: Reset the bashrc file.
        elif args[0] == 'reset':
            os.remove(os.path.dirname(__file__)+'/info')
            h.get_info()
    # Case Default: User doesn't add arguments.
    except IndexError as e:
        print('\nERROR: No Arguments.\n\
                Please run with arguments.\n\
                Accepted syntax:\n\
                \n\thotrc new/add [key] [value]\n\
                \thotrc rm/remove [key] [(optional) value]\n\
                \thotrc list\n\
                \thotrc reset\n')


if __name__ == "__main__":
    start()
