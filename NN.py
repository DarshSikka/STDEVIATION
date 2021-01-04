import pandas
import plotly.figure_factory as ff
import csv
import statistics
import plotly.graph_objects as px
from random import randint as rand
import math
df=pandas.read_csv('newdata.csv')
df=df['average'].tolist()
print(df[1])
sample=[]
start=rand(0, len(df))
for a in range(start, start+100):
    sample.append(df[a])
mean=sum(sample)/ len(sample)
stdev=statistics.stdev(sample)
print(mean, stdev)
fig=ff.create_distplot([sample], ['average'])
print(statistics.mean(df))
se=statistics.stdev(df)/math.sqrt(len(sample))
print('Sample Error:', se)
fig.add_trace(px.Scatter(x=[mean, mean], y=[0,1], mode='lines', name='mean'))
fig.show()
#se=stdev(pop)/sqrt(sample_size)