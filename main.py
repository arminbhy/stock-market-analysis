import stocks

for i in stocks.GFinance('msft').get_events():
    print i
