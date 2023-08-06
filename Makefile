install:
		poetry install

gendiff:
		poetry run gendiff

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

pre-commit:
		pre-commit run --all-files

lint:
	    poetry run flake8 gendiff
