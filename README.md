# Projeto Integrado de IoT e IA

**Alunos:** Eduardo Klug, João Artur Belli, Leonardo Rocha, Mateus de Faria da Silva, Mateus Mautone e Renan Iomes.

## Introdução ao Projeto
Este projeto integra tecnologias de Internet das Coisas (IoT) e Inteligência Artificial (IA) com o objetivo de resolver o problema de monitoramento e automação no cuidado de plantas. A solução proposta visa coletar, processar e analisar dados em tempo real sobre as condições de temperatura, umidade e iluminação ao redor das plantas, enviando notificações de alerta quando necessário. A importância desta solução reside na capacidade de melhorar a saúde das plantas, otimizar os recursos e reduzir o desperdício de água e energia.

## Funcionamento Geral
O projeto utiliza sensores IoT para capturar dados ambientais, como temperatura, umidade e intensidade de luz. Esses dados são enviados para uma central de processamento, onde algoritmos de IA, incluindo o uso de lógica Fuzzy, realizam a análise. A lógica Fuzzy é aplicada para lidar com incertezas e variabilidades nos dados, permitindo uma tomada de decisão mais flexível em tempo real.

Os algoritmos de IA utilizam técnicas de aprendizado de máquina e lógica Fuzzy para detectar padrões e tomar decisões. Por exemplo, se a umidade estiver abaixo de um certo nível, o sistema poderá acionar automaticamente a irrigação. A integração entre IoT e IA permite que o sistema funcione de maneira autônoma, realizando ações sem intervenção humana.

## Fluxo de Informações
O fluxo de dados no projeto começa com a captura de informações pelos sensores IoT posicionados em torno das plantas. Esses dados são transmitidos via rede para um servidor central, onde são processados:

1. **Captura de Dados:** Sensores coletam informações de temperatura, umidade e intensidade de luz.
2. **Transmissão:** Os dados são enviados para a central de processamento.
3. **Processamento:** 
   - Limpeza e normalização dos dados.
   - Análise dos dados por algoritmos de IA.
4. **Ação:** Os resultados são enviados aos atuadores IoT, que realizam ações como ativar a irrigação ou ajustar a iluminação.
5. **Visualização:** Os dados e ações são apresentados ao usuário por meio de uma interface de visualização.

## Benefícios e Desafios
**Benefícios:**
- Automação no cuidado de plantas.
- Otimização de recursos como água e energia.
- Melhoria na saúde das plantas.
- Resposta rápida a mudanças nas condições ambientais.

**Desafios:**
- Garantir uma comunicação estável e segura entre os dispositivos IoT e a central de processamento.
- Desenvolver algoritmos de IA que sejam eficientes e robustos o suficiente para operar em tempo real.

## Orçamento
| Item                         | Custo (R$) |
|------------------------------|------------|
| Sensor de Temperatura e Umidade DHT11 | 11,90      |
| Sensor WiFi                  | 25,75      |
| Sensor de Luz                | 00,00      |
| Arduino Uno                  | 00,00      |
| Cabo Jumper                  | 00,00      |
| Resistor                     | 00,00      |

## Diagrama do Projeto
![Diagrama do Projeto](project_diagram.png)
