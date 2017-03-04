import pandas as pd

from mod_Stock_Analyze_Helper import *

import matplotlib.pyplot as plt

if __name__ == "__main__":

	start_date = "2016-10-01"
	end_date = "2017-03-01"
	arrSymbols = ["CPF","PTT", "CPALL","TTW"]
	helper = Stock_Helper()
	df = helper.buildClosePrice(start_date, end_date, arrSymbols)

	# slice the array
	newdf = df.ix["2016-10-01" : "2017-03-01", ['CPF'] ]

	# compute daily return
	dailyReturn = helper.compute_daily_returns(newdf)\
	#dailyReturn.plot()
	#plt.show()

	# compute histogram
	dailyReturn.hist( bins=20 )
	plt.show()


