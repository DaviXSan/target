def calcular_percentual_faturamento(dados_faturamento):
  # Calcular o faturamento total
  faturamento_total = sum(dados_faturamento.values())
  # Calcular o percentual de cada estado
  percentuais = {}
  for estado, faturamento in dados_faturamento.items():
    percentual = (faturamento / faturamento_total) * 100
    percentuais[estado] = round(percentual, 2)

  return percentuais

# Dados do exemplo
dados = {
  "SP": 67836.43,
  "RJ": 36678.66,
  "MG": 29229.88,
  "ES": 27165.48,
  "Outros": 19849.53
}

# Chamar a função e imprimir os resultados
resultados = calcular_percentual_faturamento(dados)
for estado, percentual in resultados.items():
  print(f"O estado {estado} representou {percentual}% do faturamento total.")
