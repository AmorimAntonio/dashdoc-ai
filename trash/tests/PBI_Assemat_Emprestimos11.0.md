```markdown
# Visão Geral do Dashboard

O dashboard "PBI Assemat Empréstimos" é uma ferramenta desenvolvida para fornecer uma visão abrangente sobre a situação dos empréstimos geridos pela equipe de gestão de empréstimos e finanças. Ele oferece insights detalhados sobre o total de dívida, dívida em cobrança, dívida em atraso, entre outras métricas cruciais para a tomada de decisões estratégicas. Este dashboard é essencial para os gestores que buscam monitorar e otimizar a performance financeira da organização.

Através de visualizações interativas, os usuários podem analisar dados de empréstimos por diversas dimensões, como categoria e localização, permitindo um entendimento mais profundo das tendências e padrões. O público-alvo deste dashboard inclui principalmente a equipe de gestão de empréstimos e finanças, que pode utilizá-lo para melhorar a eficiência operacional e a gestão de riscos.

# Objetivo de Negócio

- Monitorar o total de dívida e identificar tendências ao longo do tempo.
- Avaliar a eficácia das estratégias de cobrança de dívidas.
- Identificar e mitigar riscos associados a dívidas em atraso.
- Analisar a distribuição de empréstimos por filial e categoria.
- Otimizar o gerenciamento de recursos humanos e financeiros.

# Principais KPIs e Indicadores

- **Total de Dívida:** Representa o montante total de empréstimos pendentes.
- **Dívida em Cobrança:** Indica o valor total de dívidas que estão em processo de cobrança.
- **Dívida em Atraso:** Mostra o montante de dívidas que não foram pagas no prazo.
- **Número de Trabalhadores:** Refere-se ao total de trabalhadores envolvidos na gestão dos empréstimos.
- **Ticket Médio:** Calcula o valor médio dos empréstimos concedidos.

# Descrição das Visualizações

## Status

![Status](../images/PBI_Assemat_Emprestimos_graph_0.png)


**Tipo:** donut

Este gráfico de donut ilustra a distribuição percentual dos empréstimos por status, como ativos, em cobrança ou em atraso. Ele ajuda a visualizar rapidamente a proporção de cada status em relação ao total de empréstimos.

### Como interpretar:

- Identificar qual status possui a maior proporção de empréstimos.
- Avaliar a eficácia das estratégias de cobrança ao observar a proporção de dívidas em cobrança.
- Analisar a saúde financeira geral através da proporção de dívidas em atraso.

## Dias Após Rescisão

![Dias Após Rescisão](../images/PBI_Assemat_Emprestimos_graph_1.png)


**Tipo:** barra

O gráfico de barras mostra a quantidade de dias após a rescisão dos contratos de empréstimo, permitindo identificar padrões de atraso e o tempo médio de resolução.

### Como interpretar:

- Observar picos de atraso que possam indicar problemas sistêmicos.
- Comparar a média de dias após rescisão entre diferentes períodos.
- Identificar melhorias ou deteriorações na gestão de cobranças ao longo do tempo.

## Filial Employer

![Filial Employer](../images/PBI_Assemat_Emprestimos_graph_2.png)


**Tipo:** barra

Este gráfico de barras apresenta a distribuição dos empréstimos por filial, permitindo uma análise detalhada de quais locais estão gerando mais empréstimos e quais podem precisar de atenção.

### Como interpretar:

- Identificar filiais com maior volume de empréstimos.
- Avaliar a performance de cada filial em termos de gestão de empréstimos.
- Detectar filiais que possam estar enfrentando dificuldades financeiras.

## Evolução

![Evolução](../images/PBI_Assemat_Emprestimos_graph_3.png)


**Tipo:** linha

O gráfico de linha mostra a evolução temporal do total de dívida, permitindo uma análise de tendências e sazonalidades ao longo do tempo.

### Como interpretar:

- Identificar tendências de aumento ou diminuição do total de dívida.
- Avaliar o impacto de intervenções estratégicas em períodos específicos.
- Analisar sazonalidades que possam afetar a dívida total.

# Filtros e Interações

O dashboard oferece filtros por período, categoria de empréstimo, e filial, permitindo que os usuários ajustem as visualizações para focar em áreas específicas de interesse. Esses filtros afetam todas as visualizações simultaneamente, proporcionando uma análise coerente e integrada dos dados.

# Fluxo de Uso Recomendado

1. Iniciar pela visualização "Status" para obter uma visão geral da distribuição dos empréstimos.
2. Utilizar o gráfico "Dias Após Rescisão" para identificar padrões de atraso.
3. Analisar a distribuição por filial no gráfico "Filial Employer" para insights localizados.
4. Examinar a "Evolução" do total de dívida para entender tendências temporais.
5. Aplicar filtros conforme necessário para aprofundar a análise em áreas específicas.

# Perguntas de Negócio que o Dashboard Responde

- **Qual é o status atual dos empréstimos?** → Ver gráfico "Status".
- **Quantos dias, em média, os empréstimos estão em atraso após a rescisão?** → Consultar gráfico "Dias Após Rescisão".
- **Qual filial possui o maior volume de empréstimos?** → Analisar gráfico "Filial Employer".
- **Como o total de dívida evoluiu ao longo do tempo?** → Examinar gráfico "Evolução".
- **Qual é a proporção de dívida em cobrança em relação ao total?** → Ver gráfico "Status".
- **Quais são as tendências de dívida em atraso?** → Analisar gráfico "Evolução".
- **Como os empréstimos estão distribuídos por categoria?** → Aplicar filtros e observar mudanças nos gráficos.
- **Qual é o ticket médio dos empréstimos?** → Consultar a seção de KPIs.
```