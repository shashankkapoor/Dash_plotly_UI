from flask import Flask
import dash
from dash import dcc, html,dash_table
import plotly.express as px
import pandas as pd

# Initialize Flask server
server = Flask(__name__)
app = dash.Dash(__name__, server=server, routes_pathname_prefix='/', suppress_callback_exceptions=True)

# Sample Data for Plotly Charts
df = px.data.iris()
fig1 = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
fig2 = px.bar(df, x='species', y='petal_width', color='species')

# Layout as per the given image
app.layout = html.Div([
    html.Link(rel='stylesheet', href='/static/style.css'),
    html.Div("Model Classification", className='title'),
    
    
    html.Div([
        html.Div([
            html.Button("Heading +Drop down", className='dropdown-button'),
            html.Button("Heading +Drop down", className='dropdown-button'),
            html.Button("Heading +Drop down", className='dropdown-button'),
            html.Button("Heading +Drop down", className='dropdown-button'),
            html.Button("Heading +Drop down", className='dropdown-button')
        ], className='sidebar'),
        
        html.Div([
            html.Div([dash_table.DataTable(data=df.to_dict('records'), page_size=5),
                      ], className='csv-data'),
            html.Div([
                dcc.Graph(figure=fig1, className='plotly-chart'),
                dcc.Graph(figure=fig2, className='plotly-chart')
            ], className='charts-container')
        ], className='main-content')
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
