"""def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


"""
"""
def calculate_probablity(n):

    #n - input number of flips being a head



    bag_size = 10
    if n==1:
        probability_of_coin_picked=(1/(bag_size))+((bag_size-1)*(1/2)*(1/bag_size))
        return probability_of_coin_picked
    else:
        probability_of_coin_picked =calculate_probablity(n-1)+(1/bag_size)+(bag_size-1)*(1/2**n)*(1/bag_size)
        return probability_of_coin_picked




prob = calculate_probablity(3)
print(prob)
"""
# Monte Carlo simulation
# Sample space:
# if coin_is_fair:
import random

bag = [['H', 'T']] * 9 + [['H', 'H']]

n = 0
k = 0

while n < 1000:
    coin = random.choice(bag)

    outcome = [random.choice(coin) for _ in range(5)]

    if outcome == ['H'] * 6:
        n += 1
        last_flip = random.choice(coin)
        if last_flip == 'H':
            k += 1

print(k / n)