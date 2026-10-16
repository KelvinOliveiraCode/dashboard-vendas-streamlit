"""Testes das agregações e geração de dados do dashboard de vendas.

Cada teste cobre um comportamento real do código de produção, sem mocks.
"""

from __future__ import annotations

import pandas as pd

from dashboard_vendas.agregacoes import (
    agregar_por_produto,
    agregar_por_regiao,
    agregar_por_tempo,
)
from dashboard_vendas.data import gerar_dados_vendas

COLUNAS_ESPERADAS = [
    "id",
    "produto",
    "regiao",
    "data",
    "quantidade",
    "valor_unitario",
    "valor_total",
]


def test_gerar_dados_retorna_dataframe_com_colunas_esperadas():
    """O DataFrame gerado deve conter todas as colunas do contrato de dados."""
    df = gerar_dados_vendas()
    assert not df.empty
    for coluna in COLUNAS_ESPERADAS:
        assert coluna in df.columns


def test_gerar_dados_gera_linhas_positivas():
    """O DataFrame gerado deve ter número de linhas maior que zero."""
    df = gerar_dados_vendas()
    assert len(df) > 0


def test_gerar_dados_e_determinista_por_seed():
    """Mesma seed deve produzir exatamente o mesmo DataFrame."""
    primeiro = gerar_dados_vendas(seed=7)
    segundo = gerar_dados_vendas(seed=7)
    assert primeiro.equals(segundo)


def test_gerar_dados_seeds_diferentes_produzem_resultados_diferentes():
    """Seeds diferentes devem produzir DataFrames diferentes (não colisão)."""
    assert not gerar_dados_vendas(seed=1).equals(gerar_dados_vendas(seed=2))


def test_agregacao_por_produto_soma_valores_da_fonte():
    """A soma de vendas por produto deve bater com o total do DataFrame."""
    df = gerar_dados_vendas()
    res = agregar_por_produto(df)
    assert not res.empty
    assert list(res.columns) == ["produto", "vendas", "quantidade", "pedidos"]
    total_fonte = float(df["valor_total"].sum())
    total_agregado = float(res["vendas"].sum())
    assert abs(total_fonte - total_agregado) < 1e-6


def test_agregacao_por_produto_ordenada_decrescente():
    """O resultado por produto deve vir ordenado do maior para o menor valor."""
    df = gerar_dados_vendas()
    res = agregar_por_produto(df)
    vendas = res["vendas"].tolist()
    assert vendas == sorted(vendas, reverse=True)


def test_agregacao_por_regiao_soma_valores_da_fonte():
    """A soma de vendas por região deve bater com o total do DataFrame."""
    df = gerar_dados_vendas()
    res = agregar_por_regiao(df)
    assert not res.empty
    assert list(res.columns) == ["regiao", "vendas", "quantidade", "pedidos"]
    total_fonte = float(df["valor_total"].sum())
    total_agregado = float(res["vendas"].sum())
    assert abs(total_fonte - total_agregado) < 1e-6


def test_agregacao_por_tempo_soma_valores_da_fonte():
    """A soma de vendas por dia deve bater com o total do DataFrame."""
    df = gerar_dados_vendas()
    res = agregar_por_tempo(df)
    assert not res.empty
    assert list(res.columns) == ["data", "vendas", "quantidade"]
    total_fonte = float(df["valor_total"].sum())
    total_agregado = float(res["vendas"].sum())
    assert abs(total_fonte - total_agregado) < 1e-6


def test_agregacao_por_tempo_ordenada_cronologicamente():
    """O resultado por tempo deve vir ordenado do mais antigo para o mais recente."""
    df = gerar_dados_vendas()
    res = agregar_por_tempo(df)
    datas = res["data"].tolist()
    assert datas == sorted(datas)


def test_dataframe_vazio_retorna_agregacao_por_produto_vazia():
    """DataFrame vazio não deve quebrar a agregação por produto."""
    vazio = pd.DataFrame(columns=COLUNAS_ESPERADAS)
    res = agregar_por_produto(vazio)
    assert res.empty


def test_dataframe_vazio_retorna_agregacao_por_regiao_vazia():
    """DataFrame vazio não deve quebrar a agregação por região."""
    vazio = pd.DataFrame(columns=COLUNAS_ESPERADAS)
    res = agregar_por_regiao(vazio)
    assert res.empty


def test_dataframe_vazio_retorna_agregacao_por_tempo_vazia():
    """DataFrame vazio não deve quebrar a agregação por tempo."""
    vazio = pd.DataFrame(columns=COLUNAS_ESPERADAS)
    res = agregar_por_tempo(vazio)
    assert res.empty
