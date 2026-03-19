# Visão Geral do Dashboard

O dashboard “PBI Assemat Empréstimos” oferece uma visão abrangente sobre a situação dos empréstimos, permitindo o acompanhamento detalhado de indicadores-chave como total de dívida, valores em cobrança, inadimplência e performance por filial ao longo do tempo. Utilizando diferentes tipos de visualizações, o painel visa acelerar a tomada de decisões pela equipe de gestão financeira e operacional.

# Objetivo de Negócio

Capacitar a equipe de Gestão de Empréstimos e Finanças a acompanhar o panorama dos empréstimos, identificar riscos de inadimplência e ações de cobrança, analisar desempenho por unidade e otimizar estratégias de recuperação de crédito.

# Principais KPIs e Indicadores

- **Total de Dívida:** Valor total de empréstimos ativos e em aberto.
- **Dívida em Cobrança:** Montante dos empréstimos atualmente em processo de cobrança.
- **Dívida em Atraso:** Valor de empréstimos com parcelas vencidas.
- **Número de Trabalhadores:** Quantidade de mutuários ou clientes ativos.
- **Ticket Médio:** Valor médio dos empréstimos.

# Descrição das Visualizações

O dashboard apresenta os seguintes gráficos principais, cada um trazendo um recorte estratégico sobre a carteira de empréstimos:

---

## Status por inadimplência (pizza)

![Status por inadimplência](../images/PBI_Assemat_Emprestimos_graph_0.png)


### Descrição:
Gráfico do tipo pizza (ou setor) que representa proporcionalmente os diferentes status dos empréstimos em relação à inadimplência.

---

## Dias Após Rescisão por inadimplência (barras)

![Dias Após Rescisão por inadimplência](../images/PBI_Assemat_Emprestimos_graph_1.png)


### Descrição:
Gráfico de barras que exibe a quantidade de inadimplentes organizados pelos dias decorridos após o vencimento ou rescisão do contrato, trazendo uma visão temporal do atraso.

---

## Filial Employer por inadimplência (barras horizontais)

![Filial Employer por inadimplência](../images/PBI_Assemat_Emprestimos_graph_2.png)


### Descrição:
Gráfico de barras horizontais mostrando a inadimplência distribuída por cada filial, possibilitando identificar quais unidades apresentam maior concentração de débitos em atraso.

---

## Evolução por inadimplência (linha)

![Evolução por inadimplência](../images/PBI_Assemat_Emprestimos_graph_3.png)


### Descrição:
Gráfico de linha acompanhando a evolução dos valores em inadimplência ao longo do tempo, possibilitando visualização de tendências e sazonalidade.

# Como Interpretar Cada Gráfico

---

## Status por inadimplência (pizza)

![Status por inadimplência](../images/PBI_Assemat_Emprestimos_graph_0.png)


Permite rapidamente visualizar a proporção entre empréstimos em situação regular, em atraso e em cobrança. Uma fatia maior em “atraso” ou “cobrança” pode indicar deterioração da carteira de crédito, exigindo atenção imediata.

---

## Dias Após Rescisão por inadimplência (barras)

![Dias Após Rescisão por inadimplência](../images/PBI_Assemat_Emprestimos_graph_1.png)


Mostra a distribuição dos inadimplentes conforme o tempo decorrido desde o vencimento. Maiores volumes nas barras de períodos longos (ex: acima de 90 dias) indicam dificuldades na recuperação e risco de provisionamento.

---

## Filial Employer por inadimplência (barras horizontais)

![Filial Employer por inadimplência](../images/PBI_Assemat_Emprestimos_graph_2.png)


Demonstra quais filiais concentram os maiores valores ou volumes em inadimplência. Uma filial destacadamente acima das demais pode demandar ações específicas de gestão ou cobrança.

---

## Evolução por inadimplência (linha)

![Evolução por inadimplência](../images/PBI_Assemat_Emprestimos_graph_3.png)


A linha mostra o comportamento do nível de inadimplência ao longo dos meses. Picos ou tendências de alta são sinais de alerta, enquanto quedas apontam para avanços na recuperação de crédito.

# Filtros e Interações

O dashboard oferece filtros interativos (slicers) para segmentar a análise por períodos, filiais, status do empréstimo e outras dimensões relevantes. Os gráficos se conectam entre si: ao clicar em um segmento de um gráfico, os outros painéis se atualizam automaticamente para refletir essa seleção, permitindo análises detalhadas e cruzadas.

# Fluxo de Uso Recomendado

1. **Inicie pelo panorama geral dos KPIs** para entender o status atual da carteira de crédito.
2. **Utilize o gráfico de status por inadimplência** para identificar rapidamente o nível de saúde da carteira.

![Status por inadimplência](../images/PBI_Assemat_Emprestimos_graph_0.png)

3. **Explore os dias após rescisão** para identificar faixas críticas de atraso e definir prioridades de cobrança.
4. **Avalie as filiais com maior inadimplência** para eventualmente realocar recursos ou adaptar estratégias regionais.
5. **Monitore a evolução temporal** para avaliar o impacto de ações tomadas e identificar tendências.
6. **Aplique filtros conforme a necessidade** para análises mais específicas (por período, filial, perfil do trabalhador, etc).

# Perguntas de Negócio que o Dashboard Responde

- Qual é o valor total em dívida, cobrança e atraso?
- Qual o percentual da carteira atualmente inadimplente?
- Como a inadimplência se distribui entre as diferentes filiais?
- Há quanto tempo, em média, os empréstimos inadimplentes estão sem regularização?
- Qual foi a evolução da inadimplência nos últimos meses?
- Onde estão concentrados os principais riscos da carteira de crédito?
- Como as ações de cobrança impactaram os indicadores ao longo do tempo?