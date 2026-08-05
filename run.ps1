python -c @"
from kaggle_environments import make
env = make('kaggriculture', debug=True)
env.run(['agent.py', 'random'])
print([(i, s.reward) for i, s in enumerate(env.steps[-1])])
"@
