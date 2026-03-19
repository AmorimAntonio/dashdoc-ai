# Visão Geral do Dashboard

O dashboard "PBI Assemat Empréstimos" é uma ferramenta essencial para a equipe de Gestão de Empréstimos e Finanças, fornecendo uma visão abrangente sobre o estado dos empréstimos dentro da organização. Ele é projetado para ajudar os usuários a monitorar e analisar métricas críticas, como o total de dívida, dívida em cobrança e dívida em atraso. Com uma interface intuitiva, o dashboard facilita a identificação de tendências e a tomada de decisões informadas.

Este dashboard é particularmente útil para gestores que precisam de uma visão consolidada e detalhada das operações de empréstimos. Ele permite que os usuários explorem dados por diferentes categorias e períodos, garantindo que as estratégias financeiras sejam baseadas em informações precisas e atualizadas.

# Objetivo de Negócio

- Monitorar o total de dívida e identificar tendências ao longo do tempo.
- Avaliar a eficiência das cobranças e o impacto das dívidas em atraso.
- Analisar o desempenho das filiais em relação aos empréstimos.
- Identificar áreas de risco e oportunidades de melhoria nos processos de empréstimo.
- Auxiliar na alocação de recursos e planejamento financeiro estratégico.

# Principais KPIs e Indicadores

- **Total de Dívida**: Representa o montante total de empréstimos pendentes.
- **Dívida em Cobrança**: Indica o valor dos empréstimos que estão atualmente em processo de cobrança.
- **Dívida em Atraso**: Reflete o montante de empréstimos que não foram pagos dentro do prazo acordado.
- **Número de Trabalhadores**: Mostra a quantidade de trabalhadores envolvidos nos empréstimos.
- **Ticket Médio**: Calcula o valor médio dos empréstimos concedidos.

# Descrição das Visualizações

## Status

![Status](../images/PBI_Assemat_Emprestimos_0.png)


**Tipo:** donut

Este gráfico de donut ilustra a distribuição dos empréstimos por status, como em dia, em cobrança e em atraso. Ele fornece uma visão rápida da proporção de cada categoria em relação ao total de empréstimos.

### Como interpretar:

- Identificar a maior categoria de status de empréstimos.
- Avaliar a proporção de empréstimos em atraso em relação ao total.
- Comparar a distribuição atual com períodos anteriores para identificar mudanças.

## Dias Após Rescisão

![Dias Após Rescisão](../images/PBI_Assemat_Emprestimos_1.png)


**Tipo:** barra

O gráfico de barras "Dias Após Rescisão" mostra a quantidade de dias decorridos após a rescisão dos contratos de empréstimo. Ele ajuda a entender o tempo médio que leva para resolver empréstimos após a rescisão.

### Como interpretar:

- Verificar a média de dias após rescisão para identificar atrasos.
- Comparar diferentes períodos para avaliar melhorias ou pioras.
- Analisar se há picos em determinados períodos que necessitam de atenção.

## Filial Employer

![Filial Employer](../images/PBI_Assemat_Emprestimos_2.png)


**Tipo:** barra

Este gráfico de barras apresenta a distribuição dos empréstimos por filial, permitindo uma análise do desempenho de cada unidade em termos de volume de empréstimos.

### Como interpretar:

- Identificar quais filiais têm o maior volume de empréstimos.
- Comparar o desempenho entre diferentes filiais.
- Avaliar se o volume de empréstimos está alinhado com as metas estabelecidas para cada filial.

## Evolução

![Evolução](../images/PBI_Assemat_Emprestimos_3.png)


**Tipo:** linha

O gráfico de linha "Evolução" demonstra a tendência dos empréstimos ao longo do tempo, destacando variações no total de dívida, cobranças e atrasos.

### Como interpretar:

- Observar tendências de aumento ou diminuição no total de dívida.
- Identificar períodos com maior volume de cobranças ou atrasos.
- Avaliar a eficácia de estratégias implementadas em períodos específicos.

# Filtros e Interações

O dashboard oferece filtros por período, filial e status do empréstimo. Esses filtros permitem que os usuários ajustem as visualizações para focar em dados relevantes para suas análises específicas. Ao aplicar um filtro, todas as visualizações são atualizadas para refletir apenas os dados que atendem aos critérios selecionados, facilitando comparações e insights detalhados.

# Fluxo de Uso Recomendado

1. Inicie revisando o gráfico "Status" para obter uma visão geral da distribuição dos empréstimos.
2. Use o gráfico "Dias Após Rescisão" para identificar possíveis atrasos nos processos.
3. Analise o gráfico "Filial Employer" para comparar o desempenho entre as diferentes filiais.
4. Examine o gráfico "Evolução" para observar tendências ao longo do tempo.
5. Utilize os filtros para ajustar as visualizações conforme necessário e aprofundar a análise.

# Perguntas de Negócio que o Dashboard Responde

- **Qual é o total de dívida atual?** → Verifique o KPI "Total de Dívida" na seção de KPIs.
- **Qual a proporção de empréstimos em atraso?** → Consulte o gráfico "Status".
- **Quais filiais têm o maior volume de empréstimos?** → Analise o gráfico "Filial Employer".
- **Como está a evolução dos empréstimos ao longo do tempo?** → Veja o gráfico "Evolução".
- **Qual é o tempo médio após a rescisão dos contratos?** → Observe o gráfico "Dias Após Rescisão".
- **Qual é o ticket médio dos empréstimos?** → Verifique o KPI "Ticket Médio".
- **Como os empréstimos em cobrança estão distribuídos atualmente?** → Consulte o gráfico "Status" e aplique filtros conforme necessário.
- **Há períodos específicos com aumento de dívidas em atraso?** → Analise o gráfico "Evolução" para identificar picos.
```