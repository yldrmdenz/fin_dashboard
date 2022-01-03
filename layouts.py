import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from api_receiver import get_stock_market_data
import dash_table as dt
from jumbo_cols import jumbotron, second_jumbotron

layout_crypto = html.Div(
    children=[
        dbc.Label('Crypto Currencies'),
        html.Div(id='split-column-2',
                 children=[dcc.Interval(
                     id='interval-component',
                     interval=5*1000,  # in milliseconds
                     n_intervals=0
                 ),
                     dbc.Row(children=[dbc.Col(children=[dt.DataTable(id='crypto-table', editable=True)],md=6),
                                       dbc.Col(children=[dcc.Graph(id='btc-graph')],md=6)]
                             ),
                 ]
                 ),
    ]
)

layout_home = html.Div(
    children=[
        dbc.Label('Dashboard Homepage(Scroll Down for News)'),
        html.Div(id='split-column-1',
                 children=[
                     jumbotron,
                     html.Iframe(
                         src="https://tr.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,4,6,66,97,18",
                         width="100%", height='400px'),

                     second_jumbotron,
                     html.H2('Latest News',style={'text-align':'center'}),
                     dbc.Row(children=[
                         dbc.Col(dbc.ListGroupItem(id='yahoo-fin-cont')),
                         dbc.Col(dbc.ListGroupItem(id='wash-post-cont')),
                         dbc.Col(dbc.ListGroupItem(id='fin-times-cont')),
                     ], id='news-list-group'),
                 ]
                 ),
    ]
)

layout_stock = html.Div(
    children=[
        html.Div(id='split-column-1',
                 children=[
                     html.H2('Please Pick the Stock(s) you would like to Display from the Dropdown'),
                     html.Div('',style={'height':'100px'}),
                     dcc.Dropdown(id='select-stock',
                                  multi=True,
                                  value=['TSLA'],
                                  options=[{'label' : str(i), 'value' : i} for i in
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
                                  options=[{'label' : str(i), 'value' : i} for i in
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
