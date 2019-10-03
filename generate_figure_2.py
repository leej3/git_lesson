# coding: utf-8
import matplotlib as mpl
mpl.use('Agg')
import seaborn as sns

df = sns.load_dataset('tips')
seaborn_plot = sns.pairplot(df)
