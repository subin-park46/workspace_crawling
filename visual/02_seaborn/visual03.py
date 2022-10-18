import seaborn as sns
import matplotlib.pyplot as plt

car_crashes = sns.load_dataset('car_crashes')
car_crashes.sort_values("total", ascending=False, inplace=True)

plt.figure()

sns.barplot(data=car_crashes, x='abbrev', y='total', facecolor='w', edgecolor='black')

sns.barplot(data=car_crashes, x='abbrev', y='speeding', linewidth=3, color='r', alpha=0.3, label="speeding")
sns.barplot(data=car_crashes, x='abbrev', y='alcohol', linewidth=3, color='g', alpha=0.3, label="alcohol")
sns.barplot(data=car_crashes, x='abbrev', y='no_previous', linewidth=3, color='b', alpha=0.3, label="no_previous")

plt.xlim(-1, 51)
plt.show()