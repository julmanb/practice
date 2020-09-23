# Flipping coins

import numpy as np

person1_money = 0
person2_money = 0

for i in range(10000):
    coin1 = np.random.random()
    if coin1 <= 0.5:
        coin1 = 1
    else:
        coin1 = 0

    coin2 = np.random.random()
    if coin2 <= 0.5:
        coin2 = 1
    else:
        coin2 = 0

    if coin1-coin2 == 0:
        person2_money = 1 + person2_money
    else:
        person1_money = 1 + person1_money

print("the second kid wins", person1_money, "and", "The first kid wins", person2_money)
