# import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# Problem 1
# define variables
MDs = LpVariable("MDs", 0, None) # MDs>=0
NPs = LpVariable("NPs", 0, None) # NPs>=0
PAs = LpVariable("PAs", 0, None) # PAs>=0

# defines the problem
prob = LpProblem("problem", LpMinimize)
# Note, LpMaximize for a maximization problem, 
# and LpMinimize for a minimization problem

# define constraints
prob += MDs + NPs + PAs >= 10
prob += 1.5 * PAs <= NPs
prob += PAs + NPs <= 2 * MDs
# Note, if <= then <=
# If >= then >=
# If = then ==

# define objective function
prob += 150*MDs + 110*NPs + 100*PAs

# solve the problem
status = prob.solve()
print(f"Problem 1")
print(f"status={LpStatus[status]}")

# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")
    
print(f"Objective = {value(prob.objective)}")
print(f"")
