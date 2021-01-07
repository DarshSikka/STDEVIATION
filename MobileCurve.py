import pandas
import plotly.figure_factory as px
import csv
df=pandas.read_csv('MobileNetwork.csv')
list_df=df['Mobile Brand'].tolist()
print(list_df)
fig=px.create_distplot([df['Avg Rating'].tolist()], ['Different Brands as per serial number in list given in dialogue'], show_hist=False)
fig.show()