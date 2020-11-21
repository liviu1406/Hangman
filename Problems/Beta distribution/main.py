import random


random.seed(3)
# call the function here
gen = random.betavariate(alpha=0.9, beta=0.1)
print(gen)