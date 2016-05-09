#!/usr/bin/python

import sys

class HotRC(object):
    ALIASES = dict()
    ALL_ALIASES = dict()
    BASHRC = ''

    def __init__(self, *args, **kwargs):
        self.ALL_ALIASES = self.get_aliases()

    def create_alias(self, key, value):
        if value[0] is not "'" or value[0] is not '"':
            value = '"' + value + '"'
        try:
            if self.ALL_ALIASES[key] is not None:
                self.ALL_ALIASES[key] = value
                self.ALIASES[key] = value
        except KeyError:
            self.ALL_ALIASES[key] = value
            self.ALIASES[key] = value
            self.write_to_bashrc(key, value)

    def write_to_bashrc(self, key, value):
        command = "alias "+str(key)+"="+str(value)
        with open(self.BASHRC, 'r') as file:
            contents = file.read()
            if "# HOTRC" not in contents:
                file.close()
                contents = open(self.BASHRC, 'a')
                contents.write("\n# HOTRC\n")
                contents.close()
                contents = open(self.BASHRC, 'r').read()
        contents = contents.split('\n')
        d_range = self.get_index_range_of_definitions()
        contents.insert(d_range[1], command)
        contents = '\n'.join(contents)
        bashrc = open(self.BASHRC, 'w')
        bashrc.write(contents)

    def get_index_range_of_definitions(self):
        bashrc = open(self.BASHRC, 'r').read()
        bashrc = bashrc.split('\n')
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

    def get_aliases(self):
        try:
            info = open('info', 'r')
            bashrc = info.readline()
            self.BASHRC = bashrc
            info.close()
        except IOError as e:
            info = open('info','w')
            print("Bashrc not found. Specify path to bashrc.")
            bashrc = str(raw_input('BASHRC_PATH: '))
            self.BASHRC = bashrc
            info.write(bashrc)
            info.close()

        bashrc = open(bashrc, 'r')
        contents = bashrc.read().split('\n')

        aliases = dict()
        for line in contents:
            if line.startswith('alias'):
                line = line.replace('alias ', '')
                definition = line.split('=')
                aliases[definition[0]] = definition[1]
        return aliases


h = HotRC()
print(h.get_index_range_of_definitions())
args = sys.argv[1:]
if args[0] == 'new':
    if len(args) > 1:
        h.create_alias(args[1], args[2])
    else:
        key = str(raw_input("Alias Key: "))
        value = str(raw_input("Alias Value: "))
        h.create_alias(key, value)

