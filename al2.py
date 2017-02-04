# coding=utf-8
import os
import numpy as np

x = 10
y = 11089
np.set_printoptions(threshold='nan')


def al2(p_data, n_data, us_data, i):
    LP = []
    LN =  []
    for num in range(i):
        p_vote = 0
        n_vote = 0
        for e in us_data[num]:
            n_ = []
            p_ = []
            for j in range(10):
                n_.append(sim(e, n_data[j]))
                p_.append(sim(e, p_data[j]))
            n_max = np.max(n_)
            p_max = np.max(p_)
            if p_max > n_max:
                p_vote += 1
            else:
                n_vote += 1
        if p_vote > n_vote:
            LP.append(us_data[num])
        else:
            LN.append(us_data[num])
        print '1'

def sim(x, y):
    return (np.dot(x, y) / np.dot(np.sqrt(
        np.sum(np.square(x))), np.sqrt(np.sum(np.square(y)))))


if __name__ == '__main__':
    list_file_1 = os.listdir('dpgmm/done')
    i = len(list_file_1)
    n_data = np.load('N_data.npy')
    p_data = np.load('P_data.npy')
    us_data = {}
    for num in list_file_1:
        list_file_2 = os.listdir('dpgmm/done/' + num)
        us_data[int(num)] = []
        count = 0
        for doc in list_file_2:
            with open('dpgmm/done/' + num + '/' + doc, 'r') as point:
                temp = point.read()
                us_data[int(num)].append(np.fromstring(temp, sep=' '))
    al2(p_data, n_data, us_data, i)
