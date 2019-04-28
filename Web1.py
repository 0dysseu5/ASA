import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import os
import plotly.graph_objs as go
key = 'a8vwNErKiJvtnETZJE4b'
os.environ["QUANDL_API_KEY"] = key


startd = datetime.datetime(2015,1,1)
endd= datetime.datetime.now()

print(startd)
stock = 'AAPL.US'


df = web.DataReader(stock, 'quandl', start = startd, end = endd, retry_count=3, pause=0.1)
print(df.head())
app = dash.Dash()


app.layout = html.Div(children = [
    html.H1('Header'),
    dcc.Graph(
        figure=go.Figure(
            data=[  go.Scatter( x=df.index, y= df.Close, name='apple'  ) ],
            layout=go.Layout(
                title='Apple',
                showlegend=True,
                legend=go.layout.Legend(
                    x=0,
                    y=1.0
                ),
                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
            )
        ),
        style={'height': 300},
        id='my-graph'
    )
])


if __name__ == '__main__':
    app.run_server(debug = True)
