import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
Result=pandas.read_csv('D:\python\machine learning\iris\iris.csv')
print(Result)
print(Result.shape)
print(Result.head(20))
print(Result.describe())
print(Result.groupby('variety').size())
#Data visualization
Result.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)
plt.show()
Result.hist()
plt.show()
scatter_matrix(Result)
plt.show()
