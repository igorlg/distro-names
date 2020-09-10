.PHONY: default
default: clean test build publish

.PHONY: clean
clean:
	@echo "Cleaning up..."
	rm -rvf build/
	rm -rvf dist/
	rm -rvf distro_names.egg-info
	rm -rvf .pytest_cache
	rm -rvf MANIFEST.in
	rm -rvf distro/__pycache__ distro/*.pyc
	rm -rvf test/__pycache__ test/*.pyc

.PHONY: dev
dev:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

.PHONY: test
test:
	@echo "Running tests..."
	@pylint distro
	@pytest

.PHONY: build
build: clean
	@python setup.py sdist bdist bdist_egg
	@twine check dist/*

.PHONY: test-publish
test-publish: build
	@rm -f dist/distro-names-*mac*.tar.gz
	@twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: publish
publish: build
	@rm -f dist/distro-names-*mac*.tar.gz
	@twine upload dist/*
