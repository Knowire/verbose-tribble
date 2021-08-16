import os
path = '/home/psi/Repozytoria/F5/data_analysis/2_Qfactor'
os.chdir(path)

#LOAD================================================
import numpy as np

sensitivity_detector1 = np.load('sensitivity_detector1.npy')
sensitivity_detector2 = np.load('sensitivity_detector2.npy')

old_det1_para = np.loadtxt('old_det1_para.dat').T
old_det1_perp = np.loadtxt('old_det1_perp.dat').T
old_det2_para = np.loadtxt('old_det2_para.dat').T
old_det2_perp = np.loadtxt('old_det2_perp.dat').T

print(old_det1_para[0][0], old_det1_para[0][-1])
print(old_det1_perp[0][0], old_det1_perp[0][-1])
print(old_det2_para[0][0], old_det2_para[0][-1])
print(old_det2_perp[0][0], old_det2_perp[0][-1])
