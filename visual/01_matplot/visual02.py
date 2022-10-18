import matplotlib.pyplot as plt

# figure, subplots 한번에
# fig = plt.figure
# ax = fig.subplots()
fix, ax = plt.subplots()

# 그래프 그리기
x = [1, 2, 3, 4, 5]
y01 = list(map(lambda x: x ** 2, x))
y02 = list(map(lambda x: x ** 3, x))

ax.plot(x, y01, color = 'red', label = 'pow2')
ax.plot(x, y02, color = 'blue', label = 'pow3')

# 범례 표시
plt.legend()


# 그래프 출력
plt.show()