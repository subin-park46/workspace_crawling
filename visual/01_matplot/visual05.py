import matplotlib.pyplot as plt
from random import randint

fig, ax = plt.subplots()

x = list(randint(0, 10) for i in range(100))

ax.hist(x, bins = 10)

plt.xticks(list(range(0, 11))) # 눈금 표시
plt.yticks(list(range(0, 101, 5))) # 5 간격으로 눈금 표시

plt.xlim(0, 10) # X축이 표시되는 범위를 지정하거나 반환
plt.ylim(0, 100) # Y축이 표시되는 범위를 지정하거나 반환

plt.show()