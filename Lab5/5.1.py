values = [10,20,30]
keys = ['ten','twenty','thirty']
d1 = dict(zip(keys, values))
#print(d1)
d1 = {}
for i in range(len(values)):
    d1[keys[i]] = values[i]
d1 = { keys[i]: values[i] for i in range(len(values))}
print(d1)
d2= (dict(forty=40, fifty=50, sixty=60))
print(d2)
d3={}
d3=d1.copy()
d3.update(d2)
print(d3)