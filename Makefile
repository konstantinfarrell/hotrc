.PHONY: install run

install:
	python setup.py install

test:
	python -m unittest discover

travis-install:
	pip install setuptools flake8

travis-test:
	python -m unittest discover
