import numpy as np
from random import random

days = 500

# list of probabiliies for number of bikes sold
sales_probs = [.15]*4
more_than_4 = [.35, .45, .15, .05]
more_than_4 = [prob * .4 for prob in more_than_4]
sales_probs.extend(more_than_4)

# list of bonus values
bonus_vals = [10, 15, 20, 25]
bonus_probs = [.4, .35, .2, .05]

daily_sales = np.random.choice(
  list(range(1,9)), 
  days,
  p=sales_probs
  )


def daily_bonus(n): 
    if n <= 4:
        return 0
    
    bonuses = np.random.choice(
      bonus_vals, 
      n,
      p=bonus_probs
      )
    
    return sum(bonuses)

bonus_history = [daily_bonus(n) for n in daily_sales]

SD = np.std(bonus_history)
print("std: ", SD)
standard_error = SD/np.sqrt(days)
print("mean bonus: ", np.mean(bonus_history))
