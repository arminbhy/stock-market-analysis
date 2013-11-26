init:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests tests

main:
	mkdir -p data 
	python main.py

update:
	mkdir -p symbols
	curl ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt | grep -v "ACT Symbol" | grep -v "File Creation Time" | awk -F"|" '{print $1}' | sort -u > symbols/nasdaq
	curl ftp://ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt | grep -v "ACT Symbol" | grep -v "File Creation Time" | awk -F"|" '{print $1}' | sort -u > symbols/other
	cat symbols/nasdaq symbols/other | sort -u > symbols/all

clean:
	find . -name '*.pyc' | xargs rm

