#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:13:12 2026

@author: guntripj
"""

import numpy as np
from functools import partial


def val_iteration(S,A,P,R,gamma=0.5,epsilon=0.001):
    
    """S is a list of states;
    A is a list of actions;
    P is the state transition function specifying P(s'|s,a);
    R is a reward function R(s'|s,a);
    gamma is the discount factor in [0,1)"""
    

    # Set up accessible actions and states from specified state
    A_valid_dict = {s:{} for s in S}
    S_valid_dict = {s:{} for s in S}
    
    
    for i in range(len(S)):
        for a in A:
            for s_new in S:
                if P(s_new,S[i],a) != 0:
                    A_valid_dict[S[i]] = set(A_valid_dict[S[i]]).union({a})
                    S_valid_dict[S[i]] = set(S_valid_dict[S[i]]).union({s_new})                            
    
    # Q function
    
    def q_func(s,a,val_func):
    
        S_new = S_valid_dict[s]
        
        q_val = sum([P(s_new,s,a)*(R(s_new,s,a) + gamma*val_func[s_new]) for s_new in S_new])
        
        return q_val
        
    
    
    val_map = {s:0 for s in S}
    policy_map = {s:None for s in S}
    
    val_maps = [val_map]
    
    k = 0
    
    
    while ((k < 1) or max([abs(val_maps[-1][s] - val_maps[-2][s]) for s in S])) >= epsilon:
        
        k += 1
        val_map_k = {s:0 for s in S}
        
        # Calculate new value map 
        for s in S:
            
            A_valid = list(A_valid_dict[s]) # Get possible actions

            if A_valid != []: # Update value only with respect to states we can access from s (BR is a terminal state)
                val_map_k[s] = max([q_func(s,a,val_maps[-1]) for a in A_valid])
        
        val_maps.append(val_map_k)
        
    # Calculate updated policy
    for s in S:
        
        A_valid = list(A_valid_dict[s]) # Get possible actions
        
        if A_valid != []: # Update value only of states we can access from s (BR is a terminal state)
            a_index = np.argmax(np.array([q_func(s,a,val_maps[-1]) for a in A_valid]))
            policy_map[s] = A_valid[a_index]



    return policy_map,val_maps[-1]





