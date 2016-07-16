import os
import sys
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install


class PostInstall(install):
    def run(self):
        install.run(self)
        subprocess.call(os.path.join(sys.path[0], 'hotrc/reload.sh'))
        path = os.path.join(sys.path[0], 'hotrc/path.sh')
        sys.path.append(sys.path[0])
        subprocess.call(path, shell=True)
        subprocess.call(['source ~/.bashrc'], shell=True)


version = '0.2.1'

description = 'A command line tool for managing aliases in your .bashrc file.'
current_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(current_dir, 'README.md')).read()
except:
    long_description = description

requirements = open('requirements.txt', 'r').read().splitlines()

setup(
    name='HotRC',
    version=version,
    packages=find_packages(),
    url='https://github.com/konstantinfarrell/hotrc',
    license='MIT',
    description=description,
    long_description=long_description,
    author='Konstantin Farrell',
    author_email='konstantinfarrell@gmail.com',
    install_requires=requirements,
    cmdclass={'install': PostInstall},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ]
)
