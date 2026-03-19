
# Visão Geral do Dashboard

O dashboard "PBI Assemat Empréstimos" é uma ferramenta analítica projetada para fornecer uma visão abrangente sobre o estado dos empréstimos geridos pela equipe de Gestão de Empréstimos e Finanças. Ele oferece insights detalhados sobre métricas críticas, como o total de dívida, dívida em cobrança e dívida em atraso, permitindo uma análise aprofundada do desempenho financeiro.

Destinado principalmente para a equipe de Gestão de Empréstimos e Finanças, o dashboard facilita o monitoramento contínuo das métricas de empréstimos, ajudando na tomada de decisões estratégicas e operacionais. Ele é essencial para entender o panorama atual dos empréstimos e identificar áreas que necessitam de atenção imediata.

# Objetivo de Negócio

- Monitorar o total de dívida por categoria.
- Analisar a dívida em cobrança e identificar tendências.
- Avaliar a dívida em atraso para ações corretivas.
- Acompanhar o desempenho por filial.
- Auxiliar na alocação de recursos humanos com base no número de trabalhadores.

# Principais KPIs e Indicadores

- **Total de Dívida**: Representa o valor total dos empréstimos pendentes.
- **Dívida em Cobrança**: Indica o montante de dívida atualmente em processo de cobrança.
- **Dívida em Atraso**: Reflete o valor dos empréstimos que estão atrasados.
- **Número de Trabalhadores**: Quantidade de funcionários envolvidos na gestão dos empréstimos.
- **Ticket Médio**: Valor médio dos empréstimos concedidos.

# Descrição das Visualizações

## Status

![Status](../images/PBI_Assemat_Emprestimos_graph_0.png)


**Tipo:** Donut

Este gráfico de donut ilustra a distribuição percentual das diferentes categorias de status dos empréstimos, como ativos, em cobrança e atrasados, proporcionando uma visão clara da composição atual dos empréstimos.

### Como interpretar:

- Identificar a proporção de empréstimos em cada status.
- Avaliar rapidamente a saúde geral da carteira de empréstimos.
- Comparar a quantidade de empréstimos ativos versus aqueles em cobrança ou atraso.

## Dias Após Rescisão

![Dias Após Rescisão](../images/PBI_Assemat_Emprestimos_graph_1.png)


**Tipo:** Barra

O gráfico de barras mostra a quantidade de dias após a rescisão dos contratos de empréstimo, permitindo a análise do tempo médio que leva para que um empréstimo seja encerrado após a rescisão.

### Como interpretar:

- Identificar padrões de tempo de rescisão.
- Avaliar se há um aumento no tempo médio de rescisão.
- Comparar diferentes períodos para detectar mudanças no comportamento.

## Filial Employer

![Filial Employer](../images/PBI_Assemat_Emprestimos_graph_2.png)


**Tipo:** Barra

Este gráfico de barras apresenta a distribuição dos empréstimos por filial, permitindo a comparação do desempenho entre diferentes locais de operação.

### Como interpretar:

- Determinar quais filiais têm o maior volume de empréstimos.
- Avaliar o desempenho relativo entre as filiais.
- Identificar filiais que podem necessitar de suporte adicional.

## Evolução

![Evolução](../images/PBI_Assemat_Emprestimos_graph_3.png)


**Tipo:** Linha

O gráfico de linha mostra a evolução temporal das métricas principais, como total de dívida e dívida em atraso, destacando tendências e mudanças ao longo do tempo.

### Como interpretar:

- Observar tendências de aumento ou diminuição nas métricas.
- Identificar períodos de pico ou queda nas atividades de empréstimo.
- Analisar o impacto de eventos específicos nas métricas ao longo do tempo.

# Filtros e Interações

O dashboard oferece filtros por período, categoria de empréstimo e filial, permitindo que os usuários ajustem as visualizações para focar em segmentos específicos de interesse. Esses filtros afetam todas as visualizações, proporcionando uma análise detalhada e personalizada.

# Fluxo de Uso Recomendado

1. Inicie revisando o gráfico de **Status** para entender a distribuição atual dos empréstimos.
2. Utilize os filtros para ajustar o período e a filial de interesse.
3. Analise o gráfico de **Dias Após Rescisão** para insights sobre o tempo de rescisão.
4. Compare o desempenho entre filiais usando o gráfico de **Filial Employer**.
5. Observe tendências ao longo do tempo no gráfico de **Evolução**.

# Perguntas de Negócio que o Dashboard Responde

- **Qual é o status atual da carteira de empréstimos?** → Verifique o gráfico de Status.
- **Qual é o tempo médio de rescisão dos empréstimos?** → Consulte o gráfico de Dias Após Rescisão.
- **Quais filiais estão performando melhor?** → Analise o gráfico de Filial Employer.
- **Como a dívida em atraso evoluiu nos últimos meses?** → Veja o gráfico de Evolução.
- **Qual é o valor total da dívida em cobrança?** → Confira o KPI de Dívida em Cobrança.
- **Como o ticket médio varia entre as filiais?** → Use os filtros para ajustar por filial e observe os KPIs.
- **Quais são as tendências recentes nos empréstimos?** → Analise o gráfico de Evolução.
- **Há um aumento na dívida em atraso?** → Compare os dados históricos no gráfico de Evolução.
```
