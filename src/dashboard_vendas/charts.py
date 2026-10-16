"""Gráficos Plotly usados pelo dashboard de vendas."""

from __future__ import annotations

import pandas as pd
import plotly.express as px

from dashboard_vendas.agregacoes import (
    agregar_por_produto,
    agregar_por_regiao,
    agregar_por_tempo,
)


def fig_vendas_por_produto(df: pd.DataFrame):
    """Gráfico de barras: vendas totais por produto."""
    dados = agregar_por_produto(df)
    fig = px.bar(
        dados,
        x="produto",
        y="vendas",
        text="vendas",
        labels={"produto": "Produto", "vendas": "Vendas (R$)"},
        title="Vendas por produto",
    )
    fig.update_traces(texttemplate="R$ %{text:,.2f}", textposition="outside")
    fig.update_layout(uniformtext_minsize=10, uniformtext_mode="hide", showlegend=False)
    return fig


def fig_vendas_por_regiao(df: pd.DataFrame):
    """Gráfico de barras: vendas totais por região."""
    dados = agregar_por_regiao(df)
    fig = px.bar(
        dados,
        x="regiao",
        y="vendas",
        text="vendas",
        labels={"regiao": "Região", "vendas": "Vendas (R$)"},
        title="Vendas por região",
    )
    fig.update_traces(texttemplate="R$ %{text:,.2f}", textposition="outside")
    fig.update_layout(uniformtext_minsize=10, uniformtext_mode="hide", showlegend=False)
    return fig


def fig_vendas_por_tempo(df: pd.DataFrame):
    """Gráfico de linha: vendas ao longo do tempo."""
    dados = agregar_por_tempo(df)
    fig = px.line(
        dados,
        x="data",
        y="vendas",
        markers=True,
        labels={"data": "Data", "vendas": "Vendas (R$)"},
        title="Vendas ao longo do tempo",
    )
    fig.update_traces(line_shape="spline")
    fig.update_layout(hovermode="x unified")
    return fig
