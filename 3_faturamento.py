import json
import xml.etree.ElementTree as ET
from google.colab import drive

def analisar_faturamento(arquivo, formato):
    """
    Analisa o faturamento diário de uma distribuidora a partir de um arquivo JSON ou XML.

    Args:
        arquivo: Nome do arquivo com os dados do faturamento.
        formato: Formato do arquivo (json ou xml).

    Returns:
        tuple: Uma tupla contendo o menor valor, o maior valor e a quantidade de dias com faturamento acima da média.
    """

    faturamentos = []
    if formato == 'json':
        with open(arquivo, 'r') as f:
            dados = json.load(f)
            faturamentos = [dado['valor'] for dado in dados if 'valor' in dado]
    elif formato == 'xml':
        tree = ET.parse(arquivo)
        root = tree.getroot()
        faturamentos = [float(elemento.text) for elemento in root.iter('valor') if elemento.text]
    else:
        raise ValueError("Formato de arquivo inválido.")

    # Ignorar valores nulos ou negativos
    faturamentos = [valor for valor in faturamentos if valor > 0]

    # Calcular a média, o menor e o maior valor
    media = sum(faturamentos) / len(faturamentos)
    menor_valor = min(faturamentos)
    maior_valor = max(faturamentos)
    dias_acima_media = sum(1 for valor in faturamentos if valor > media)

    return menor_valor, maior_valor, dias_acima_media

# Exemplo de uso
arquivo = 'faturamento.json'  # Substitua pelo nome do seu arquivo
formato = 'json'  # Altere para 'xml' se necessário

menor, maior, dias_acima = analisar_faturamento(arquivo, formato)

print(f"Menor valor de faturamento: R$ {menor:.2f}")
print(f"Maior valor de faturamento: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")
