import matplotlib.pyplot as plt

# figure 생성 -> 도화지
fig = plt.figure()

# subplot 배치 -> 도화지 나누기 (몇 등분)
ax = fig.subplots()

# 그래프 그리기
ax.plot([1, 2, 3, 4, 5])

# 그래프 출력
plt.show()

