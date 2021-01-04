import plotly.graph_objects as go 
import pandas as pd
import csv
import plotly.figure_factory as pff
import statistics as stats
from random import randint
df=pd.read_csv('studentMarks.csv')
list_df=df['Math_score'].tolist()
fig=pff.create_distplot([list_df],['Math Score'], show_hist=False)
print(stats.stdev(list_df))
print(stats.mean(list_df))
length=len(list_df)
x=randint(1, length-100)
random_list=[]
for a in range(x, x+100):
    random_list.append(list_df[a])
mean=stats.mean(random_list)
stdev=stats.stdev(random_list)
print(mean, stdev)
fig2=pff.create_distplot([random_list], ['sample marks'], show_hist=False)
fig2.add_trace(go.Scatter(x=[mean, mean], y=[0,0.2], mode="lines", name='mean'))
fig2.show()
st_deviation=stdev
dif_d, sum_d=mean-st_deviation, mean+st_deviation
dif_d2, sum_d2=mean-(2*st_deviation), mean+(2*st_deviation)
dif_d3, sum_d3=mean-(3*st_deviation), mean+(3*st_deviation)
dif_d4, sum_d4=mean-(4*st_deviation), mean+(4*st_deviation)
ranges=[]
for g in my_dices:
    if(g>dif_d and g<sum_d):
        ranges.append(1)
    elif(g>dif_d2 and g<sum_d2):
        ranges.append(2)
    elif(g>dif_d3 and g<sum_d3):
        ranges.append(3)
    elif(g>dif_d3 and g<sum_d3):
        ranges.append(4)
d1s=0
d2s=0
d3s=0
d4s=0
for l in ranges:
    if(l==1):
        d1s+=1
    elif(l==2):
        d2s+=1
    elif(l==3):
        d3s+=1
    else:
        d4s+=1
total=len(my_dices)
percent1=(d1s/total)*100
percent2=(d2s/total)*100
percent3=(d3s/total)*100
percent4=(d4s/total)*100
array_whole=[percent1, percent2, percent3, percent4]
print(*array_whole, sep='::')