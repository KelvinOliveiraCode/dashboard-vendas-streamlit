"""Agregações de vendas por produto, região e tempo."""

from __future__ import annotations

import pandas as pd


def agregar_por_produto(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega valor total, quantidade e número de pedidos por produto."""
    if df.empty:
        return pd.DataFrame(columns=["produto", "vendas", "quantidade", "pedidos"])
    return (
        df.groupby("produto", as_index=False)
        .agg(
            vendas=("valor_total", "sum"),
            quantidade=("quantidade", "sum"),
            pedidos=("id", "nunique"),
        )
        .sort_values("vendas", ascending=False)
        .reset_index(drop=True)
    )


def agregar_por_regiao(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega valor total, quantidade e número de pedidos por região."""
    if df.empty:
        return pd.DataFrame(columns=["regiao", "vendas", "quantidade", "pedidos"])
    return (
        df.groupby("regiao", as_index=False)
        .agg(
            vendas=("valor_total", "sum"),
            quantidade=("quantidade", "sum"),
            pedidos=("id", "nunique"),
        )
        .sort_values("vendas", ascending=False)
        .reset_index(drop=True)
    )


def agregar_por_tempo(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega valor total e quantidade por dia."""
    if df.empty:
        return pd.DataFrame(columns=["data", "vendas", "quantidade"])
    return (
        df.groupby("data", as_index=False)
        .agg(vendas=("valor_total", "sum"), quantidade=("quantidade", "sum"))
        .sort_values("data")
        .reset_index(drop=True)
    )
