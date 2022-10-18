import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

sns.violinplot(data=penguins, x='body_mass_g', y='species', hue='sex', split=True)

plt.show()