d = {'first_good': None,
     'second_good': 123,
     'third_good': None
     }

print(len(d.keys()))
a = [i for i in d.values() if i]
print(a)