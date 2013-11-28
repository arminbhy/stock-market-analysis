init:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests tests

main:
	mkdir -p data 
	python main.py

update:
	mkdir -p symbols
	sh update.sh
	rm -rf data
	mkdir -p data
	python main.py update

archive:
	mkdir -p archive
	tar -zcvf archive/`date +"%Y-%m-%d"`.tar.gz data/

clean:
	find . -name '*.pyc' | xargs rm

