.PHONY: build install clean deploy test unit-test

-include CONFIG

build:
	echo "Nothing yet"

clean:
	echo "Nothing yet"

deploy:
	echo "Nothing yet"

functional-test:
	echo "No functional tests yet"

unit-test:
	pytest ./src/tests/test.py

test: unit-test

install:
	pip install -r requirements.txt

