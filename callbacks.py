from dash.dependencies import Input,Output
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import requests
from yahoo_fin import stock_info as si
import datetime
from app import app
import news_api

btc_live = []
time_live = []

@app.callback(
    Output('left-graph', 'figure'),
    [Input('select-stock', 'value')]
)
def update_stock_graph(input_data):
    """
    Displays the  Historical Data of selected one(s).
    :param input_data: takes the shortcodes of the stocks
    :return: dcc.Graph elements as data and layout
    """
    import yahoo_fin.stock_info as si
    ret_data = {}
    if input_data is None:
        return {'data': None, 'layout': None}
    for symbol in input_data:
        ret_data[symbol] = si.get_data(symbol)
    return {
        'data'  : [go.Scatter(x=ret_data[i].index, y=ret_data[i]['high'], name=i)
                   for i in ret_data.keys()],
        'layout': {'title': 'Stock Historical Data'}}


# 'paper_bgcolor' : "rgba(0, 0, 0, 0)" ,
# 'plot_bgcolor' : "rgba(0, 0, 0, 0)"}
#
# @app.callback([Output('data-table', 'data'),
#                Output('data-table', 'columns')],
#               [Input('interval-component', 'n_intervals')]
#               )
# def update_currency_rate(update):
#     import requests
#     url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=TRY&apikey=XCF8WUVWCGG3VAXS'
#     # r = requests.get ( url )
#     # data = r.json()
#     # print(data)
#     # print(f'this is the rate {data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]}')
#     data = si.get_currencies()
#     data = data.drop(['52 Week Range', 'Day Chart'], axis=1)
#     columns = [{'name': col, 'id': col} for col in data.columns]
#     data = data.to_dict(orient='records')
#
#     return data, columns


@app.callback([Output('crypto-table', 'data'),
               Output('crypto-table', 'columns'),
               Output('btc-graph', 'figure'),
               ],
              [Input('interval-component', 'n_intervals')]
              )
def update_currency_rate(update):
    """

    :param update: takes only the interval to retreive the latest data.
    :return:
    :data: used as dcc Element
    :layout : used as dcc Element
    :dict : returns the live updating btc graph
    """
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=TRY&apikey=XCF8WUVWCGG3VAXS'
    # r = requests.get ( url )
    # data = r.json()
    # print(data)
    # print(f'this is the rate {data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]}')
    crypto_data = si.get_top_crypto()
    allowed_columns = ['Symbol', 'Name', 'Price (Intraday)', 'Change', '% Change']
    columns = [{'name': col, 'id': col} for col in allowed_columns]
    data = crypto_data.to_dict(orient='records')
    btc_live.append(data[0]['Price (Intraday)'])
    time_live.append(datetime.datetime.now())
    btc_live_graph = go.Scatter(x=time_live, y=btc_live)
    return data, columns, {
        'data'  : [go.Scatter(x=time_live, y=btc_live)]
        ,
        'layout': {'title': 'Live BTC/USD Data'}}


# @app.callback([Output('try-table', 'data'),
#                Output('try-table', 'columns')],
#               [Input('interval-component', 'n_intervals')]
#               )
# def update_try_currency(update):
#     headers = {'User-agent': 'Mozilla/5.0'}
#     site = "https://www.bloomberght.com/doviz"
#     tables = pd.read_html(requests.get(site, headers=headers).text)
#     result = tables[0]
#     data = result.to_dict(orient='records')
#     columns = [{'name': str(col), 'id': str(col)} for col in result.columns]
#     print(data)
#     return data, columns


@app.callback([Output('yahoo-fin-cont', 'children'),
               Output('wash-post-cont', 'children'),
               Output('fin-times-cont', 'children')],
              Input('interval-component', 'n_intervals'))
def update_news(refresh) :
    """
    Generates the columns for each news source

    :param refresh: takes the n_interval to refresh regularly
    :return: returns list_of_yf ,list_of_wp ,list_of_ft
    """
    list_of_yf = []
    list_of_wp = []
    list_of_ft = []
    for source in news_api.parse_rss_data() :
        for new in source.values() :
            if new['title'] == 'Yahoo Finance' :
                list_of_yf.append(dbc.ListGroupItem(
                    [
                        html.Div(
                            [
                                html.H5(new['title'], className="mb-1"),
                                html.Small("Breaking!", className="text-success"),
                            ],
                            className="d-flex w-100 justify-content-between",
                        ),
                        html.P(new['body'], className="mb-1"),
                        html.Small("Plus some small print.", className="text-muted"),
                    ]
                ))
            if new['title'] == 'Washington Post' :
                list_of_wp.append(dbc.ListGroupItem(
                    [
                        html.Div(
                            [
                                html.H5(new['title'], className="mb-1"),
                                html.Small("Breaking!", className="text-success"),
                            ],
                            className="d-flex w-100 justify-content-between",
                        ),
                        html.P(new['body'], className="mb-1"),
                        #html.Small("Plus some small print.", className="text-muted"),
                    ]
                ))
            if new['title'] == 'Financial Times' :
                list_of_ft.append(dbc.ListGroupItem(
                    [
                        html.Div(
                            [
                                html.H5(new['title'], className="mb-1"),
                                html.Small("Breaking!", className="text-success"),
                            ],
                            className="d-flex w-100 justify-content-between",
                        ),
                        html.P(new['body'], className="mb-1"),
                        html.Small("Plus some small print.", className="text-muted"),
                    ]
                ))
    return list_of_yf, list_of_wp, list_of_ft