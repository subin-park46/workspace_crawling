import seaborn as sns
import matplotlib.pyplot as plt

taxis = sns.load_dataset("taxis")

"""
pickup : 승차시간
dropoff : 하차시간
passengers : 승객 수
distance : 거리
fare : 요금
tip : 팁
tolls : 통행료
total : 총 요금 ? 
color : 택시 색
payment : 지불 방법
pickup_zone : 승차 위치 
dropoff_zone : 하차 위치
pickup_borough : 승차 도시
dropoff_borough : 하차 도시
"""

plt.figure(figsize=(15, 10))


taxis['ymd'] = list(map(lambda x: x.split()[0], taxis['pickup']))
taxis.sort_values(by=['ymd'], ascending=True, inplace=True)

ymd_group = taxis.groupby(['ymd']).sum()
ymd_group['ymd'] = ymd_group.index

bar = sns.barplot(data=ymd_group, x='ymd', y='total')
bar.tick_params(labelrotation=30)
bar.set_xlim([-1,len(ymd_group)])

for i, value in enumerate(ymd_group['ymd']):
    plt.text(i, ymd_group['total'][i], ymd_group['total'][i], horizontalalignment='center')


plt.show()