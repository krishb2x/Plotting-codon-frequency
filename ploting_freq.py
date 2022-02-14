from tkplot import *
from Numeric import *
def codon_sort(a,b):
if a < b:
return -1
elif a > b:
return 1
else:
return 0
labels=count.keys()
labels.sort(codon_sort)
w1=window(plot_title=’Count codons’,width=1000)
y=array(count.values())[:len(count)/2]
x=arange(len(y)+1)
w1.bar(y,x,label=labels[:len(count)/2])
w2=window(plot_title=’Count codons(2)’,width=1000)
y=array(count.values())[(len(count)/2)+1:]
x=arange(len(y)+1)
w2.bar(y,x,label=labels[(len(count)/2)+1:])
