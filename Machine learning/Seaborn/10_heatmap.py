import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
df['species']=df['species'].map({'setosa':1,'versicolor':2,'virginca':3})
correlation=df.corr()
sns.heatmap(correlation,cbar=True,annot=True,linewidth=0.5,cmap='Blues')#displaying plot
plt.show()
#positive correlation is represented as light
#negative correlation is represented as dark