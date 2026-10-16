# Brief — dashboard-vendas-streamlit (Dados/BI)

## Entregas

Projeto de dashboard interativo de vendas com Streamlit + Plotly, conforme PLANO_50_PROJETOS.md (projeto 28, área Dados/BI).

Arquivos criados:

- `app.py` — ponto de entrada do dashboard (`streamlit run app.py`)
- `pyproject.toml` — metadados e dependências (streamlit, plotly, pandas)
- `.gitignore` — venv, cache, pyc, env
- `README.md` — documentação bilíngue PT-BR + EN
- `BRIEF.md` — este resumo
- `src/dashboard_vendas/__init__.py` — pacote
- `src/dashboard_vendas/data.py` — geração determinística de dados de vendas (seed fixa)
- `src/dashboard_vendas/agregacoes.py` — agregações por produto, região e tempo
- `src/dashboard_vendas/charts.py` — gráficos Plotly (barras produto/região, linha tempo)
- `conftest.py` — torna `src/` importável nos testes
- `tests/test_agregacoes.py` — suíte pytest (12 testes)

## Como verificar

1. Instale as dependências:

   ```bash
   pip install streamlit plotly pandas
   ```

2. Rode o dashboard localmente:

   ```bash
   streamlit run app.py
   ```

3. Rode a suíte de testes:

   ```bash
   python -m pytest -q
   ```

## Resultado dos testes

Comando: `python -m pytest -q`

Resultado: **12 passed** (todos os testes verdes).

Critérios de aceitação atendidos: dashboard roda localmente, testes que passam, README PT/EN completo, licença MIT, autor Kelvin Oliveira.
