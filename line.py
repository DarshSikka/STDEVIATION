import pandas
import plotly.express as px
data=[[1,2,3,4,5],[1,2,3,4,5]]
df=pandas.read_csv('line_chart.csv')
l=px.line(df, x='Year', y='Per capita income', title='PCI', color='Country')
print(l)
l.show()