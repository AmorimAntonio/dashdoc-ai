# Visão Geral do Dashboard

O dashboard **PBI Assemat Empréstimos** fornece uma visão consolidada e interativa dos principais indicadores relacionados à gestão de empréstimos da organização. Reúne dados sobre a situação atual dos empréstimos, distribuição e evolução das dívidas, cobertura de cobrança e inadimplência, permitindo aos gestores uma análise detalhada por múltiplas dimensões e períodos.

# Objetivo de Negócio

O objetivo principal do dashboard é proporcionar informações relevantes e atualizadas para a equipe de Gestão de Empréstimos e Finanças, permitindo o monitoramento eficaz da carteira de empréstimos, identificação de tendências de inadimplência, apoio à tomada de decisão estratégica, priorização de ações de cobrança e suporte a análises segmentadas por categoria, filial e tempo após rescisão.

# Principais KPIs e Indicadores

- **Total de Dívida:** Valor total dos empréstimos ativos na carteira.
- **Dívida em Cobrança:** Montante referente aos empréstimos que estão em processo de cobrança.
- **Dívida em Atraso:** Quantia total de empréstimos em atraso conforme regras do negócio.
- **Número de Trabalhadores:** Total de trabalhadores devedores considerados nos dados.
- **Ticket Médio:** Valor médio da dívida por trabalhador.

# Descrição das Visualizações

O dashboard contém os seguintes gráficos principais:

- **Status por inadimplência (pizza):** Exibe a proporção dos empréstimos conforme o status de inadimplência.

![Status por inadimplência](../images/PBI_Assemat_Emprestimos_graph_0.png)

- **Dias Após Rescisão por inadimplência (barras):** Mostra a quantidade ou valor de empréstimos inadimplentes segmentados pelos dias decorridos após a rescisão do trabalhador.

![Dias Após Rescisão por inadimplência](../images/PBI_Assemat_Emprestimos_graph_1.png)

- **Filial Employer por inadimplência (barra horizontal):** Demonstra a inadimplência distribuída por filiais ou empregadores.

![Filial Employer por inadimplência](../images/PBI_Assemat_Emprestimos_graph_2.png)

- **Evolução por inadimplência (linha):** Apresenta a evolução temporal dos indicadores de inadimplência, evidenciando tendências ao longo do tempo.

![Evolução por inadimplência](../images/PBI_Assemat_Emprestimos_graph_3.png)


# Como Interpretar Cada Gráfico

- **Status por inadimplência (pizza):**

![Status por inadimplência](../images/PBI_Assemat_Emprestimos_graph_0.png)

  - Interprete as fatias como a representação percentual ou absoluta de cada status de inadimplência dos empréstimos (adimplente, em dia, em cobrança, em atraso, etc.), permitindo identificar rapidamente a distribuição das pendências financeiras.

- **Dias Após Rescisão por inadimplência (barra):**

![Dias Após Rescisão por inadimplência](../images/PBI_Assemat_Emprestimos_graph_1.png)

  - As barras representam quantidades ou valores agrupados por faixas de dias após a rescisão. Permite identificar em quais períodos pós-rescisão ocorre maior incidência de inadimplência, facilitando ações de cobrança mais assertivas.

- **Filial Employer por inadimplência (barra horizontal):**

![Filial Employer por inadimplência](../images/PBI_Assemat_Emprestimos_graph_2.png)

  - Cada barra mostra o montante ou número de empréstimos inadimplentes por filial/empregador. Auxilia na identificação de unidades com maiores índices de inadimplência, possibilitando ações direcionadas e comparativos entre regiões ou empresas.

- **Evolução por inadimplência (linha):**

![Evolução por inadimplência](../images/PBI_Assemat_Emprestimos_graph_3.png)

  - O gráfico de linhas apresenta a tendência da inadimplência ao longo do tempo, por períodos (meses, trimestres, etc.). Útil para análise de sazonalidade, impacto de medidas corretivas e monitoramento da efetividade de políticas de crédito.

# Filtros e Interações

O dashboard disponibiliza filtros para refinar a análise com base em variables como:
- Período (datas)
- Categoria de empréstimo
- Filial/Empregador
- Faixas de valor
- Outros atributos relevantes (ex: status de cobrança, tipo de contrato)
A interação entre os gráficos é dinâmica: selecionar um segmento em uma visualização reflete instantaneamente nas demais, possibilitando análises multifacetadas e exploração de possíveis correlações.

# Fluxo de Uso Recomendado

1. **Selecione o período de análise** para restringir o escopo conforme necessidade.
2. **Analise o panorama geral pela pizza de status**, identificando proporções de inadimplência.
3. **Investigue picos de inadimplência nas barras por dias após rescisão** para compreender comportamentos temporais.
4. **Aprofunde a análise nas unidades com maiores índices via barra por filial** e verifique onde estão concentrados os maiores riscos.
5. **Acompanhe a evolução da inadimplência pelo gráfico de linha** para avaliar tendências e impactos de ações ao longo do tempo.
6. **Aplique filtros adicionais** para realizar cortes por categoria, valor ou outros interesses específicos.

# Perguntas de Negócio que o Dashboard Responde

- Qual o valor total da dívida, e como ela se distribui entre os diferentes status de cobrança?
- Quantos trabalhadores estão inadimplentes e qual o ticket médio por trabalhador?
- Como a inadimplência evolui ao longo do tempo e existe sazonalidade nesses valores?
- Após quanto tempo da rescisão a inadimplência tende a se concentrar?
- Quais filiais apresentam maiores índices ou valores absolutos de inadimplência?
- As ações de cobrança atuais têm impacto e onde é necessário intensificá-las?
- Quais segmentos ou categorias demandam maior atenção em termos de risco de inadimplência?