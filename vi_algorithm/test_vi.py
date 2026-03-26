
from vi_algorithm.vi_4 import *

from functools import partial


ex_1_dict =  {
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


ex_1_S = ['TL','TR','BL','BR']
ex_1_A = ['R','L','U','D']


ex_2_dict = {
        'HRH':[0.95,7],
        'HPH':[0.7,10],
        'SRH':[0.5,0],
        'SPH':[0.1,2],
        'HRS':[0.05,7],
        'HPS':[0.3,10],
        'SRS':[0.5,0],
        'SPS':[0.9,2]
    }

ex_2_S = ['H','S']
ex_2_A = ['R','P']


def P(ex_dict,s_new,s,a):
    
    if ((s+a+s_new) in ex_dict):
        p = ex_dict[s+a+s_new][0]
    else:
        p = 0
    
    return p

def R(ex_dict,s_new,s,a):
    
    return ex_dict[s+a+s_new][1]

P_1 = partial(P,ex_1_dict)
R_1 = partial(R,ex_1_dict)
P_2 = partial(P,ex_2_dict)
R_2 = partial(R,ex_2_dict)




def test_1():
    
    pi,val_map = val_iteration(ex_1_S,ex_1_A,P_1,R_1,gamma=0.9)
    
    correct_pi = { 'TL': 'D', 'TR': 'D', 'BL': 'R', 'BR': None }
    correct_val_map = {'TL': 14.86378742883109,
                       'TR': 14.47531566016127,
                       'BL': 19.087657830080634,
                       'BR': 0}

    
    if (pi == correct_pi) and (val_map == correct_val_map):
        result = "PASSED_TEST_1"
    else:
        result = "FAILED_TEST_1"
    
    return result


def test_2():
    
    pi,val_map = val_iteration(ex_2_S,ex_2_A,P_2,R_2,gamma=0.8)
    
    correct_pi = {'H': 'P', 'S': 'R'}
    correct_val_map = {'H': 35.711062336395926, 'S': 23.80630043163403}

    
    if (pi == correct_pi) and (val_map == correct_val_map):
        result = "PASSED_TEST_2"
    else:
        result = "FAILED_TEST_2"
    
    return result

