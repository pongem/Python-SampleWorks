
import pandas as pd

class Stock_Helper(object):

	def __init__(self):
		pass

	def buildClosePrice(self,start_date, end_date, arrSymbols):

		# define start and enddate
		dates = pd.date_range(start_date, end_date)

		# create an empty dataframe
		df1 = pd.DataFrame( index=dates )

		for symbol in arrSymbols:
			# read symbol data
			dfTemp = pd.read_csv("data/%s.csv" % (symbol), index_col="Date",
				parse_dates=True, usecols=['Date','Close'],
				na_values=['nan'])

			# rename column
			dfTemp.rename( columns={'Close': symbol }, inplace=True)

			# join the dataframes
			df1 = df1.join(dfTemp)

		# drop nan value
		df1 = df1.dropna()

		return df1
		