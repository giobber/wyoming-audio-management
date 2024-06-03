VENV=.venv

PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip


.PHONY: init clean venv develop install


init: venv develop install


clean:
	rm -rf .venv
venv: clean
	python3 -m venv .venv

develop:
	$(PIP) install black isort

install:
	$(PIP) install -r requirements.txt


run:
	$(PYTHON) -m volume

lint: 
	$(VENV)/bin/black volume
	$(VENV)/bin/isort --profile black volume
