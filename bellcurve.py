import pandas
import plotly.figure_factory as px
import csv
df=pandas.read_csv('hw.csv')
fig=px.create_distplot([df['Weight(Pounds)'].tolist()], ['Weight'], show_hist=False)
fig.show()