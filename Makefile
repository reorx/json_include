.PHONY: clean test

clean:
	rm -rf build dist *.egg-info

build:
	python setup.py build

test:
	PYTHONPATH=. nosetests -w test/ -v

publish:
	python setup.py sdist bdist_wheel upload
