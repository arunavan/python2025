from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


#pip install matplotlib
#pip install seaborn
sns.distplot(random.binomial(n=5, p=0.5, size=1000), hist=True, kde=False)

plt.show()