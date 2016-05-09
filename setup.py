import os
from setuptools import setup, find_packages


version = '0.0.2'

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
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ]
)
