.PHONY: clean clean-pyc lint install
.DEFAULT_GOAL := help


help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-pyc

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

lint: ## check style with flake8
	flake8 ariane

install-python:
	pyenv install --skip-existing --verbose 3.10.1
	pyenv local 3.10.1

install-requirements:
	pip install --upgrade pip
	pip install -r requirements.txt

install-virtualenv: clean install-python  ## install the package to the active Python's site-packages
	rm -rf .venv
	~/.pyenv/shims/python3.10 -m venv .venv
	echo "Please run source .venv/bin/activat and then run make install-requirements"
	