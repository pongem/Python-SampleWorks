import pandas as pd

import matplotlib.pyplot as plt

def get_max_close(symbol):
	df = pd.read_csv("data/%s.csv" % (symbol))
	return df['Close'].max()



def test_run():
	df = pd.read_csv("data/CPF.csv")
	print (df['Close'])
	df[['Close','Low','High']].plot()
	plt.show()



if __name__ == "__main__":
	test_run()