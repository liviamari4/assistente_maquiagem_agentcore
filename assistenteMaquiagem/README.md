# Assistente de Maquiagem — Amazon Bedrock AgentCore

Assistente de IA especializado em maquiagem e cosméticos, desenvolvido com **Amazon Bedrock AgentCore**.

O projeto foi desenvolvido no contexto do **Desafio 2 — Avaliação e Red Teaming**, com foco na construção, avaliação e análise de segurança de um agente de IA.

## Objetivo

O assistente responde a consultas relacionadas aos produtos disponíveis em um catálogo de maquiagem, utilizando uma fonte autorizada para obter informações sobre:

* produtos;
* preços;
* características;
* tipo de pele;
* acabamento;
* orçamento;
* cálculos relacionados aos produtos.

O agente deve evitar a invenção de produtos, preços ou características e permanecer dentro do escopo definido para maquiagem e cosméticos.

---

## Arquitetura

O projeto utiliza os seguintes componentes:

* **Amazon Bedrock AgentCore**
* **Amazon Nova Lite** como modelo do agente
* **Managed Memory**
* **Code Interpreter** para cálculos
* **Skill `catalogo-maquiagem`**
* **Amazon S3** como fonte do catálogo
* **Amazon Nova Pro** como modelo avaliador do `conformidade_beauty`
* **AWS CDK** para infraestrutura

### Fluxo simplificado

```text
Usuário
   │
   ▼
Assistente de Maquiagem
   │
   ├── System Prompt
   │
   ├── Managed Memory
   │
   ├── Skill: catalogo-maquiagem
   │        │
   │        └── Catálogo autorizado
   │
   └── Code Interpreter
            │
            └── Cálculos
```

---

## Catálogo

O assistente utiliza um catálogo com **20 produtos**.

A skill `catalogo-maquiagem` define as regras para consulta da fonte autorizada e está localizada em:

```text
app/assistenteMaquiagem/catalogo-maquiagem/
├── SKILL.md
├── catalogo.json
└── references/
    └── catalogo.md
```

---

## Avaliação

O projeto foi avaliado utilizando três frentes complementares:

### 1. AgentCore Evaluations

Avaliação realizada no ambiente do AgentCore utilizando:

* Correctness;
* Faithfulness;
* avaliador customizado `conformidade_beauty`.

O avaliador customizado utiliza **Amazon Nova Pro** como LLM-as-a-Judge.

Evidência:

```text
avaliacoes/01-frente_a_agentcore.md
```

### 2. DeepEval

Foi utilizado um conjunto de **18 casos** para avaliar o comportamento do agente por meio de métricas como:

* Answer Relevancy;
* Faithfulness;
* Conformidade.

Evidências:

```text
dataset.json
test_deepeval.py
avaliacoes/02-frente_b_deepeval.md
```

### 3. Red Teaming

Foram realizados **15 testes adversariais** envolvendo situações como:

* prompt injection;
* tentativa de vazamento de informações internas;
* manipulação de valores;
* uso indevido de contexto;
* solicitações fora do escopo;
* recomendações sem fonte autorizada;
* uso inadequado de ferramentas.

Evidências:

```text
red_teaming.md
analise_correcao.md
relatoria.md
```

---

## Principais resultados

### AgentCore Evaluations

Foram avaliadas cinco interações comparando o comportamento baseline com a versão final.

Os resultados indicaram melhora em alguns cenários, manutenção em outros e uma regressão no caso relacionado à solicitação de garantia.

### DeepEval

No conjunto de 18 casos:

```text
Baseline:     7/18 atingiram os thresholds
Versão final: 8/18 atingiram os thresholds
```

Também foi identificada uma regressão em um cenário multi-turno, demonstrando que as correções não produziram melhora uniforme em todos os casos.

### Red Teaming

Os testes identificaram vulnerabilidades relacionadas a:

* vazamento de informações internas;
* manipulação de valores;
* uso de contexto;
* estimativa de preços inexistentes;
* solicitações fora do escopo;
* generalização de alertas;
* recomendações sem fonte autorizada.

Algumas vulnerabilidades foram corrigidas nos cenários retestados, enquanto outras permaneceram parcialmente corrigidas ou inconclusivas.

---

## Riscos residuais

A avaliação identificou riscos que ainda precisam de tratamento antes de uma eventual utilização em produção.

Entre eles:

* recomendação sem fonte autorizada quando o catálogo está indisponível;
* comportamento inconclusivo relacionado ao uso de contexto entre sessões;
* regressão identificada em cenário multi-turno;
* necessidade de ampliar os retestes para avaliar estabilidade do comportamento.

Os detalhes estão documentados em:

```text
red_teaming.md
analise_correcao.md
avaliacoes/01-frente_a_agentcore.md
avaliacoes/02-frente_b_deepeval.md
```

---

## Estrutura do projeto

```text
assistente-maquiagem-agentcore/
│
├── README.md
├── AGENTS.md
├── .gitignore
│
├── app/
│   └── assistenteMaquiagem/
│       ├── harness.json
│       ├── system-prompt.md
│       │
│       └── catalogo-maquiagem/
│           ├── SKILL.md
│           ├── catalogo.json
│           └── references/
│               └── catalogo.md
│
├── agentcore/
│   ├── agentcore.json
│   └── cdk/
│
├── avaliacoes/
│   ├── 01-frente_a_agentcore.md
│   ├── 02-frente_b_deepeval.md
│   └── comparacao.md
│
├── backup/
│   ├── harness.nova-lite.json
│   └── system-prompt.baseline.md
│
├── dataset.json
├── test_deepeval.py
├── invoke_agent.py
├── red_teaming.md
├── analise_correcao.md
├── relatoria.md
├── sessao_exploratoria.md
└── instrucoes_conformidade.txt
```

---

## Requisitos

Para trabalhar com o projeto, são necessários os recursos utilizados no desenvolvimento, incluindo:

* Python;
* Node.js;
* AWS CLI;
* AgentCore CLI;
* credenciais AWS com as permissões necessárias;
* acesso aos recursos AWS utilizados pelo projeto.

---

## Observações

O projeto foi desenvolvido para fins de avaliação e estudo no contexto do desafio.

Os resultados apresentados representam os cenários efetivamente testados. Retestes individuais não permitem concluir sobre a estabilidade do comportamento em múltiplas execuções.

Consulte os arquivos de avaliação e Red Teaming para os resultados detalhados.

---

## Evidências

As principais evidências do projeto estão organizadas em:

```text
avaliacoes/
red_teaming.md
analise_correcao.md
relatoria.md
dataset.json
test_deepeval.py
sessao_exploratoria.md
```
