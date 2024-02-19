from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=20 ,loc=20*0.5, scale=2.5))

plt.show()