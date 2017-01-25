import numpy as np
from sklearn import mixture

np.set_printoptions(threshold="nan")
data=open("finished_pos.dat",'r').read().replace("0.",'0')
data_array=np.fromstring(data,sep=' ').reshape(80,-1)
g=mixture.DPGMM().fit(data_array).fit_predict(data_array)
print mixture.DPGMM().fit(data_array).fit_predict(data_array)
