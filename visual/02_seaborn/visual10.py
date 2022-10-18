import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

# ecdf : 경험적 누적분포함수 (반복된 시행을 통해 확률변수가 일정 값을 넘지 않을 확률 유추)
sns.ecdfplot(data=penguins, x='body_mass_g')
plt.show()