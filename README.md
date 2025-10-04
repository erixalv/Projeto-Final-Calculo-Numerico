# Cálculo de Área com Imagens de Jogo

Este projeto tem como objetivo calcular áreas em uma imagem de um jogo utilizando integração numérica, especificamente os métodos dos Trapézios e Simpson. A partir de uma imagem fornecida, o usuário pode definir pontos de referência para calcular a área de uma região e, em seguida, converter essa área de pixels para metros quadrados, usando a escala definida por uma imagem adicional (de um personagem no jogo).

---

## **Pré-requisitos**

Certifique-se de que você tem as seguintes bibliotecas instaladas:

- `matplotlib` (para exibição e manipulação de imagens)
- `numpy` (para operações matemáticas)

Você pode instalar as dependências necessárias usando o `pip`:

```bash
pip install matplotlib numpy
```
---

## **Estrutura do Projeto**

O projeto consiste em dois principais blocos de código:

1. **Cálculo de escala a partir da altura de um campeão no jogo**
   - O usuário seleciona os pontos correspondentes ao topo da cabeça e aos pés de um campeão na imagem.
   - A altura real do campeão é fornecida e, a partir dessa informação, a escala (em metros por pixel) é calculada.

2. **Cálculo da área a partir da imagem de um gráfico (exemplo do jogo)**
   - Através de uma imagem, o usuário seleciona os pontos superiores e inferiores em diferentes fatias verticais da região de interesse.
   - O código utiliza a integração numérica (Trapézios ou Simpson) para estimar a área sob uma curva representada na imagem.

---

## **Passos para Uso**

### **1. Cálculo da Área**

1. **Seleção de pontos**:
   - O código solicitará que o usuário clique nas bordas superior e inferior de cada uma das fatias verticais em uma imagem fornecida (imagem "Screen06.png").
   - O número de fatias e os limites horizontais da imagem são configuráveis.

2. **Cálculo da área**:
   - O código calculará a área utilizando o método dos Trapézios e o método de Simpson.
   - A área é calculada em pixels e convertida para metros quadrados utilizando a escala fornecida.

3. **Fator de ajuste**:
   - O código aplica um fator de ajuste para multiplicar os resultados finais, permitindo calibrar a medição de acordo com necessidades específicas.

### **2. Cálculo da Escala (Imagem do Campeão)**

1. **Seleção de pontos**:
   - O usuário seleciona o topo da cabeça e os pés do campeão em uma imagem (imagem "Screen07.png").
   
2. **Cálculo da escala**:
   - A altura real do campeão é fornecida, e a escala (em metros por pixel) é calculada com base na altura medida em pixels.

3. **Exibição de resultados**:
   - O código exibe a altura medida em pixels, a altura real do campeão, a escala calculada e a escala ao quadrado (para conversão de áreas).

---

## **Como Funciona**

### **1. Seleção de Pontos na Imagem**

Através da função `ginput()` da biblioteca `matplotlib`, o usuário seleciona pontos clicando na imagem. O número de pontos e a lógica de organização dependem do que se deseja calcular.

- **Para calcular a área**: O usuário deve clicar nas bordas superior e inferior de cada fatia.
- **Para calcular a altura de um campeão**: O usuário seleciona o topo da cabeça e os pés.

### **2. Cálculo da Área**

- **Método dos Trapézios**: A área é estimada utilizando a fórmula dos trapézios, que é uma aproximação da integral de uma função.
  
- **Método de Simpson**: Utiliza uma aproximação mais precisa que combina trapézios com parabólicas.

- **Conversão para metros quadrados**: A área é convertida de pixels para metros quadrados com base na escala definida.

### **3. Exibição dos Resultados**

O código mostra os resultados em duas partes:

- **Área calculada em pixels**.
- **Área convertida para metros quadrados**, levando em consideração a escala e o fator de ajuste.

---

## **Exemplo de Execução**

1. O código solicita que o usuário clique em pontos na imagem da região de interesse (no caso, "Screen06.png").
2. O usuário é então solicitado a selecionar a altura do campeão (em "Screen07.png") para determinar a escala.
3. O código calcula a área e exibe o resultado, incluindo a conversão para metros quadrados.

---

## **Considerações Finais**

- **Escala**: A precisão dos cálculos depende da exatidão dos pontos selecionados pelo usuário.
- **Imagens**: As imagens "Screen06.png" e "Screen07.png" são exemplos e devem ser fornecidas com o formato correto para o código funcionar corretamente.
- **Fator de ajuste**: O código inclui um fator de ajuste configurável para calibrar o resultado da área.

---

## **Possíveis Melhorias**

- Adicionar suporte para múltiplas imagens e escalas dinâmicas.
- Permitir mais métodos de integração para maior flexibilidade.
- Melhorar a interface de usuário com mensagens mais informativas.

---

## **Apresentação**

[Projeto-Final-Calculo-Numerico.pdf](https://github.com/user-attachments/files/22690727/Projeto-Final-Calculo-Numerico.pdf)

