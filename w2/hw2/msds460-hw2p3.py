from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

'''
A catering company must have the following number of clean napkins available at the beginning of each of the next four days:  day 1: 15, day 2: 12, day 3: 18, and day 4: 6.  After being used, a napkin can be cleaned by one of two methods: fast service or slow service. Fast service costs $0.10 per napkin, and a napkin cleaned via fast service is available for use the day after it is last used.  Slow service costs $0.06 per napkin, and a napkin cleaned via slow service is available two days after they were last used.  New napkins can be purchased for a cost of $0.20 per napkin.
'''

########### problem definitions
''' 
cleaned slow service 'a' : cost = .06, wait = 2
cleaned fast service 'b' : cost = .10, wait = 1
purchased            'c' : cost = .20, wait = 0

'''

# define variables
# day 1
a1 = LpVariable("day1napkinsslow", 0, None)
b1 = LpVariable("day1napkinsfast", 0, None)
c1 = LpVariable("day1napkinspurchased", 15, None) # must purchase enough for first day
# day 2
a2 = LpVariable("day2napkinsslow", 0, None)
b2 = LpVariable("day2napkinsfast", 0, None)
c2 = LpVariable("day2napkinspurchased", 0, None)
# day 3
b3 = LpVariable("day3napkinsfast", 0, 18)
c3 = LpVariable("day3napkinspurchased", 0, None)
# day 4
c4 = LpVariable("day4napkinspurchased", 0, 6) # will not purchase more than needed for last day



# define the problem
prob = LpProblem("problem", LpMinimize)


### define constraints
# laundered each day is less than or equal to demand
prob += a1 + b1 <= 15
prob += a2 + b2 <= 12
# prob += b3 <= 18  # this can be moved to the variable definition since a3 is zero

# received each day is greater than or equal to demand
# prob += c1 >= 15  # moved to variable definition
prob += c1 + c2 + b1 >= 27
prob += c1 + c2 + c3 + b1 + b2 + a1 >= 45
prob += c1 + c2 + c3 + c4 + b1 + b2 + b3 + a1 + a2  >= 51


# define objective function
prob += .06*(a1 + a2) + .1*(b1 + b2 + b3) + .2*(c1 + c2 + c3 + c4)


# solve the problem
status3 = prob.solve()
print(f"Problem")
print(f"status={LpStatus[status3]}")

# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")
    
print(f"Objective = {value(prob.objective)}")
print(f"")


# in month 1, all \\$200 remaining should be invested in (d)
# in month 2, approx \\$100 should be invested in (c), and \\$200 in (a)
# in month 3, no additional money is invested, as the \\$200 return from month 2 is used to pay bills
# in month 4, \\$50 should be invested in (a)
# this will result in approx \\$370 cash on hand in month 5
# 
# ----
