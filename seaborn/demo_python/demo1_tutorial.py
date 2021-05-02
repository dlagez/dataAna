# author: roczhang
# file: demo1_tutorial.py
# time: 2021/04/19
import seaborn as sns
penguins = sns.load_dataset('penguins')
sns.histplot(data=penguins, x="flipper_length_mm", hue="sprcies", multiple="srack")
