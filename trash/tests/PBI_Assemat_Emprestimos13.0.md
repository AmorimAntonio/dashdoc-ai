
# Visão Geral do Dashboard
O dashboard "PBI Assemat Empréstimos" é uma ferramenta analítica projetada para fornecer uma visão abrangente sobre o estado dos empréstimos dentro da organização. Ele é essencial para monitorar métricas financeiras críticas, como o total de dívida, dívida em cobrança e dívida em atraso. Destinado principalmente à equipe de Gestão de Empréstimos e Finanças, o dashboard facilita a análise detalhada e o acompanhamento das operações de crédito.

Este dashboard serve como um recurso vital para a equipe de gestão, permitindo uma análise aprofundada das dívidas por categoria, além de oferecer insights sobre o desempenho financeiro e operacional. Ele é projetado para ajudar na tomada de decisões estratégicas, garantindo que a equipe esteja sempre informada sobre o status atual das dívidas e suas implicações financeiras.

# Objetivo de Negócio
- Monitorar o total de dívida e identificar tendências ao longo do tempo.
- Acompanhar a dívida em cobrança e em atraso para otimizar processos de recuperação.
- Analisar o desempenho das filiais em relação à gestão de empréstimos.
- Avaliar o impacto dos dias após rescisão nos índices de inadimplência.
- Fornecer insights sobre o ticket médio para ajustes estratégicos.

# Principais KPIs e Indicadores
- **Total de Dívida:** Representa o valor acumulado de todos os empréstimos concedidos.
- **Dívida em Cobrança:** Refere-se ao montante de dívida atualmente em processo de cobrança.
- **Dívida em Atraso:** Indica o valor total de empréstimos que estão atrasados.
- **Número de Trabalhadores:** Quantidade de trabalhadores envolvidos na gestão de empréstimos.
- **Ticket Médio:** Valor médio dos empréstimos concedidos.

# Descrição das Visualizações

## Status

![Status](../images/PBI_Assemat_Emprestimos_0.png)


**Tipo:** Donut

Este gráfico de donut fornece uma visão rápida da distribuição dos empréstimos por status, permitindo identificar rapidamente a proporção de dívidas em cobrança, em atraso e quitadas.

### Como interpretar:

- Visualizar a proporção de dívidas em diferentes status.
- Identificar rapidamente áreas que necessitam de atenção, como alta proporção de dívidas em atraso.
- Comparar a distribuição atual com períodos anteriores para identificar tendências.

## Dias Após Rescisão

![Dias Após Rescisão](../images/PBI_Assemat_Emprestimos_1.png)


**Tipo:** Barra

O gráfico de barras "Dias Após Rescisão" mostra a quantidade de dias que se passaram desde a rescisão de contratos, correlacionando com o impacto nos índices de inadimplência.

### Como interpretar:

- Avaliar o impacto do tempo após rescisão nos índices de inadimplência.
- Identificar padrões de atraso relacionados ao tempo decorrido após rescisão.
- Comparar diferentes períodos para ajustes nas estratégias de cobrança.

## Filial Employer

![Filial Employer](../images/PBI_Assemat_Emprestimos_2.png)


**Tipo:** Barra

Este gráfico de barras apresenta o desempenho de diferentes filiais em relação à gestão de empréstimos, destacando quais unidades têm melhor ou pior desempenho.

### Como interpretar:

- Comparar o desempenho de diferentes filiais em termos de gestão de empréstimos.
- Identificar filiais com alta inadimplência para ações corretivas.
- Avaliar a eficácia das estratégias de empréstimo por filial.

## Evolução

![Evolução](../images/PBI_Assemat_Emprestimos_3.png)


**Tipo:** Linha

O gráfico de linha "Evolução" ilustra as tendências ao longo do tempo para o total de dívida, permitindo uma análise temporal das flutuações financeiras.

### Como interpretar:

- Observar tendências de aumento ou diminuição no total de dívida ao longo do tempo.
- Identificar períodos de alta ou baixa significativa e investigar causas.
- Utilizar tendências para prever comportamentos futuros e ajustar estratégias.

# Filtros e Interações
O dashboard oferece filtros por período, filial e status do empréstimo. Esses filtros permitem que os usuários ajustem as visualizações para focar em períodos específicos, comparar o desempenho entre diferentes filiais ou analisar apenas empréstimos em um determinado status. As interações entre os gráficos são dinâmicas, permitindo que a seleção de um segmento em um gráfico atualize automaticamente os dados exibidos nos outros.

# Fluxo de Uso Recomendado
1. Inicie revisando o gráfico "Status" para uma visão geral da distribuição dos empréstimos.
2. Use os filtros para ajustar o período de análise e focar em áreas específicas.
3. Analise o gráfico "Dias Após Rescisão" para entender o impacto do tempo nos índices de inadimplência.
4. Compare o desempenho das diferentes filiais usando o gráfico "Filial Employer".
5. Examine o gráfico "Evolução" para identificar tendências temporais no total de dívida.
6. Ajuste estratégias com base nos insights obtidos.

# Perguntas de Negócio que o Dashboard Responde
- **Qual é o total de dívida atual?** → Verifique o KPI "Total de Dívida" no topo do dashboard.
- **Qual a proporção de dívidas em atraso?** → Consulte o gráfico "Status" para a distribuição de dívidas.
- **Como a dívida em atraso evoluiu nos últimos meses?** → Analise o gráfico "Evolução" para tendências temporais.
- **Quais filiais têm o maior índice de inadimplência?** → Veja o gráfico "Filial Employer" para comparações entre filiais.
- **Qual é o impacto dos dias após rescisão nos índices de inadimplência?** → Examine o gráfico "Dias Após Rescisão".
- **Como o ticket médio está variando ao longo do tempo?** → Utilize o gráfico "Evolução" para observar variações no ticket médio.
- **Quais períodos apresentaram maior aumento na dívida em cobrança?** → Use o gráfico "Evolução" para identificar picos.
- **Como posso ajustar estratégias para melhorar a cobrança?** → Combine insights dos gráficos e KPIs para formular estratégias.
```