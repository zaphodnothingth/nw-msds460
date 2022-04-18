from gekko import GEKKO
m = GEKKO()             # create GEKKO model

x1 = m.Var(value=1)      # define new variable, initial value=0
x2 = m.Var(value=1)      # define new variable, initial value=1

m.Equation(x1 >= 0)
m.Equation(x2 >= 0)
m.Equation(8000 * x1 + 5000 *  x2 <= 40000)
m.Maximize(4*x1+2*x2-0.5*x1**2-0.25*x2**2)

m.solve(disp=True)     # solve
print([x1.value[0],x2.value[0]]) # print solution

