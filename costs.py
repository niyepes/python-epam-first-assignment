def get_total(costs, items, tax):
    subtotal = sum(costs[item] for item in items if item in costs)
    return round(subtotal * (1 + tax), 2)
 
 
costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
print(get_total(costs, ['socks', 'shoes'], 0.09))
 
