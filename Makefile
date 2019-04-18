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

run:
	python HW6\ Files/willy.py english_cnf.gr sentences.sen

install:
	pip install -r requirements.txt

