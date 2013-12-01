#!/bin/sh
curl ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt | grep -v "ACT Symbol" | grep -v "File Creation Time" | awk -F"|" '{print $1}' | sort -u > symbols/nasdaq
curl ftp://ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt | grep -v "ACT Symbol" | grep -v "File Creation Time" | awk -F"|" '{print $1}' | sort -u > symbols/other
cat symbols/nasdaq symbols/other | sort -u > symbols/all
cat symbols/own.ignore > symbols/own
cat symbols/watch.ignore > symbols/watch
wc -l symbols/all
wc -l symbols/ignore
rm symbols/nasdaq
rm symbols/other