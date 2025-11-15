# iris-classifier-ag2

Projeto da disciplina AG2 (Engenharia de Computação e Software – INATEL) para treinar, avaliar e disponibilizar um modelo de classificação para o conjunto de dados Iris.  
O projeto realiza pré-processamento, treinamento de modelo, avaliação e permite prever a espécie de uma flor a partir de dados inseridos pelo usuário.

## Algoritmo de Classificação Escolhido

Para este projeto foi selecionado o algoritmo **Árvore de Decisão (Decision Tree)** como modelo principal de classificação.

A escolha foi baseada em critérios técnicos:

- O conjunto de dados Iris possui três classes e quatro variáveis numéricas, formando um problema multiclasses de baixa dimensionalidade. Um cenário no qual árvores de decisão apresentam desempenho sólido e estável.  
- Árvores de decisão conseguem lidar naturalmente com relações não-lineares entre variáveis, algo relevante no conjunto Iris, que apresenta fronteiras de decisão parcialmente não lineares entre as espécies.  
- Não é necessário escalonamento ou normalização das variáveis, reduzindo a complexidade do pré-processamento.  
- Em estudos comparativos, árvores de decisão frequentemente apresentam bom equilíbrio entre desempenho, interpretabilidade e simplicidade para conjuntos estruturados como o Iris.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
