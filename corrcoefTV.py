import pandas
import csv
import plotly.express as px
import numpy as np 
df=pandas.read_csv('tv.csv')
size=df['Size'].tolist()
time=df['Time'].tolist()
a=np.corrcoef(time, size)
print(a)
fig=px.scatter(data_frame=df, x='Size', y='Time', color='Size')
fig.show()