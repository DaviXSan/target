def analisa_faturamento(faturamento_diario):
    """
    Args:
        faturamento_diario: Uma lista com os valores de faturamento diário.

    Returns:
        tuple: Uma tupla contendo o menor valor, o maior valor e o número de dias acima da média.
    """

    # média mensal
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)

    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)

    # dias com faturamento acima da média
    dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_media

# Exemplo de uso:
faturamento = [1000, 1500, 2000, 500, 1200]
menor, maior, dias_acima = analisa_faturamento(faturamento)

print("Menor valor de faturamento:", menor)
print("Maior valor de faturamento:", maior)
print("Número de dias com faturamento acima da média:", dias_acima)
