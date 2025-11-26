symbols = 'AAPL,MSFT,GOOG,AMZN'
print(symbols[0])
print(symbols[1])
print(symbols[-1])

symbols = symbols + ',TSLA'
print(symbols)

print('GOOG' in symbols)
print('AA' in symbols)
print('N,T' in symbols)

print(symbols.lower()) # does not happen in place, instead it creates a new string

print(symbols)

print(symbols.find('MSFT'))

print(symbols.strip('A'))