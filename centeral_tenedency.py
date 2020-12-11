import csv
from collections import Counter as counter
with open('SOCR-HeightWeight.csv', newline='') as f:
    reader=csv.reader(f)
    text=list(reader)
text.pop(0)
new_data=[]
for a in range(0, len(text)):
    num=text[a][1]
    new_data.append(float(num))
x=(sum(new_data))/len(new_data)
print(x)
new_data.sort()
xxx=len(new_data)-1
b=xxx/2
if(str(b).endswith!='.5'):
    print(new_data[int(b)])
else:
    m=xxx-0.5
    n=xxx+0.5
    ans=(new_data(m)+new_data(n))/2
    print(ans)
for i in range(0, len(new_data)):
    new_data[i]=int(new_data[i])
data=counter(new_data)
mode={'50-60':0, '60-70':0, '70-80':0}
for z in data:
    if(z<60 and z>50):
        mode['50-60']+=1
    elif(z<70 and z>60):
        mode['60-70']+=1
    elif(z>70 and z<80):
        mode['70-80']+=1
h=list(data.values())
g=data.keys()
mno=max(h)
for name, age in data.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
    if age == mno:
        print(name)