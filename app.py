"""Ponto de entrada do dashboard de vendas.

Execução: ``streamlit run app.py``
"""

from __future__ import annotations

import sys
from pathlib import Path

# Garante que o pacote em src/ seja importável quando executado via Streamlit.
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

import pandas as pd
import plotly.express as px  # noqa: E402  (import após ajuste de sys.path)
import streamlit as st  # noqa: E402

from dashboard_vendas.agregacoes import (  # noqa: E402
    agregar_por_produto,
    agregar_por_regiao,
    agregar_por_tempo,
)
from dashboard_vendas.charts import (  # noqa: E402
    fig_vendas_por_produto,
    fig_vendas_por_regiao,
    fig_vendas_por_tempo,
)
from dashboard_vendas.data import gerar_dados_vendas  # noqa: E402


def _filtros_sidebar(df: pd.DataFrame) -> pd.DataFrame:
    """Renderiza os filtros da sidebar e retorna o DataFrame filtrado."""
    with st.sidebar:
        st.header("Filtros")

        produtos = sorted(df["produto"].unique().tolist())
        produtos_sel = st.multiselect("Produto", produtos, default=produtos)

        regioes = sorted(df["regiao"].unique().tolist())
        regioes_sel = st.multiselect("Região", regioes, default=regioes)

        data_min = pd.to_datetime(df["data"].min()).date()
        data_max = pd.to_datetime(df["data"].max()).date()
        periodo = st.date_input(
            "Período",
            value=(data_min, data_max),
            min_value=data_min,
            max_value=data_max,
        )

    mascara = df["produto"].isin(produtos_sel) & df["regiao"].isin(regioes_sel)
    if len(periodo) == 2:
        inicio, fim = pd.to_datetime(periodo[0]), pd.to_datetime(periodo[1])
        mascara = mascara & (df["data"] >= inicio) & (df["data"] <= fim)

    return df.loc[mascara]


def _kpis(df: pd.DataFrame) -> None:
    """Exibe os cartões de indicadores-chave."""
    total_vendas = float(df["valor_total"].sum()) if not df.empty else 0.0
    total_itens = int(df["quantidade"].sum()) if not df.empty else 0
    ticket_medio = total_vendas / len(df) if len(df) else 0.0

    col1, col2, col3 = st.columns(3)
    col1.metric("Total de vendas", f"R$ {total_vendas:,.2f}")
    col2.metric("Itens vendidos", total_itens)
    col3.metric("Ticket médio", f"R$ {ticket_medio:,.2f}")


def main() -> None:
    """Executa o dashboard."""
    st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
    st.title("Dashboard de Vendas")
    st.caption("Vendas por produto, região e tempo — com filtros interativos.")

    df = gerar_dados_vendas()
    df_filtrado = _filtros_sidebar(df)

    st.divider()
    _kpis(df_filtrado)

    st.subheader("Vendas por produto")
    st.plotly_chart(fig_vendas_por_produto(df_filtrado), use_container_width=True)

    st.subheader("Vendas por região")
    st.plotly_chart(fig_vendas_por_regiao(df_filtrado), use_container_width=True)

    st.subheader("Vendas ao longo do tempo")
    st.plotly_chart(fig_vendas_por_tempo(df_filtrado), use_container_width=True)

    st.subheader("Detalhe das vendas")
    st.dataframe(
        df_filtrado.sort_values("data", ascending=False),
        use_container_width=True,
        hide_index=True,
    )


if __name__ == "__main__":
    main()
