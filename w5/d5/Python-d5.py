# import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# Problem (Knapsack NJ 2 CA)
# define variables
x1 = LpVariable("x1", 0, 1, cat = 'Integer')
x2 = LpVariable("x2", 0, 1, cat = 'Integer')
x3 = LpVariable("x3", 0, 1, cat = 'Integer')
x4 = LpVariable("x4", 0, 1, cat = 'Integer')
x5 = LpVariable("x5", 0, 1, cat = 'Integer')

# defines the problem
prob = LpProblem("problem", LpMaximize)
# Note, LpMaximize for a maximization problem, 
# and LpMinimize for a minimization problem

# define constraints
prob += 800*x1 + 600*x2 + 300*x3 + 400*x4 + 200*x5 <= 1100

# Note, if <= then <=
# If >= then >=
# If = then ==

# define objective function
prob += 60*x1 + 48*x2 + 14*x3 + 31*x4 + 10*x5

# solve the problem
status = prob.solve()
print(f"Problem")
print(f"status={LpStatus[status]}")

# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")
    
print(f"Objective = {value(prob.objective)}")
print(f"")

