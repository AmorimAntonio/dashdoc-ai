# Visão Geral do Dashboard
O dashboard "PBI Assemat Empréstimos" é uma ferramenta desenvolvida para fornecer uma visão abrangente sobre o status dos empréstimos dentro da organização. Ele serve para monitorar métricas críticas relacionadas a dívidas, como total de dívida, dívida em cobrança e dívida em atraso. O público-alvo deste dashboard é a equipe de Gestão de Empréstimos e Finanças, que pode utilizá-lo para tomar decisões informadas sobre a administração de empréstimos e estratégias de cobrança.

Este dashboard é essencial para identificar tendências e padrões nos empréstimos, permitindo que a equipe de finanças ajuste suas estratégias conforme necessário. Ele também facilita o acompanhamento do desempenho das filiais e a análise do impacto financeiro dos empréstimos em atraso.

# Objetivo de Negócio
- Monitorar o total de dívida por categoria.
- Acompanhar a evolução da dívida em cobrança e em atraso.
- Avaliar o desempenho das filiais em relação à gestão de empréstimos.
- Identificar tendências e padrões nos empréstimos ao longo do tempo.
- Auxiliar na tomada de decisões estratégicas para a gestão de dívidas.

# Principais KPIs e Indicadores
- **Total de Dívida:** Representa o valor total de empréstimos pendentes.
- **Dívida em Cobrança:** Indica o montante de dívida atualmente em processo de cobrança.
- **Dívida em Atraso:** Reflete o valor de empréstimos que estão atrasados.
- **Número de Trabalhadores:** Mostra a quantidade de trabalhadores associados aos empréstimos.
- **Ticket Médio:** Calcula o valor médio dos empréstimos concedidos.

# Descrição das Visualizações

## Status

![Status](../images/PBI_Assemat_Emprestimos_graph_0.png)


**Tipo:** Donut

Este gráfico de donut apresenta a distribuição percentual dos empréstimos por status, como ativos, em cobrança ou em atraso. Ele oferece uma visão rápida da proporção de cada categoria em relação ao total de empréstimos.

### Como interpretar:
- Identifique rapidamente a maior categoria de status de empréstimos.
- Avalie a proporção de empréstimos em atraso em comparação com os ativos.
- Use para priorizar ações de cobrança ou renegociação.

## Dias Após Rescisão

![Dias Após Rescisão](../images/PBI_Assemat_Emprestimos_graph_1.png)


**Tipo:** Barra

O gráfico de barras mostra a quantidade de dias após a rescisão dos contratos de empréstimo, permitindo a análise do tempo médio de atraso.

### Como interpretar:
- Observe o tempo médio de atraso dos empréstimos.
- Identifique picos de atraso que possam necessitar de atenção especial.
- Compare o desempenho de diferentes períodos ou categorias.

## Filial Employer

![Filial Employer](../images/PBI_Assemat_Emprestimos_graph_2.png)


**Tipo:** Barra

Este gráfico de barras ilustra o desempenho de diferentes filiais em termos de gestão de empréstimos, destacando o total de dívida por filial.

### Como interpretar:
- Compare o desempenho das filiais em termos de volume de dívida.
- Identifique filiais com maior necessidade de intervenção.
- Avalie a eficácia das estratégias de cobrança por filial.

## Evolução

![Evolução](../images/PBI_Assemat_Emprestimos_graph_3.png)


**Tipo:** Linha

O gráfico de linha mostra a evolução temporal dos empréstimos, destacando tendências e variações ao longo do tempo.

### Como interpretar:
- Identifique tendências de aumento ou redução na dívida ao longo do tempo.
- Avalie o impacto de eventos sazonais ou econômicos nas métricas de empréstimo.
- Use para prever tendências futuras e ajustar estratégias.

# Filtros e Interações
O dashboard oferece filtros por período, filial e status do empréstimo. Esses filtros permitem que os usuários ajustem as visualizações para focar em segmentos específicos de interesse, afetando diretamente os dados exibidos nos gráficos.

# Fluxo de Uso Recomendado
1. Inicie revisando o gráfico de **Status** para entender a distribuição geral dos empréstimos.
2. Use o gráfico de **Dias Após Rescisão** para identificar problemas de atraso.
3. Analise o gráfico de **Filial Employer** para avaliar o desempenho por filial.
4. Examine o gráfico de **Evolução** para entender as tendências ao longo do tempo.
5. Ajuste os filtros conforme necessário para aprofundar a análise em áreas específicas.

# Perguntas de Negócio que o Dashboard Responde
- ❓ **Qual é o total de dívida atual?** → Consulte o KPI "Total de Dívida".
- ❓ **Qual é a proporção de dívida em atraso?** → Veja o gráfico de **Status**.
- ❓ **Quais filiais têm o maior volume de dívida?** → Analise o gráfico de **Filial Employer**.
- ❓ **Como a dívida evoluiu nos últimos meses?** → Examine o gráfico de **Evolução**.
- ❓ **Qual é o tempo médio de atraso dos empréstimos?** → Confira o gráfico de **Dias Após Rescisão**.
- ❓ **Como a dívida em cobrança está distribuída por filial?** → Use o gráfico de **Filial Employer** com o filtro adequado.
- ❓ **Quais são as tendências de dívida por categoria?** → Ajuste os filtros e observe o gráfico de **Evolução**.
- ❓ **Qual é o ticket médio dos empréstimos?** → Consulte o KPI "Ticket Médio".
```