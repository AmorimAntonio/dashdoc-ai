# Visão Geral do Dashboard

O dashboard "PBI Assemat Empréstimos" é uma ferramenta analítica projetada para fornecer uma visão abrangente sobre a situação dos empréstimos geridos pela equipe de finanças. Ele é essencial para monitorar o desempenho dos empréstimos, incluindo métricas críticas como o total de dívida, dívida em cobrança e dívida em atraso. Destinado principalmente à equipe de Gestão de Empréstimos e Finanças, o dashboard facilita a tomada de decisões informadas através de dados atualizados e visualizações intuitivas.

Este dashboard serve como um recurso central para analisar tendências de empréstimos, permitindo que os usuários identifiquem rapidamente áreas problemáticas e oportunidades de melhoria. Com ele, os gestores podem acompanhar a evolução das dívidas e ajustar estratégias para otimizar a recuperação de crédito e minimizar riscos financeiros.

# Objetivo de Negócio

- Monitorar o total de dívida e sua evolução ao longo do tempo.
- Identificar e gerenciar dívidas em cobrança e em atraso.
- Analisar o desempenho por filial e categoria de empréstimo.
- Avaliar o impacto do número de trabalhadores no ticket médio.
- Facilitar a tomada de decisões estratégicas baseadas em dados financeiros.

# Principais KPIs e Indicadores

- **Total de Dívida:** Representa o montante total de empréstimos pendentes.
- **Dívida em Cobrança:** Quantidade de dívida atualmente em processo de cobrança.
- **Dívida em Atraso:** Valor total de empréstimos que estão em atraso.
- **Número de Trabalhadores:** Total de trabalhadores associados aos empréstimos.
- **Ticket Médio:** Valor médio dos empréstimos concedidos.

# Descrição das Visualizações

## Status

![Status](../images/PBI_Assemat_Emprestimos_graph_0.png)


**Tipo:** Pizza

Este gráfico de pizza ilustra a distribuição percentual das diferentes categorias de status dos empréstimos, como ativos, em cobrança e em atraso.

### Como interpretar:

- Identifique rapidamente a proporção de empréstimos em cada status.
- Avalie a saúde geral da carteira de empréstimos.
- Compare a distribuição atual com períodos anteriores para identificar tendências.

## Dias Após Rescisão

![Dias Após Rescisão](../images/PBI_Assemat_Emprestimos_graph_1.png)


**Tipo:** Barra

O gráfico de barras mostra a quantidade de dias decorridos após a rescisão dos contratos de empréstimo, destacando os intervalos mais críticos.

### Como interpretar:

- Identifique os períodos mais comuns de atraso após a rescisão.
- Avalie a necessidade de ações de cobrança em diferentes intervalos de tempo.
- Compare com benchmarks internos para ajustar políticas de crédito.

## Filial Employer

![Filial Employer](../images/PBI_Assemat_Emprestimos_graph_2.png)


**Tipo:** Barra

Este gráfico de barras apresenta a distribuição de empréstimos por filial, permitindo uma análise detalhada do desempenho de cada unidade.

### Como interpretar:

- Compare o volume de empréstimos entre diferentes filiais.
- Identifique filiais com desempenho fora do padrão.
- Avalie o impacto das políticas locais na concessão de empréstimos.

## Evolução

![Evolução](../images/PBI_Assemat_Emprestimos_graph_3.png)


**Tipo:** Linha

O gráfico de linha mostra a evolução temporal do total de dívida, permitindo uma análise de tendências ao longo do tempo.

### Como interpretar:

- Observe tendências de aumento ou redução na dívida total.
- Identifique períodos de crescimento ou declínio acentuado.
- Correlacione eventos externos com mudanças na dívida.

# Filtros e Interações

O dashboard oferece filtros por data, filial e categoria de empréstimo. Esses filtros permitem que os usuários ajustem as visualizações para focar em períodos específicos, unidades de negócio ou tipos de empréstimo, afetando diretamente os dados exibidos nos gráficos.

# Fluxo de Uso Recomendado

1. Inicie revisando o gráfico de **Status** para uma visão geral da distribuição atual dos empréstimos.
2. Utilize os filtros para ajustar o período de análise e focar em filiais específicas.
3. Analise o gráfico de **Dias Após Rescisão** para identificar padrões de atraso.
4. Revise o gráfico **Filial Employer** para comparar o desempenho entre filiais.
5. Use o gráfico de **Evolução** para entender as tendências ao longo do tempo.
6. Ajuste estratégias com base nas análises realizadas.

# Perguntas de Negócio que o Dashboard Responde

- ❓ **Qual é o total de dívida atual?** → Verifique o KPI "Total de Dívida" no topo do dashboard.
- ❓ **Qual a proporção de dívidas em cobrança?** → Consulte o gráfico de pizza "Status".
- ❓ **Quais filiais têm o maior volume de empréstimos?** → Analise o gráfico de barras "Filial Employer".
- ❓ **Como a dívida total evoluiu nos últimos meses?** → Examine o gráfico de linha "Evolução".
- ❓ **Qual é o ticket médio dos empréstimos?** → Veja o KPI "Ticket Médio".
- ❓ **Quais são os períodos mais críticos após a rescisão?** → Consulte o gráfico de barras "Dias Após Rescisão".
- ❓ **Como as dívidas em atraso estão distribuídas por categoria?** → Use os filtros para ajustar a visualização de acordo com a categoria.
- ❓ **Qual é o impacto do número de trabalhadores na dívida total?** → Compare o KPI "Número de Trabalhadores" com o "Total de Dívida".
```