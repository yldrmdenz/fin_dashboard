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
import layouts
import callbacks
from app import app,server


app.layout = html.Div(
    children=[
        dbc.Navbar(
            className='nav-bar',
            children=[
                dbc.NavLink('Crypto Currencies', id='crypto-page', href='/page-crypto',external_link=True),
                      dbc.NavLink('Finance News', id='news-page', href='/page-news',external_link=True),
                      dbc.NavLink('Stock Data', id='stock-page', href='/page-stock',external_link=True),
                      dbc.NavLink('My Assets', id='assets-page', href='/page-assets',external_link=True),
                      ],
            sticky="top",
            color="primary",
        ),
        dcc.Location(id='url',refresh=False),
        dcc.Interval(
            id='interval-component',
            interval=5 * 1000,  # in milliseconds
            n_intervals=0
        ),
        html.Div(id='page-content')
    ]
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def page_changer(page):
    if page == '/page-crypto':
        return layouts.layout_crypto
    elif page == '/page-news':
        return layouts.layout_news
    elif page == '/page-stock':
        return layouts.layout_stock
    elif page == '/page-assets':
        return layouts.layout_assets
    else:
        return html.Div('Hello this is Deniz')


if __name__ == "__main__":
    app.run_server(debug=True)