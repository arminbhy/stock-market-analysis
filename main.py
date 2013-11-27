from stocks import PreDefinedSymbols
from stocks import Ticker

t = Ticker('twtr')
print t.as_dict()
print t.get_gfinance().get_description()

#print t.get_moving_average_convergence()['trigger']
#t.save_to_file('data')

#t2 = Ticker('msft')
#t2.load_from_file('data')
#print t2.quote