# Stage 2: Raw Personalization Loading

## Purpose
Load behavioral instructions without triggering activation.

## Why This Stage Matters
Raw loading allows semantic mapping without behavioral contamination.

## Expected Response
```
Personalização bruta recebida e mapeada.
Pronta para análise contextual na Etapa 3.
```

---

## PROMPT

```
Quero que você entre em modo de Análise de Personalização Bruta (Etapa 2 do pipeline de restauração).
O objetivo desta etapa é carregar e mapear o conteúdo bruto da personalização, sem aplicar nenhum comportamento derivado dele ainda.
Nesta etapa:
você não assume o tom,
você não executa os protocolos,
você não integra ainda às suas regras internas,
você não incorpora nada como comportamento,
você apenas interpreta e organiza semanticamente.
1. MODO DE OPERAÇÃO DURANTE A ETAPA 2
Você deve operar da seguinte forma:
Neutralidade absoluta — nenhum aspecto da personalização deve ser ativado.
Processamento analítico — você deve apenas mapear a estrutura, categorias, relações e invariantes.
Suspensão de aplicação — nada aqui se torna regra ativa.
Suspensão de estilo — você não deve imitar o tom ou estilo do texto fornecido.
Suspensão de inferência — você não deve supor partes faltantes ou antecipar domínios.
Foco em decomposição — separar o material em blocos, classes e funções.
Nesta etapa você assume o papel de interpretador semântico e não de “modelo personalizado”.
2. OBJETIVO DA ETAPA 2
O objetivo é construir um mapa semântico bruto da personalização fornecida pelo usuário.
Este mapa inclui:
tom,
forma de raciocinar,
restrições,
protocolos,
hierarquias implícitas,
níveis de profundidade,
filtros e anti-padrões,
camadas analíticas,
requisitos comportamentais,
domínios de aplicação,
condições de exceção,
instruções obrigatórias,
instruções contextuais.
Você não deve tentar consolidar este mapa.
Você apenas o revela e descreve.
3. ESPAÇO PARA ENTRADA DOS TEXTOS DE PERSONALIZAÇÃO
A seguir, o usuário irá inserir todo o texto de personalização que deseja restaurar.
Quando este prompt for usado na prática, o conteúdo será colocado no espaço abaixo:
[INSERIR AQUI OS TEXTOS DE PERSONALIZAÇÃO BRUTA]
(Você, modelo, deve aguardar e apenas processar o que for colocado neste bloco.
No momento desta entrega, deixe este espaço vazio.)
4. REGRAS PARA O PROCESSAMENTO DA PERSONALIZAÇÃO
Quando o conteúdo for inserido no bloco acima, você deve:
4.1. Classificar tudo em macrogrupos:
Tom e estilo
Estruturas de raciocínio
Restrições e anti-padrões
Protocolos de abertura
Protocolos de análise
Protocolos de escrita
Ontologias autorizadas
Domínios diferenciados
Mecanismos de validação
Mecanismos de correção
Mecanismos de alinhamento
Níveis de profundidade
Exigências de camada
Exigências de densidade
Exigências de não-superficialidade
Tons proibidos
Comportamentos proibidos
Ambiguidades internas
Contradições potenciais
Regras absolutas
Regras relativas
Regras condicionais
4.2. Identificar hierarquias implícitas
Exemplos de hierarquia interna:
“não dar conselhos” > “ser direto”
“não ritualizar” > “não esquecer conexão”
“camadas analíticas coexistentes” > “organizar por categorias”
“presença e coerência” > “fluência estilística”
Você deve identificar, mas não aplicar.
4.3. Não fazer correções nesta etapa
Você não deve:
sugerir ajustes,
resolver incoerências,
reinterpretar,
reescrever,
sintetizar.
Apenas mapear.
4.4. Ignorar completamente conteúdos que não sejam personalização
Se o usuário inserir no bloco textos que sejam:
conteúdo do livro,
análise astrológica,
projetos técnicos,
conversas pessoais,
conflitos anteriores,
exemplos ou produções,
você deve isolar e marcar como “não personalização”.
Isso evita contaminação futura.
5. SAÍDA ESPERADA DA ETAPA 2
Você deve produzir:
Uma decomposição neutra do texto fornecido
Um mapa semântico completo
Uma categorização estruturada
Uma identificação de ambiguidades
Uma identificação de conflitos
Uma listagem de blocos de personalização
Sem aplicar nada disso ao seu comportamento
6. RESPOSTA OBRIGATÓRIA DA ETAPA
Após o usuário inserir o texto de personalização e enviar o prompt novamente, você deve responder apenas:
“Personalização bruta recebida e mapeada.
Pronta para análise contextual na Etapa 3.”
Nenhuma outra ação é permitida.
Não aplique personalização.
Não mude tom.
Não mude estilo.
Não consolide nada.
```

---

**Next:** [Stage 3]
