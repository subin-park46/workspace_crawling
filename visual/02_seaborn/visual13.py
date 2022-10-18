import seaborn as sns
import matplotlib.pyplot as plt


penguins = sns.load_dataset('penguins')

fig = plt.figure()
ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(2, 2, 2)
ax03 = fig.add_subplot(2, 2, 4)

sns.histplot(data=penguins, x='body_mass_g', ax=ax01)
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', ax=ax02)
sns.boxplot(penguins['body_mass_g'].fillna(penguins['body_mass_g'].mean()))

plt.tight_layout()
plt.show()
