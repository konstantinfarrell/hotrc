import os
import sys
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstall(install):
    def run(self):
        install.run(self)
        path = sys.path[0] + '/hotrc/path.sh'
        sys.path.append(sys.path[0])
        subprocess.call(path, shell=True)


version = '0.1.1'

description = 'A command line tool for managing aliases in your .bashrc file.'
current_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(cur_dir, 'README.md')).read()
except:
    long_description = description

setup(
    name = 'HotRC',
    version = version,
    packages = find_packages(),
    url = 'https://github.com/konstantinfarrell/hotrc',
    license = 'BSD',
    description = description,
    long_description = long_description,
    author = 'Konstantin Farrell',
    author_email = 'konstantinfarrell@gmail.com',
    install_requires = ['setuptools'],
    cmdclass = {'install': PostInstall},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ]
)
