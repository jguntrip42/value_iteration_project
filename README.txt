Value iteration project

Dependencies for python script are:
numpy
pytest


Standard libraries used:
functools (used in testing script)



Pseudo code outline of script (note we use dictionaries for the role of functions to assign states value etc.):


VALUE ITERATION ALGORITHM

INPUTS
S, list of states
A, list of actions
P(s_new|s,a), state transition function
R(s_new|s,a), reward function
gamma, discount parameter
epsilon, convergence difference value

INITIALISE
S_d (s), dictionary of sets representing states reachable from s 
A_d (s), dictionary of sets representing actions applicable from s 
Value_map_0 (s), initial value dictionary
Value_maps = [Value_map_0 (s)], list of value dictionaries
k = 0
Q_func(s,a,val_map), Q function  
pi(s), empty policy dictionary mapping states to actions

WHILE ((k=0) OR ((Value_maps[-1] - Value_maps[-2]) < epsilon)) DO
	k = k + 1
	INITIALISE Value_map, new empty value dictionary 
	
	FOR s in S DO
		Value_map(s) = MAX(Q_func(s,a,Value_maps[-1]) for a in A_d(s))
	
	ADD Value_map TO Value_maps
	
FOR s in S DO
	a_index = ARGMAX(ARRAY(Q_func(s,a,Value_maps[-1]) for a in A_d(s)))
	pi(s) = A_d(a_index)

OUTPUTS
pi(s), optimal policy dictionary mapping states to optimal action
Value_maps[-1](s), value dictionary mapping states to calculated value



