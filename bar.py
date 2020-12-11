import pandas
import plotly.express as px
data=[[1,2,3,4,5],[1,2,3,4,5]]
df=pandas.read_csv('data.csv')
l=px.bar(df, x='Country', y=input('What information do you want'), title=input('Title'), color=input('colored column'))
print(l)
l.show()