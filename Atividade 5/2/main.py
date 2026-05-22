from estatistica.leitor import ler_csv
from estatistica.analise import estatisticas
import os

pasta_atual = os.path.dirname(__file__)

arquivo_csv = os.path.join(pasta_atual, "dados.csv")

dados = ler_csv(arquivo_csv)

print("Dados:")
print(dados)

resultado = estatisticas(dados, "idade")

print("\nEstatísticas:")
print(resultado)