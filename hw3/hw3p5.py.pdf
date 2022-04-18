import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

hrs = '''40
44
48
48
60
70
72
90
100
168'''
revs = '''5958
6662
6004
6011
7250
8632
6964
11097
9107
11498'''


hrs = hrs.split('\n')
hrs = np.array([int(hr) for hr in hrs])
revs = revs.split('\n')
revs = np.array([int(rev) for rev in revs])

plt.scatter(hrs, revs)

# linear fit
m1, b1 = np.polyfit(hrs, revs, 1)
print(np.polyfit(hrs, revs, 1, full = True))

print('result of linear regression:')
print(f'\ty={round(m1, 1)}x + {round(b1, 1)}')
print('prediction at 120: {}'.format(round(m1*120 + b1), 1))
plt.plot(hrs, m1*hrs + b1, "b--", label="Linear Fit")     


print('\n\n\n')
# non-linear, 2-degree fit
n2, m2, b2 = np.polyfit(hrs, revs, 2)
print(np.polyfit(hrs, revs, 2, full = True))

print('result of non-linear, 2-degree regression:')
print(f'\ty={round(n2, 1)}x^2 + {round(m2, 1)}x + {round(b2, 1)}')
print('prediction at 120: {}'.format(round(n2*120**2 + m2*120 + b2), 1))
plt.plot(hrs, n2*hrs**2 + m2*hrs + b2, "r--", label="Non-linear, 2-degree Fit")     

'''
# non-linear, exponential fit
regressor = LinearRegression()
results = regressor.fit(hrs.reshape(-1, 1), revs)                
model = results.predict
y_fit = model(hrs.reshape(-1, 1))

plt.plot(hrs, y_fit, "k--", label="Exponential Fit")     
'''
plt.title("Revenue prediction")

plt.savefig('model_comparison.png')