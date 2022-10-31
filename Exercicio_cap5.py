import pandas as pd
import numpy as np

# Importando o csv
dfPaises = pd.read_csv('Paises.csv', delimiter=';')
print(dfPaises.head(0))



# Exércicio 1 
print('\033[1m' + 'Exercício 1' + '\033[0m')
print()

print('\033[1m' + 'a)' + '\033[0m')
paisesOceania = dfPaises.loc[dfPaises['Region'].str.contains("OCEANIA")]
print(paisesOceania['Country'])
print()

print('\033[1m' + 'b)' + '\033[0m')
quantPaisesOceania = len(paisesOceania['Country'])
print(f"Há {quantPaisesOceania} países da Oceania.")
print()



# Exércicio 2
print('\033[1m' + 'Exercício 2' + '\033[0m')
print()

worldLiteracy = dfPaises.iloc[:,9]
serie_worldLiteracy = pd.Series(worldLiteracy)
print(f"A média da taxa de alfabetização do planeta é {serie_worldLiteracy.mean()}%.")
print()



# Exércicio 3
print('\033[1m' + 'Exercício 3' + '\033[0m')
print()

indice = dfPaises['Population'].idxmax()
regiao = dfPaises['Region'].values[indice]
pais = dfPaises['Country'].values[indice]
maiorPopulacao = dfPaises['Population'].values[indice]

print(f" O pais com a maior populção é a {pais}, que se localiza na {regiao}. A {pais} conta com uma população de {maiorPopulacao} habitantes.")
print()



# Exércicio 4
print('\033[1m' + 'Exercício 4' + '\033[0m')
print()

p_SemCosta = dfPaises.loc[dfPaises['Coastline (coast/area ratio)'] == 0]
paisesSemCosta = p_SemCosta ['Country']
print(paisesSemCosta)

paisesSemCosta.to_csv('paisesSemCosta.csv', sep=';', header=False)
