# import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# Problem (Initial)
# define variables
m1m = LpVariable("model1make", 0, None) 
m1b = LpVariable("model1buy", 0, None) 
m2m = LpVariable("model2make", 0, None) 
m2b = LpVariable("model2buy", 0, None) 
m3m = LpVariable("model3make", 0, None) 
m3b = LpVariable("model3buy", 0, None) 

# defines the problem
prob = LpProblem("problem", LpMinimize)

# define constraints
prob += m1m + m1b == 3000
prob += m2m + m2b == 2000
prob += m3m + m3b == 900
prob += 2*m1m + 1.5*m2m + 3*m3m <= 10000
prob += 1*m1m +   2*m2m + 1*m3m <= 5000

# Note, if <= then <=
# If >= then >=
# If = then ==

# define objective function
prob += 50*m1m + 83*m2m + 130*m3m + 61*m1b + 97*m2b + 145*m3b

# solve the problem
status = prob.solve()
print(f"Problem")
print(f"status={LpStatus[status]}")

# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")
    
print(f"Objective = {value(prob.objective)}")
print(f"")