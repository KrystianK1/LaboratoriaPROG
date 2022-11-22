sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
for key in sample_dict.keys():
 print(f'{key:<10} = {sample_dict[key]:>10}')

for k,v in sample_dict.items():
 print(f'{k:<10} = {v:>10}')

l = ['name','age','abc']
d ={}
for i in l:
 if i in sample_dict:
  d[i]=sample_dict[i]
  print(d)
for d in l:
 x=sample_dict.pop(d, 'błąd')
 print(x)
for i in sample_dict.values():
 if i=="Jones":
  break
