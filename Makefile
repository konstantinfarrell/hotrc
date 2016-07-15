.PHONY: install run

install:
	python setup.py install

test:
	python -m unittest discover
