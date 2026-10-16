# Dashboard de Vendas / Sales Dashboard

Dashboard interativo de vendas com Streamlit + Plotly. Visualiza vendas por produto, região e tempo, com filtros de produto, região e período.

Interactive sales dashboard with Streamlit + Plotly. Visualizes sales by product, region, and time, with product, region, and period filters.

## Stack / Stack

Python, Streamlit, Plotly, pandas.

## Como usar / How to use

Instale as dependências:

Install dependencies:

```bash
pip install streamlit plotly pandas
```

Rode o dashboard:

Run the dashboard:

```bash
streamlit run app.py
```

## Testes / Tests

Rode a suíte de testes:

Run the test suite:

```bash
python -m pytest -q
```

Os testes geram um DataFrame de vendas e verificam as agregações por produto, região e tempo.

Tests generate a sales DataFrame and verify aggregations by product, region, and time.

## Estrutura / Structure

- `app.py` — ponto de entrada do dashboard (Streamlit)
- `src/dashboard_vendas/` — geração de dados, agregações e gráficos
- `tests/` — testes pytest

- `app.py` — dashboard entry point (Streamlit)
- `src/dashboard_vendas/` — data generation, aggregations, charts
- `tests/` — pytest tests

## Licença / License

MIT

## Autor / Author

Kelvin Oliveira
