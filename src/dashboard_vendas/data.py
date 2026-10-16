"""Geração determinística de dados de vendas para o dashboard."""

from __future__ import annotations

import random
from datetime import date, timedelta

import pandas as pd

PRODUTOS = ["Notebook", "Mouse", "Teclado", "Monitor", "Headset"]
REGIOES = ["Sudeste", "Sul", "Nordeste", "Norte", "Centro-Oeste"]
DATA_INICIAL = date(2026, 1, 1)
DATA_FINAL = date(2026, 6, 30)
NUM_VENDAS = 200


def gerar_dados_vendas(seed: int = 42, num_vendas: int = NUM_VENDAS) -> pd.DataFrame:
    """Gera um DataFrame de vendas determinístico (mesma `seed` = mesmo resultado).

    Colunas: id, produto, regiao, data, quantidade, valor_unitario, valor_total.
    """
    rng = random.Random(seed)
    linhas: list[dict] = []
    for i in range(1, num_vendas + 1):
        produto = rng.choice(PRODUTOS)
        regiao = rng.choice(REGIOES)
        dias = rng.randint(0, (DATA_FINAL - DATA_INICIAL).days)
        data_venda = DATA_INICIAL + timedelta(days=dias)
        quantidade = rng.randint(1, 5)
        valor_unitario = round(rng.uniform(50.0, 3000.0), 2)
        valor_total = round(quantidade * valor_unitario, 2)
        linhas.append(
            {
                "id": i,
                "produto": produto,
                "regiao": regiao,
                "data": data_venda,
                "quantidade": quantidade,
                "valor_unitario": valor_unitario,
                "valor_total": valor_total,
            }
        )
    df = pd.DataFrame(linhas)
    df["data"] = pd.to_datetime(df["data"])
    return df
