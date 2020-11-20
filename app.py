import numpy 
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

server = app.server

card_header = dbc.Row([
            dbc.Col([dbc.Card([
                html.Div('Breast Cancer Prediction Analytics')
                ], className= ['ml-4', 'mr-4', 'mt-4', 'mb-4'], style = {'align-items':'center', 'font-size':'30px'})
            ], width=11),
            dbc.Col([html.Img(src ='/assets/logo.jfif', style={'height':'50px', 'margin-top':'1.5rem', 'margin-right':'2rem'})], width=1)
])

# content_card = dbc.card([
#                 dbc
# ])

app.layout = card_header


if __name__ == '__main__':
    app.run_server(debug=True)

