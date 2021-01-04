import csv
import statistics
import pandas
import plotly.figure_factory as px
from random import randint as rand
my_dices=[]
def dice_role():
    dice1=rand(1,6)
    dice2=rand(1,6)
    return dice1+dice2
for a in range(0, 1000):
    my_dices.append(dice_role())
mean=sum(my_dices)/len(my_dices)
median=statistics.median(my_dices)
mode=statistics.mode(my_dices)
st_deviation=statistics.stdev(my_dices)
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