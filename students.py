import pandas as panda
import plotly.graph_objects as px
import csv
data=panda.read_csv('students.csv')
data.loc[data['student_id']=='TRL_987']
print(data.groupby('level')['attempt'].mean())
graph=px.Figure(px.Bar(
    x=data.groupby('level')['attempt'].mean(),
    y=['level1', 'level2', 'level3', 'level4']
))
graph.show()