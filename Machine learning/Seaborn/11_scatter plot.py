import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
sns.displot(df['sepal_width'],color='b')
plt.show()