print('Welcome to PyPet!')

name= 'Pymon'
age= 0
weight= 0.1
hungry= True
photo= '<x3 )~~~'

Rat= {
  'name': 'Pymon',
  'hungry': True,
  'weight': 0.1,
  'age': 0,
  'photo': '<x3  )~~~',
}
print ('Yo '+ Rat['name'])
print (Rat['photo'])

def feed(Rat):
 if Rat['hungry'] == True:
  Rat['hungry'] = False
  Rat['weight'] = Rat['weight'] + 1
 else:
  print ('The Pypet is not hungry!')


print (Rat)
feed(Rat)
print (Rat)
feed(Rat)