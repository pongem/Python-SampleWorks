
from pandas_datareader import data as web

jpy = web.DataReader('DEXTHUS', 'fred')

print( jpy )

