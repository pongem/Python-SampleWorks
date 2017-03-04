import pandas as pd

from mod_Stock_Analyze_Helper import *

import matplotlib.pyplot as plt

if __name__ == "__main__":

	start_date = "2016-12-01"
	end_date = "2017-03-01"
	arrSymbols = ["CPF","PTT", "CPALL","TTW"]
	helper = Stock_Helper()
	df = helper.buildClosePrice(start_date, end_date, arrSymbols)

	#print (df)

	newdf = df.ix["2017-01-18" : "2017-02-21", ['CPF','CPALL'] ]

	print (newdf.mean())