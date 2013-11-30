init:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests tests

update:
	mkdir -p symbols
	sh update.sh

data:
	rm -rf data
	mkdir -p data
	python main.py update

archive:
	mkdir -p archive
	tar -zcvf archive/`date +"%Y-%m-%d"`.tar.gz data/

main:
	mkdir -p data 
	python main.py main

dev:
	python main.py dev

clean:
	find . -name '*.pyc' | xargs rm

