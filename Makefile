init:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests tests

main: 
	python main.py

clean:
	find . -name '*.pyc' | xargs rm

