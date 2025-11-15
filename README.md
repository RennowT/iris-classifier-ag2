# iris-classifier-ag2

Projeto da disciplina AG2 (Engenharia de Computação e Software – INATEL) para treinar, avaliar e disponibilizar um modelo de classificação para o conjunto de dados Iris.  
O projeto realiza pré-processamento, treinamento de modelo, avaliação e permite prever a espécie de uma flor a partir de dados inseridos pelo usuário.

---

## Algoritmo de Classificação Escolhido

O algoritmo selecionado para este projeto é a **Árvore de Decisão (Decision Tree)**.

### Justificativa Técnica

- O conjunto de dados Iris possui três classes e quatro variáveis numéricas, caracterizando um problema multiclasses de baixa dimensionalidade — um cenário no qual Decision Trees apresentam ótimo desempenho.  
- Árvores de decisão lidam bem com relações não-lineares entre variáveis, comuns no dataset Iris.  
- Não exigem escalonamento ou normalização, reduzindo o pré-processamento necessário.  
- Estudos comparativos mostram que Decision Trees oferecem bom equilíbrio entre desempenho, robustez e simplicidade para conjuntos tabulares como o Iris.

Durante o treinamento e na separação entre treino e teste, o parâmetro `random_state` foi fixado em **42** para garantir reprodutibilidade dos resultados. Uma escolha que também faz alusão ao clássico “O Guia do Mochileiro das Galáxias”, no qual o número 42 é apresentado como:

> “a resposta para a vida, o universo e tudo mais.”

---

## Execução do Projeto

### 1. Instalar dependências
Certifique-se de estar no diretório do projeto e execute:

```bash
pip install -r requirements.txt
```

### 2. Executar o programa principal

```bash
python main.py
```

Ao iniciar, o programa:

1. Carrega o dataset
2. Converte as classes para valores inteiros
3. Separa os dados em treino e teste
4. Treina o modelo Decision Tree
5. Avalia o modelo
6. Pergunta ao usuário dados arbitrários para classificação
7. Exibe a espécie prevista

---

## Uso — Inserir novos dados para classificação

Após rodar o programa, o terminal solicitará:

```
Comprimento da sépala (cm):
Largura da sépala (cm):
Comprimento da pétala (cm):
Largura da pétala (cm):
```

Exemplo de entrada:

```
5.1
3.5
1.4
0.2
```

Saída esperada:

```
>>> A espécie prevista é: setosa.
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
