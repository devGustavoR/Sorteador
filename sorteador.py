# Importações
import random

jogadores = ['Igor', 'Gustavo', 'Eros', 'Cassio', 'Nicolas', 'Marlon','Icaro']
geracao = random.randint(1, 6)

# Insignias
insignias1 = ['Boulder Badge','Cascade Badge','Earth Badge','Marsh Badge','Rainbow Badge'
,'Soul Badge','Thunder Badge','Volcano Badge']

insignias2 = ['Zephyr Badge','Hive Badge','Plain Badge','Fog Badge','Storm Badge','Mineral Badge'
,'Glacier Badge','Rising Badge']

insignias3 = ['Stone Badge','Knuckle Badge','Dynamo Badge','Heat Badge','Balance Badge','Feather Badge'
,'Mind Badge','Rain Badge']

insignias4 = ['Coal Badge','Forest Badge','Cobble Badge','Fen Badge','Relic Badge','Mine Badge'
,'Icicle Badge','Beacon Badge']

insignias5 = ['Trio Badge','Basic Badge','Insect Badge','Bolt Badge','Quake Badge	'
,'Jet Badge','Freeze Badge','Legend Badge','Toxic Badge','Wave Badge']

insignias6 = ['Bug Badge','Cliff Badge','Rumble Badge','Plant Badge','Voltage Badge'
,'Fairy Badge','Psychic Badge','Iceberg Badge']


print ('Jogador: ' + jogadores [ random.randrange ( len ( jogadores ))] )
print('Geracao: {}'.format(geracao))
if(geracao == 1):
  print('Insignia: ' + insignias1 [ random.randrange ( len ( insignias1 ))])
if(geracao==2):
  print('Insignia: ' + insignias2 [ random.randrange ( len ( insignias2 ))])
if(geracao==3):
  print('Insignia: ' + insignias3 [ random.randrange ( len ( insignias3 ))])
if(geracao==4):
  print('Insignia: ' + insignias4 [ random.randrange ( len ( insignias4 ))])
if(geracao==5):
  print('Insignia: ' + insignias5 [ random.randrange ( len ( insignias5 ))])
if(geracao==6):
  print('Insignia: ' + insignias6 [ random.randrange ( len ( insignias6 ))])
