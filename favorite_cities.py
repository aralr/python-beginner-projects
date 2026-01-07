class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

cdmx = City(
  'Ciudad de Mexico',
  'Mexico',
  '9.3',
  ['Bosque de Chapultepec',
  'Mi casita',
  'Museo Frida Khalo']
)

sao_paulo = City(
  'Sao Paulo',
  'Brazil',
  '12.3',
  ['Museu de Arte de Sao Paulo Assis Chateaubriand',
  'Parque do Ibirapuera',
  'Morumbi']
)

tokio = City(
  'Tokio',
  'Japon',
  '14.0',
  ['Tokio tower',
  'Mori Art Museum',
  'Shibuya']
)

shenzhen = City(
  'Shenzhen',
  'China',
  '17.99',
  ['Hong Kong Wetland Park',
  'Window of the World',
  'COCO Park']
)

paris = City(
  'Paris',
  'France',
  '2.2',
  ['Louvre Museum',
  'Tour Eiffel',
  'Montparnasse park']
)

print(vars(cdmx))
print(vars(sao_paulo))
print(vars(tokio))
print(vars(shenzhen))
print(vars(paris))
