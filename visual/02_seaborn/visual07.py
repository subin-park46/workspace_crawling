import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

markers = {"Male": "P", "Female": "o"}
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species', style='sex', markers=markers)

plt.show()