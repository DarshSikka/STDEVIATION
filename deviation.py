from math import sqrt
import statistics
import csv
with open(input('file to take deviation of'), newline='') as f:
    reader=csv.reader(f)
    text=list(reader)
total_sum=0
count=len(text)
for a in text:
    print(a[0])
    total_sum+=int(a[0])
mean=total_sum/count
square_deviators=[]
for each_num in text:
    c=int(each_num[0])-mean
    d=c**2
    square_deviators.append(d)
super_sum=sum(square_deviators)
finality_num=super_sum/count-1
print(sqrt(finality_num))
for some in text:
    some=int(some[0])