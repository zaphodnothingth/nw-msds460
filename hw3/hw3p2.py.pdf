from gekko import GEKKO

m = GEKKO()             # create GEKKO model

a = m.Var(value=1)      # define new variable, initial value=0
b = m.Var(value=1)      # define new variable, initial value=1
c = m.Var(value=1)      # define new variable, initial value=1
s = m.Var(value=1)      # define new variable, initial value=1

m.Equation(a >= 0)
m.Equation(b >= 0)
m.Equation(c >= 0)
m.Equation(s >= 0)
m.Equation(a + b + c <= 60)
m.Equation(-s + ((a + b + c)/2) == 0)
m.Maximize(m.sqrt(s*(s-a)*(s-b)*(s-c)))

m.solve(disp=True)     # solve
print([a.value[0],b.value[0],c.value[0],s.value[0], ]) # print solution

