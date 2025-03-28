# Monitoramento de Rede com Dashboard Interativo

Este projeto implementa um **dashboard interativo** para monitoramento de métricas de rede, incluindo **latência**, **jitter** e **throughput**. Ele utiliza o **Dash** para exibição visual e o **Speedtest-cli** para medir a velocidade da conexão. A cada 5 segundos, os gráficos são atualizados com as últimas medições, permitindo monitoramento em tempo real da qualidade da rede.

## Funcionalidades

- **Latência (ms):** Medição do tempo de resposta da rede.
- **Jitter (ms):** Medição da variação de latência.
- **Throughput (Mbps):** Medição da velocidade de download da conexão.

### Tecnologias Usadas

- **Dash:** Framework para construção de aplicações web interativas.
- **Plotly:** Biblioteca para criação de gráficos interativos.
- **Speedtest-cli:** Biblioteca para medir o throughput da conexão de internet.
- **Python (3.x):** Linguagem de programação utilizada.

---

## Pré-requisitos

Para executar o projeto, você precisa de:

- **Python 3.x** instalado no seu sistema.
- Conexão com a internet (para realizar as medições de throughput).

---

## Como Iniciar

### 1. Clonando o Repositório

Clone este repositório para o seu ambiente local:

bash:
git clone https://github.com/seu-usuario/dashboard-rede.git

## Instalando as Dependências


Antes de rodar o projeto, você precisa instalar as dependências listadas no `requirements.txt`. Para isso, execute:

```bash
pip install -r requirements.txt
```

Caso não tenha o `pip` instalado, primeiro instale o Python e o `pip` (se necessário).

## Configuração do Projeto

Certifique-se de que o arquivo `metrics.py` tenha as funções necessárias para medir as métricas da rede, especialmente se você estiver utilizando um ambiente diferente para testar as velocidades (exemplo: outro servidor, rede local, etc.). Você pode personalizar as funções `medir_latencia()` e `medir_throughput()` conforme suas necessidades.

## Rodando o Servidor

Depois de instalar as dependências, você pode iniciar o servidor para visualizar o dashboard.

Execute o seguinte comando:

```bash
python run.py
```

O Dash estará rodando no endereço [http://127.0.0.1:8050/](http://127.0.0.1:8050/). Abra esse link no seu navegador para visualizar o dashboard.

## Como Funciona

### Coleta de Dados
O projeto coleta periodicamente (a cada 1 segundo) os dados de latência, jitter e throughput usando a função `medir_latencia()` e `medir_throughput()`.

### Gráficos Dinâmicos
O Dash exibe três gráficos interativos:

- **Latência**: Exibe o tempo de resposta da rede.
- **Jitter**: Exibe a variação da latência.
- **Throughput**: Exibe a velocidade de download da rede.

### Atualizações em Tempo Real
Os gráficos são atualizados a cada 5 segundos, com os últimos dados coletados.

## Como Funcionar em Caso de Erros

Se ocorrer algum erro durante a execução, como a falha de conexão ao servidor de medição de velocidade (Speedtest), o programa pode retornar valores padrão (`0` ou valores aproximados). Se isso acontecer, verifique:

- Sua conexão com a internet.
- O acesso ao servidor de Speedtest.
- A instalação das dependências.

## Contribuições

Se você quiser contribuir para o projeto, fique à vontade para enviar pull requests. Não se esqueça de seguir as diretrizes de contribuição e garantir que o código esteja bem documentado.

## Licença

Este projeto está licenciado sob a Licença MIT.

## Autor(es)

**Gabriel Machado** – Desenvolvimento e implementação do projeto.
**mILA fERRARI** – Desenvolvimento e implementação do projeto.