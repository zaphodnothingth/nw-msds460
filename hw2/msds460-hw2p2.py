# import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize
import pandas as pd
# Problem (Initial)
# define variables
M1 = LpVariable("M1", 0, 98) # number of machine 1 available
M2 = LpVariable("M2", 0, 73) # number of machine 2 available
S = LpVariable("S", 0, 260) # tons of steel to be used/available
TM1 = LpVariable("TM1", 0, None) # number of cars on machine 1
TM2 = LpVariable("TM2", 0, None) # number of cars on machine 2
CM1 = LpVariable("CM1", 0, None) # number of cars on machine 1
CM2 = LpVariable("CM2", 0, None) # number of cars on machine 2
# defines the problem
prob = LpProblem("problem", LpMaximize)
# Note, LpMaximize for a maximization problem,
# and LpMinimize for a minimization problem
# define constraints
prob += .8*CM1 + 1*TM1 <= 98 # time to produce cars & trucks on machine 1 will be up to the number rented
prob += .6*CM2 + .7*TM2 <= 73 # time to produce cars & trucks on machine 2 will be up to the number available
prob += CM1 + CM2 >= 88 # number of cars sold is less than or equal to the number produced on both machines
prob += TM1 + TM2 >= 26 # number of trucks sold is less than or equal to the number produced on both machines
prob += 2*(CM1 + CM2) + 3*(TM1 + TM2) <= 260 # steel used is less than or equal to available
# Note, if <= then <=
# If >= then >=
# If = then ==
# define objective function
prob += 300*(CM1 + CM2) + 400*(TM1 + TM2) - 50*(TM1+TM2)
# solve the problem
status = prob.solve()
print(f"Problem")
print(f"status={LpStatus[status]}")
# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Objective = {value(prob.objective)}\n\n")
print(f"dual:\n")

o = [{'name':name, 'constraint': c, 'shadow price':c.pi, 'slack': c.slack}
    for name, c in prob.constraints.items()]

print(pd.DataFrame(o))