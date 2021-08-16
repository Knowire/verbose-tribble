import os
os.chdir('/home/psi/Repozytoria/F5/data_analysis/1_sensitivity')

#LOAD================================================
def load_two_lists_from_file(file_name):
    x, y = [], []
    f = open(file_name)
    for line in f:
        pair = line.split()
        x.append(float(pair[0]))
        y.append(float(pair[1]))
    return x, y

x2, y2 = load_two_lists_from_file('sensitivity_detector2.dat')

#JOIN=================================================
def load_list_of_pairs_from_file(file_name):
    l = []
    f = open(file_name)
    for line in f:
        l.append([ float(value) for value in line.split() ])
    return l

pairs = [ *load_list_of_pairs_from_file('sensitivity_detector1_range1.dat'), *load_list_of_pairs_from_file('sensitivity_detector1_range2.dat') ]

def sort_func(pair):
    return pair[0]

pairs.sort( key=sort_func )

def make_two_lists_from_pairs(list_of_pairs):
    x, y = [], []
    for pair in list_of_pairs:
        x.append(pair[0])
        y.append(pair[1])
    return x, y

x1, y1 = make_two_lists_from_pairs(pairs)

#PLOT============================================================
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(x1,y1,label='detektor 1')
ax.plot(x2,y2,label='detektor 2')
ax.legend()

# ax.set_title("Porównanie zakresów czułości dwóch detektorów")
ax.set_xlabel("Energia promieniowania [eV]")
ax.set_ylabel("Zmierzone napięcie [mV]")

# plt.show()
os.chdir('/home/psi/Repozytoria/F5/img')
plt.savefig('sensitivity.png')

#SAVE AS NDARRAY===========================================
""" import numpy as np

detector1 = np.array([x1,y1])
detector2 = np.array([x2,y2])

np.save('sensitivity_detector1', detector1)
np.save('sensitivity_detector2', detector2) """
