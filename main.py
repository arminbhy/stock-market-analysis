import stocks

print stocks.Symbols('all').get_symbols()
for i in stocks.GFinance('msft').get_events():
    print i
