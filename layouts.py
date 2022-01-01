import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from api_receiver import get_stock_market_data
import dash_table as dt
import yahoo_fin.stock_info as si
from yahoo_fin import news
import requests
import datetime
import pandas as pd

layout_crypto = html.Div(
                      children=[
                          dbc.Label('Crypto Currencies'),
                          html.Div(id='split-column-2',
                                   children=[dcc.Interval(
                                       id='interval-component',
                                       interval=5 * 1000,  # in milliseconds
                                       n_intervals=0
                                   ),
                                             dt.DataTable(id='crypto-table', editable=True),
                                             ]
                                   ),
                      ]
                      )


layout_news = html.Div(
                      children=[
                          dbc.Label('News Dashboard'),
                          html.Div(id='split-column-1',
                                   children=[
                                       dcc.Dropdown(id='select-stock',
                                                    multi=True,
                                                    options=[{'label': str(i), 'value': i} for i in
                                                             get_stock_market_data()]
                                                    ),
                                       dcc.Graph(id='left-graph'),

                                   ]
                                   ),
                      ]
                      )


layout_stock = html.Div(
                      children=[
                          html.Div(id='split-column-1',
                                   children=[
                                       dcc.Dropdown(id='select-stock',
                                                    multi=True,
                                                    options=[{'label': str(i), 'value': i} for i in
                                                             get_stock_market_data()]
                                                    ),
                                       dcc.Graph(id='left-graph'),
                                   ]
                                   ),
                      ]
                      )


layout_assets = html.Div(
                      children=[
                          dbc.Label('Assets Dashboard'),
                          html.Div(id='split-column-1',
                                   children=[
                                       dcc.Dropdown(id='select-stock',
                                                    multi=True,
                                                    options=[{'label': str(i), 'value': i} for i in
                                                             get_stock_market_data()]
                                                    ),
                                       dcc.Graph(id='left-graph'),
                                   ]
                                   ),
                          html.Div(id='split-column-2',
                                   children=[html.Div(id='usd-try'),
                                             dt.DataTable(id='data-table', editable=True),
                                             ]
                                   ),
                      ]
                      )
