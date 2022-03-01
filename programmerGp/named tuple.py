from collections import namedtuple as nt

animal = nt('animal', 'name age type color')
sample = animal(name = 'heli', age = '21', type = 'cat', color = 'red')

print(sample.type)
