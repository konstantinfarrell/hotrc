.PHONY: install run

VENV_DIR ?= .env
PYTHON = python
REQUIREMENTS = requirements.txt

install:
	$(VENV_DIR)/bin/$(PYTHON) setup.py install

init:
	clear
	rm -rf $(VENV_DIR)
	@$(MAKE) $(VENV_DIR)
	@$(MAKE) install

clean:
	find . -iname "*.pyc" -delete
	find . -iname "*.pyo" -delete
	find . -iname "__pycache__" -delete

test:
	clear
	$(VENV_DIR)/bin/$(PYTHON) -m unittest discover

coverage:
	clear
	$(VENV_DIR)/bin/$(PYTHON) -m coverage run -m unittest discover
	$(VENV_DIR)/bin/$(PYTHON) -m coverage report -m

travis-install:
	python -m pip install -r requirements.txt

travis-test:
	python -m unittest discover

travis-coverage:
	python -m coverage unittest discover

pep8:
	clear
	$(VENV_DIR)/bin/flake8 .

$(VENV_DIR):
	virtualenv $(VENV_DIR)
	if [ -a $(REQUIREMENTS) ] ; \
	then \
		$(VENV_DIR)/bin/pip install -r requirements.txt ; \
	else \
		$(VENV_DIR)/bin/pip install flake8 coverage; \
		$(VENV_DIR)/bin/pip freeze > requirements.txt ; \
	fi;
