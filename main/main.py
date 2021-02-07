if __name__ == '__main__':
    watts = input('Type watts: ')
    watts = int(watts)
  
    if watts <= 200:
        cost = watts * .25
    elif watts <= 1200:
        cost = 200 * .25
        watts = watts - 200
        cost = cost + watts * .4
    else:
        cost = 200 * .25
        watts = watts - 200
        cost = 1000 * .4 + cost
        watts = watts - 1000
        cost = cost + watts * .5
    print(cost)
