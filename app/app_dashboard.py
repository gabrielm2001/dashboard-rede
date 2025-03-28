from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import threading
import time
from . import metrics  # A importação relativa ajuda a localizar o módulo na mesma pasta

# Criando a aplicação Dash
app = Dash(__name__)

# Armazena os dados coletados
latencia_data = []
jitter_data = []
throughput_data = []

# Função para coletar dados periodicamente
def atualizar_dados():
    while True:
        latencia, jitter = metrics.medir_latencia()  # Função que retorna latência e jitter
        throughput = metrics.medir_throughput()  # Função que retorna throughput

        # Adiciona os dados ao histórico
        latencia_data.append(latencia)
        jitter_data.append(jitter)
        throughput_data.append(throughput)

        # Limita o tamanho dos dados armazenados (50 últimos valores)
        if len(latencia_data) > 50:
            latencia_data.pop(0)
            jitter_data.pop(0)
            throughput_data.pop(0)
        
        time.sleep(5)  # Atualiza a cada 5 segundos

# Inicia a coleta em uma thread separada
threading.Thread(target=atualizar_dados, daemon=True).start()

# Layout do Dashboard
app.layout = html.Div(children=[
    html.H1("Monitoramento de Rede"),

    dcc.Graph(id='grafico-latencia'),
    dcc.Graph(id='grafico-jitter'),
    dcc.Graph(id='grafico-throughput'),

    dcc.Interval(id='interval-component', interval=5000, n_intervals=0)  # Atualiza a cada 5s
])

# Callback para atualizar os gráficos dinamicamente
@app.callback(
    [Output('grafico-latencia', 'figure'),
     Output('grafico-jitter', 'figure'),
     Output('grafico-throughput', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def atualizar_graficos(n):
    # Criação das figuras com os dados coletados
    latencia_fig = go.Figure(data=[go.Scatter(y=latencia_data, mode='lines', name="Latência (ms)")])
    jitter_fig = go.Figure(data=[go.Scatter(y=jitter_data, mode='lines', name="Jitter (ms)")])
    throughput_fig = go.Figure(data=[go.Scatter(y=throughput_data, mode='lines', name="Velocidade (Mbps)")])
    
    # Atualiza as figuras com títulos e eixos
    latencia_fig.update_layout(title='Latência ao longo do tempo', xaxis_title='Tempo (s)', yaxis_title='Latência (ms)')
    jitter_fig.update_layout(title='Jitter ao longo do tempo', xaxis_title='Tempo (s)', yaxis_title='Jitter (ms)')
    throughput_fig.update_layout(title='Throughput ao longo do tempo', xaxis_title='Tempo (s)', yaxis_title='Velocidade (Mbps)')

    return latencia_fig, jitter_fig, throughput_fig

if __name__ == '__main__':
    app.run_server(debug=True)
