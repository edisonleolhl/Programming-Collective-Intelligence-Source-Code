from pprint import pprint

import optimization

domain = [(0, 9)] * (len (optimization.people) * 2)

# random search
s = optimization.randomoptimize (domain, optimization.schedulecost)
print(optimization.schedulecost (s))
pprint (optimization.printschedule (s))

# hillclimb
s = optimization.hillclimb (domain, optimization.schedulecost)
print(optimization.schedulecost (s))
optimization.printschedule (s)

# simulated annealing
s = optimization.annealingoptimize (domain, optimization.schedulecost)
print(optimization.schedulecost (s))
pprint (optimization.printschedule (s))

# genetic algorithms
s = optimization.geneticoptimize (domain, optimization.schedulecost)
# print(optimization.schedulecost(s))
pprint (optimization.printschedule (s))
