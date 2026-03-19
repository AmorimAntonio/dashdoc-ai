
# Visão Geral do Dashboard
O dashboard "PBI Assemat Empréstimos" é uma ferramenta analítica projetada para fornecer uma visão abrangente sobre a situação dos empréstimos geridos pela equipe de finanças. Ele oferece insights detalhados sobre o total de dívida, dívida em cobrança, dívida em atraso e outras métricas relevantes que são cruciais para a tomada de decisões estratégicas. Destinado principalmente à equipe de Gestão de Empréstimos e Finanças, o dashboard facilita o monitoramento contínuo e a análise detalhada das operações financeiras relacionadas aos empréstimos.

Através de visualizações interativas e intuitivas, os usuários podem explorar dados de diferentes perspectivas, permitindo uma compreensão mais profunda das dinâmicas de dívida e desempenho financeiro. O dashboard é uma ferramenta essencial para gestores que buscam otimizar a recuperação de crédito e melhorar a eficiência operacional.

# Objetivo de Negócio
- Monitorar o total de dívida por categoria para identificar áreas de risco.
- Avaliar a eficácia das estratégias de cobrança através da análise de dívida em cobrança.
- Identificar tendências de inadimplência através do acompanhamento da dívida em atraso.
- Auxiliar na alocação de recursos humanos através do monitoramento do número de trabalhadores.
- Analisar o ticket médio para ajustar políticas de empréstimo.

# Principais KPIs e Indicadores
- **Total de Dívida:** Valor acumulado de todos os empréstimos ativos.
- **Dívida em Cobrança:** Quantia total de empréstimos atualmente em processo de cobrança.
- **Dívida em Atraso:** Valor total de empréstimos que não foram pagos no prazo.
- **Número de Trabalhadores:** Quantidade de funcionários envolvidos na gestão de empréstimos.
- **Ticket Médio:** Valor médio dos empréstimos concedidos.

# Descrição das Visualizações

## Status

![Status](../images/PBI_Assemat_Emprestimos_0.png)


**Tipo:** donut

Este gráfico de donut oferece uma visão geral da distribuição dos empréstimos por status, permitindo identificar rapidamente a proporção de empréstimos em diferentes estágios, como ativos, em cobrança ou em atraso.

### Como interpretar:

- Proporção de empréstimos em atraso pode indicar áreas de preocupação.
- Alta porcentagem de empréstimos em cobrança pode sugerir necessidade de revisão de estratégias.
- Distribuição equilibrada pode indicar uma gestão eficaz dos empréstimos.

## Dias Após Rescisão

![Dias Após Rescisão](../images/PBI_Assemat_Emprestimos_1.png)


**Tipo:** barra

O gráfico de barras "Dias Após Rescisão" ilustra a distribuição dos empréstimos com base no número de dias após a rescisão, ajudando a identificar padrões de atraso e a eficácia das ações de cobrança.

### Como interpretar:

- Barras mais altas em intervalos de dias menores podem indicar eficiência na cobrança.
- Concentração em intervalos mais longos pode sinalizar necessidade de intervenção.
- Comparação entre períodos pode revelar tendências sazonais.

## Filial Employer

![Filial Employer](../images/PBI_Assemat_Emprestimos_2.png)


**Tipo:** barra

Este gráfico de barras apresenta a distribuição dos empréstimos por filial, permitindo uma análise comparativa do desempenho entre diferentes locais de operação.

### Como interpretar:

- Filiais com maior volume de empréstimos podem ser focos de análise para otimização.
- Discrepâncias significativas entre filiais podem indicar necessidade de padronização de processos.
- Análise de desempenho por filial pode auxiliar na alocação de recursos.

## Evolução

![Evolução](../images/PBI_Assemat_Emprestimos_3.png)


**Tipo:** linha

O gráfico de linha "Evolução" mostra a tendência temporal dos empréstimos, destacando mudanças no volume de dívida ao longo do tempo, o que é crucial para identificar padrões de crescimento ou declínio.

### Como interpretar:

- Tendências ascendentes podem indicar aumento na demanda por empréstimos.
- Quedas abruptas podem sinalizar mudanças nas políticas de concessão.
- Picos sazonais podem ser analisados para ajustes estratégicos.

# Filtros e Interações
O dashboard oferece filtros por período, filial e status do empréstimo, permitindo que os usuários personalizem as visualizações de acordo com suas necessidades específicas. A aplicação de filtros afeta diretamente os gráficos, atualizando as informações exibidas para refletir a seleção feita, facilitando análises mais direcionadas.

# Fluxo de Uso Recomendado
1. Iniciar a análise visualizando o gráfico "Status" para obter uma visão geral da distribuição dos empréstimos.
2. Utilizar o gráfico "Dias Após Rescisão" para identificar padrões de atraso e ajustar estratégias de cobrança.
3. Explorar o gráfico "Filial Employer" para comparar o desempenho entre diferentes filiais.
4. Analisar o gráfico "Evolução" para entender as tendências temporais dos empréstimos.
5. Aplicar filtros conforme necessário para refinar a análise e focar em áreas específicas de interesse.

# Perguntas de Negócio que o Dashboard Responde
- **Qual é o total de dívida atual?** → Visualizar no KPI "Total de Dívida".
- **Qual a proporção de empréstimos em atraso?** → Analisar o gráfico "Status".
- **Quais filiais têm o maior volume de empréstimos?** → Consultar o gráfico "Filial Employer".
- **Como está a evolução dos empréstimos ao longo do tempo?** → Examinar o gráfico "Evolução".
- **Quantos dias, em média, os empréstimos estão atrasados após a rescisão?** → Verificar o gráfico "Dias Após Rescisão".
- **Qual é o ticket médio dos empréstimos concedidos?** → Checar no KPI "Ticket Médio".
- **Como a dívida em cobrança está distribuída entre as filiais?** → Usar o gráfico "Filial Employer" com filtro de status.
- **Quais são as tendências sazonais de concessão de empréstimos?** → Analisar o gráfico "Evolução" ao longo do tempo.
