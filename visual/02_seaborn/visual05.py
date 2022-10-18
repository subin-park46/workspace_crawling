import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

# sns.boxplot(data=penguins, x='body_mass_g')
# sns.boxplot(data=penguins, x='bill_length_mm') # x는 옆쪽으로
sns.boxplot(data=penguins, x='species', y='bill_depth_mm', hue='sex')

plt.show()