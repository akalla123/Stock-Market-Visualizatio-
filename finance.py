from yahoo_fin.stock_info import *
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import matplotlib.style as style
import time	
cname = input("Enter the name of the company: ")
style.use('seaborn-poster') #sets the size of the charts
style.use('ggplot')

data = pd.read_csv("companylist.csv")
symbol = list(data['Symbol'])
name = list(data['Name'])
sector = list(data['Sector'])
industry = list(data['industry'])
plt.ion()
plt.figure()
ind = name.index(cname)
a = get_data(str(symbol[ind]))
x = []
y = []
for i in range(0,len(a)):
	if i % 10 == 0:
		plt.clf()
		plt.title(a.index[i])
		plt.xlabel(cname)
		plt.ylabel('Stock Price in US Dollars')
		plt.plot(a.index[i],a['close'][i],color='black')
		x.append(a.index[i])
		y.append(a['close'][i])
		plt.plot(x,y,color='black')
		plt.pause(0.01)
	else:
		pass
plt.pause(10)
plt.show()
