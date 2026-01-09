class pokemon:
    def __init__(self,entry, name, types, description, is_caught):
      self.entry = entry
      self.name = name
      self.types = types
      self.description = description
      self.is_caught = is_caught

    def display_details(self):
      if not self.is_caught:
        print ('This pokemon is not cought yet!')
      print(f'Entry number: {self.entry}')
      print(f'Name: {self.name}')
      print(f'Type: {self.types}')
      print(f'Description: {self.description}')
      print(f'Is caught: {self.is_caught}')
    
    def speak(self):
      print(f'This pokemon sound is:{self.name, self.name}!')

charmander = pokemon(
  '4',
  'Charmander',
  'Fire',
  'The flame on its tail shows the strength of its life-force. If Charmander is weak, the flame also burns weakly.',
  True
)

squirtle = pokemon(
  '7',
  'Squirtle',
  'Water',
  'After birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.',
  False
)

jigglypuff = pokemon(
  '39',
  'Jigglypuff',
  'Fairy',
  'When its huge eyes waver, it sings a mysteriously soothing melody that lulls its enemies to sleep.',
  False
)

gengar = pokemon(
  '94',
  'Gengar',
  'Shadow',
  'To steal the life of its target, it slips into the prey’s shadow and silently waits for an opportunity.',
  True
)

charmander.display_details()
charmander.speak()

squirtle.display_details()
squirtle.speak()

jigglypuff.display_details()
jigglypuff.speak()

gengar.display_details()
gengar.speak()
