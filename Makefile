init:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests tests

update:
	mkdir -p symbols
	sh update.sh

filter:
	python main.py filter

get-data:
	rm -rf data
	mkdir -p data
	python main.py update

do-archive:
	mkdir -p archive
	tar -zcvf archive/`date +"%Y-%m-%d"`.tar.gz data/

main:
	mkdir -p data 
	python main.py main

dev:
	python main.py dev

own:
	python main.py own

update_owned:
	mkdir -p data
	python main.py update_owned

reset:
	rm symbols/ignore
	touch symbols/ignore

clean:
	find . -name '*.pyc' | xargs rm

