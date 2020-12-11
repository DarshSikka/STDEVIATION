import pandas
import plotly.express as px
data=[[1,2,3,4,5],[1,2,3,4,5]]
df=pandas.read_csv('Copy+of+data+-+data.csv')
l=px.scatter(df, x='Country', y='InternetUsers', title='PCI', color='Country', size='Percentage' ,size_max=60)
print(l)
l.show()
