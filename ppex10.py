import random

list_a = random.sample(range(1, 101), random.randint(20, 40))
list_b = random.sample(range(1, 101), random.randint(20, 40))
list_c = [i for i in list_a if i in list_b]

print(list_c)
