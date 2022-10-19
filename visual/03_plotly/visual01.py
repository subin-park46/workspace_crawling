import plotly.express as px
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 2013년 몬트리올 시장 선거 데이터 (Coderre, Bergeron, Joly -> 사람 이름)
df = px.data.election()
print(df)

fig = px.bar(df, x='district', y=['Coderre', 'Bergeron', 'Joly'], barmode='group')
# fig.show()

fig.write_html('montreal.html')
fig.write_json('montreal.json')
fig.write_image('montreal.png')