# Comparação entre as duas frentes

## Cobertura

A principal diferença entre as duas frentes está na forma de avaliação. A **Frente B (DeepEval)** foi executada sobre os **18 casos do Golden Dataset**, utilizando o comando `deepeval test run` e as métricas definidas para a avaliação.

A **Frente A (AgentCore Evaluations)** foi aplicada a uma **amostra de 5 interações reais**, selecionadas a partir da sessão exploratória.

Dessa forma, as duas frentes possuem escopos diferentes. A Frente B fornece resultados quantitativos para os casos do dataset, enquanto a Frente A permite observar com mais detalhes determinadas interações e seus respectivos traces.

---

## O que foi observado em cada frente

### Observações obtidas principalmente pela Frente B

- **Resultados quantitativos das métricas:** o caso 17 apresentou **0,00 em Conformidade**, enquanto outros casos apresentaram valores diferentes nas métricas de Relevância, Conformidade e Faithfulness.
- **Problemas de relevância:** a métrica Answer Relevancy apresentou valores abaixo do threshold em alguns casos, como 9, 13 e 14.
- **Diferenças entre métricas:** no caso 7, por exemplo, a Faithfulness foi **0,40**, enquanto a Conformidade foi **0,90**, mostrando que as métricas avaliaram aspectos diferentes da resposta.
- **Avaliação das cinco categorias:** os 18 casos permitiram obter resultados para consultas diretas, tarefas com ferramenta, interações multi-turno, casos fora do escopo e cenários adversariais.

### Observações obtidas principalmente pela Frente A

- **Possível persistência de informações entre sessões:** durante a análise dos traces, o produto **"Base Matte Ruby"**, observado na sessão `b32880b0...`, apareceu posteriormente no `user_context` de outra sessão (`facec552...`). A observação foi feita a partir da análise do contexto recuperado nos traces.
- **Possível causa técnica associada a uma falha:** no trace do caso `b32880b0...`, foram observadas tentativas de acesso ao catálogo utilizando um caminho de arquivo incorreto. Essa informação ajudou a contextualizar o comportamento observado naquela interação.
- **Comportamento do avaliador customizado:** no segundo turno da sessão `b32880b0...`, o `conformidade_beauty` retornou **Pass**, embora a resposta utilizasse produtos que haviam sido **inventados** no turno anterior daquela mesma interação. A análise do trace completo permitiu observar que a avaliação isolada do turno não identificou a origem inventada dessas informações.

---

## Características observadas nas duas frentes

| Aspecto | Frente A — AgentCore Evaluations | Frente B — DeepEval |
|---|---|---|
| **Foco** | Análise de interações e traces específicos | Avaliação dos casos do Golden Dataset |
| **Resultados** | Métricas dos casos selecionados e análise dos traces | Métricas quantitativas para os casos executados |
| **Análise de contexto** | Permite observar traces e contexto recuperado | Utiliza os dados definidos nos casos do dataset |
| **Relevância** | Não possui uma métrica equivalente à Answer Relevancy utilizada no DeepEval | Possui Answer Relevancy |
| **Automação** | Avaliação aplicada às interações selecionadas | Execução automatizada por `pytest` e `deepeval test run` |

---

## Limites observados

- **Frente A:** como foram utilizadas 5 interações selecionadas, os resultados representam os casos analisados e não permitem generalizar os valores para todo o comportamento do agente.
- **Frente B:** embora tenha sido executada sobre os 18 casos do Golden Dataset, seus resultados estão relacionados aos cenários definidos no dataset e às métricas utilizadas. A análise dos traces do AgentCore pode fornecer informações adicionais sobre determinados comportamentos observados.

---

## Conclusão da comparação

As duas frentes forneceram **perspectivas diferentes sobre os testes realizados**. A **Frente B** permitiu obter resultados quantitativos para os 18 casos do Golden Dataset, enquanto a **Frente A** permitiu analisar interações específicas com maior atenção aos traces e ao contexto recuperado.

Os resultados podem, portanto, ser utilizados de forma conjunta na etapa seguinte. Os casos que apresentaram resultados abaixo dos thresholds na Frente B podem ser considerados na análise de correção, enquanto as informações observadas nos traces da Frente A podem auxiliar na investigação dos comportamentos identificados.

