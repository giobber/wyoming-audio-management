VENV=.venv

PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))



.PHONY: clean venv update init develop install

init: venv update

clean:
	rm -rf .venv
venv: clean
	python3 -m venv $(VENV)
	$(PIP) install -U pip

update:
	$(PIP) install -r requirements.txt

develop: update
	$(PIP) install -e .[dev]

install: update
	$(PIP) install -e .

requirements.txt: venv install
	$(PIP) install -U -e .
	$(PIP) freeze --exclude-editable > requirements.txt
	$(PIP) install -e .[dev]

.PHONY: service
service:
	echo "PROJECT_DIR: $(ROOT_DIR)"
	sed "s|PROJECT_PATH|$(ROOT_DIR)|g" ./system/volume.service > /etc/systemd/system/volume.service
	systemctl daemon-reload
	systemctl enable volume.service
	systemctl start volume.service



.PHONY: run lint
run:
	$(PYTHON) -m audio

lint: 
	$(VENV)/bin/black audio
	$(VENV)/bin/isort --profile black audio
