
from vi_algorithm import *


example_data_dict =  {
               'TLRTR': [0.9,-1],
               'TLRBL': [0.1, -2],
               'TLDBL': [0.9, -2],
               'TLDTR': [0.1, -1],
               'TRLTL': [0.9, -3/2],
               'TRLBR': [0.1, 10],
               'TRDBR': [0.8, 15],
               'TRDTL': [0.2, -1],
               'BLRBR': [0.9, 20],
               'BLRTL': [0.1, -5/2],
               'BLUTL': [0.8, -1/2],
               'BLUBR': [0.2, 5]}


example_S = ['TL','TR','BL','BR']
example_A = ['R','L','U','D']


def P_0(s_new,s,a):
    
    if ((s+a+s_new) in example_data_dict):
        p = example_data_dict[s+a+s_new][0]
    else:
        p = 0
    
    return p

def R_0(s_new,s,a):
    
    return example_data_dict[s+a+s_new][1]


pi_0, val_maps_0 = val_iteration(example_S,example_A,P_0,R_0)