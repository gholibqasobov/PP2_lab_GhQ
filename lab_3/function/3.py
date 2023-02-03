# every animal has two legs, so multiply num of heads by 2
# 35 * 2 = 70
# subtract from total num
# 94 - 70 = 24
# number of rabbits is 24/2
# since chickens don't have front legs, subtract the number of rabbits
# from the total num of heads,
# 35 - 24 = 11
# num of chicken


def solve(numheads, numlegs):
    legs = numheads * 2
    print(legs)
    rabbit = (numlegs - legs) // 2
    print(rabbit)
    chicken = numheads - rabbit
    print(chicken)
    return rabbit, chicken


print(solve(35, 94))
