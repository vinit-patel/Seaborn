import seaborn as sns
import matplotlib.pyplot as plt


tips=sns.load_dataset('tips')


sns.distplot(tips['total_bill'],bins=30)

plt.show()

