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

clean:
	find . -name '*.pyc' | xargs rm

