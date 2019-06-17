init:
	pip install -r requirements.txt

test:
	# py.test tests

run: init test
	python sample/LightshotSniffer.py

.PHONY: init test