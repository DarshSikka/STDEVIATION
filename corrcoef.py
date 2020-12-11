import numpy
import csv
import plotly.express as plot
with open('tv.csv') as f:
    reader=csv.DictReader(f)
    text=list(reader)
print(text)
tv_size=[]
tv_time=[]
for a in text:
    tv_size.append(float(a['size'])
    tv_time.append(float(a['\ttime'])
print(tv_size)
print(tv_time)