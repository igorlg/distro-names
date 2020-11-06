clean:
	rm -rf dist/ .pytest_cache/
	find . -type d -name __pycache__ -delete

target:
	@$(MAKE) pr

dev:
	pip install --upgrade pip poetry pre-commit
	pre-commit install

test:
	poetry run pytest -vvv

pr: test

# build: pr
build:
	poetry build

#
# Use `poetry version <major>/<minor>/<patch>` for version bump
#
release-prod:
	poetry config pypi-token.pypi ${PYPI_TOKEN}
	poetry publish -n

release-test:
	poetry config repositories.testpypi https://test.pypi.org/legacy
	poetry config pypi-token.pypi ${PYPI_TEST_TOKEN}
	poetry publish --repository testpypi -n

release: pr
	poetry build
	$(MAKE) release-test
	$(MAKE) release-prod

