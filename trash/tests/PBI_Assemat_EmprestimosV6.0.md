# Visão Geral do Dashboard

O dashboard **PBI Assemat Empréstimos** foi desenvolvido para fornecer à equipe de gestão de empréstimos e finanças uma visão ampla e detalhada sobre o cenário de empréstimos na organização. O relatório reúne métricas essenciais para acompanhamento e tomadas de decisão, incluindo informações sobre totais de dívidas, dívidas em cobrança, dívidas em atraso, ticket médio, número de trabalhadores, entre outros indicadores relevantes.

# Objetivo de Negócio

O principal objetivo deste dashboard é possibilitar o monitoramento e análise detalhada dos empréstimos concedidos pela organização, facilitando a detecção de inadimplência, a avaliação do desempenho por filial e o acompanhamento das mudanças ao longo do tempo. O dashboard oferece suporte para ações corretivas, análises de risco e decisões estratégicas relacionadas à concessão e recuperação de empréstimos.

# Principais KPIs e Indicadores

- **Total de Dívida**: Valor total devido pelos tomadores de empréstimo, considerando todos os empréstimos ativos na base.
- **Dívida em Cobrança**: Valor das dívidas que estão atualmente em fase de cobrança.
- **Dívida em Atraso**: Valor das dívidas cujo pagamento está em atraso, conforme os critérios internos.
- **Número de Trabalhadores**: Quantidade total de trabalhadores que possuem empréstimos registrados.
- **Ticket Médio**: Valor médio dos empréstimos concedidos.
  
# Descrição das Visualizações

## Status por inadimplência

![Status por inadimplência](../images/PBI_Assemat_Emprestimos_graph_0.png)


Este gráfico apresenta a distribuição dos empréstimos de acordo com o status da inadimplência, como "adimplente", "em cobrança", "em atraso" e outros possíveis status definidos pela organização.

**Como interpretar o gráfico:**  
Permite identificar rapidamente a quantidade e o valor dos empréstimos em cada status de inadimplência, facilitando o acompanhamento da saúde da carteira de empréstimos e a identificação de pontos críticos que exigem atenção imediata.

---

## Dias Após Rescisão por inadimplência

![Dias Após Rescisão por inadimplência](../images/PBI_Assemat_Emprestimos_graph_1.png)


Este gráfico analisa a relação entre os dias transcorridos desde a rescisão do contrato e a inadimplência associada aos empréstimos.

**Como interpretar o gráfico:**  
É útil para entender o comportamento dos devedores após o fim do vínculo contratual, possibilitando identificar tendências de inadimplência em diferentes períodos após a rescisão e subsidiando políticas de cobrança mais eficazes.

---

## Filial Employer por inadimplência

![Filial Employer por inadimplência](../images/PBI_Assemat_Emprestimos_graph_2.png)


Neste gráfico, a inadimplência é segmentada por filial (unidade Employer).

**Como interpretar o gráfico:**  
Permite comparar o desempenho de diferentes filiais no que diz respeito à inadimplência, identificando filiais com maiores índices de atraso ou em cobrança, direcionando ações corretivas e suportando decisões de gestão regionalizadas.

---

## Evolução por inadimplência

![Evolução por inadimplência](../images/PBI_Assemat_Emprestimos_graph_3.png)


O gráfico apresenta a evolução temporal dos valores de inadimplência, mostrando como os saldos em atraso ou em cobrança variaram ao longo do tempo.

**Como interpretar o gráfico:**  
Acompanha tendências históricas, possibilitando avaliar a efetividade de ações tomadas anteriormente e antecipar possíveis problemas futuros a partir da identificação de padrões de evolução.

# Filtros e Interações

O dashboard oferece filtros para seleção de períodos, status de inadimplência, filial, e demais atributos relevantes presentes nas tabelas de dados. As interações entre os gráficos permitem ao usuário clicar em um elemento de um gráfico (por exemplo, uma filial) e visualizar o detalhamento desse filtro nas demais visualizações, proporcionando uma análise dinâmica e multifacetada.

# Fluxo de Uso Recomendado

1. **Seleção inicial de período e filial**: Ajuste os filtros para o período e a(s) filial(is) de interesse.
2. **Análise geral do status da carteira**: Utilize o gráfico de Status por inadimplência para obter uma visão global.
3. **Investigação de tendências**: Consulte o gráfico de Evolução por inadimplência para compreender a dinâmica temporal.
4. **Análise detalhada por segmentação**: Explore os gráficos de dias após rescisão e filial para identificar focos de inadimplência específicos.
5. **Deep dive com interações**: Explore detalhes utilizando interações e cruzamentos entre gráficos, ajustando filtros conforme necessidades.

# Perguntas de Negócio que o Dashboard Responde

- Qual é o valor total de empréstimos em atraso e em cobrança atualmente?
- Quais são as filiais com maiores índices de inadimplência?
- Como a inadimplência evoluiu ao longo do tempo?
- Qual o comportamento da inadimplência após a rescisão dos contratos?
- Quantos trabalhadores estão inadimplentes em relação ao total de empréstimos?
- Qual é o ticket médio dos empréstimos?
- Existem períodos críticos ou picos de inadimplência que exigem atenção?
- As ações de cobrança e prevenção têm surtido efeito na redução da inadimplência?