VENV=.venv

PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))


.PHONY: clean venv develop update install


.PHONY: clean venv

clean:
	rm -rf .venv
venv: clean
	python3 -m venv .venv



.PHONY: develop update

develop: venv update-dev

update-dev:
	$(PIP) install -e .[dev]



.PHONY: service install

install: venv update service

update:
	$(PIP) install -e .

service:
	echo "$(ROOT_DIR)"
	sed "s|PROJECT_PATH|$(ROOT_DIR)|g" volume.service > /etc/systemd/system/volume.service
	systemctl daemon-reload
	systemctl enable volume.service
	systemctl start volume.service



.PHONY: run lint
run:
	$(PYTHON) -m volume

lint: 
	$(VENV)/bin/black volume
	$(VENV)/bin/isort --profile black volume
