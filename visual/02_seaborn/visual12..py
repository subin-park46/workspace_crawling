import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

sns.displot(data=penguins, x='bill_length_mm')
plt.show()