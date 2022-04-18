# try to import statsapi; install if not already   - https://pypi.org/project/MLB-StatsAPI/
try:
    import statsapi
except ImportError:
    import pip
    pip.main(['install', 'mlb-statsapi'])
    import statsapi

#try to import pulp, install if not already
try:
    from pulp import * 
except ImportError:
    import pip
    pip.main(['install', 'pulp'])
    from pulp import *


import requests

import pandas as pd
import numpy as np
import pulp

# i belive requires auth to api
roster = requests.get("https://www.baseball-reference.com/teams/CHW/2019-roster.shtml#appearances")
roster.content

''' some of the base functions (https://github.com/toddrob99/MLB-StatsAPI/blob/554aa3cf1ab7ceec537cba58d408d93e98ef523b/statsapi/__init__.py) 
    were built to call `get`s to the `endpoints: https://github.com/toddrob99/MLB-StatsAPI/wiki/Endpoints
    may be easier to just call the endpoints themselvs from the get funciont
'''

teams = statsapi.lookup_team(1)
for team in teams:
  if team['teamCode']=='cha':
    team_dict = team

team_dict

# roster for selected year
print(statsapi.roster(team_dict['id'], 2019))

