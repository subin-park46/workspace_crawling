import plotly.express as px

df = px.data.medals_long()
# print(df)

korea = df[df['nation'] == 'South Korea']
# print(korea)

fig = px.pie(korea, values='count', names='medal')
fig.show()