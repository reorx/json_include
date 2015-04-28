.PHONY: clean test

clean:
	rm -rf build dist *.egg-info

build:
	python setup.py build

build_dist:
	python setup.py build sdist

upload_dist:
	python setup.py sdist upload

test:
	PYTHONPATH=. nosetests -w test/ -v
