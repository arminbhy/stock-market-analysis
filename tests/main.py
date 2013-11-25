import stocks

if __name__ == "__main__":
    print stocks.Ticker('MSFT').get_close_prices()
