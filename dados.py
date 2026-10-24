"""Leitura dos arquivos CSV do projeto."""

import csv
from pathlib import Path

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_CHOCOLATES = PASTA / "chocolates.csv"

def ler_chocolates():
    """Lê o arquivo CSV e retorna uma lista de dicionários."""
    chocolates = []
    try:
        with open(CAMINHO_CHOCOLATES, encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                chocolates.append(linha)
    except FileNotFoundError:
        print(f"Arquivo {CAMINHO_CHOCOLATES} não encontrado.")
    except Exception as error:
        print(f"Ocorreu um erro ao ler o arquivo: {error}")

    return chocolates

