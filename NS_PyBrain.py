import pandas
import numpy as np
from scipy.stats.stats import pearsonr
#help(pearsonr)

f = 'c:\spisok.csv'
#spisok = pandas.read_csv(f, sep = ';', decimal='.', dtype=float, header = 0,  low_memory=False)
spisok = pandas.read_csv(f, sep = ';', decimal=',', dtype=float, low_memory=False, encoding='cp1251')

#print(spisok.dtypes)
spisok.insert(8, 'm1', 0)

#spisok['m1'] = (spisok['n1'] + spisok['n2'])*1000
#print(spisok['m1'][1:10])

from pybrain.tools.shortcuts import buildNetwork
net = buildNetwork(5, 3, 1)
