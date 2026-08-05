
from kaggle_environments import make

from agent import wheat_loop

AGENTS = [wheat_loop, "random"]

env = make('kaggriculture', debug=True)
env.run(AGENTS)

print([(agent.__name__ if callable(agent) else str(agent), s["reward"]) 
				for agent, s in zip(AGENTS, env.steps[-1])])