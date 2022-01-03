import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import layouts
from app import app
from jumbo_cols import jumbotron, second_jumbotron
from news_api import parse_rss_data


app.layout = html.Div(
    children=[
        dbc.Navbar(
            class_name="navbar navbar-expand-lg navbar-light bg-light",
            className='nav-bar',
            children=[
                dbc.NavLink('Crypto Currencies', id='crypto-page', href='/page-crypto', external_link=True),
                dbc.NavLink('Finance News', id='news-page', href='/page-news', external_link=True),
                dbc.NavLink('Stock Data', id='stock-page', href='/page-stock', external_link=True),
                dbc.NavLink('My Assets', id='assets-page', href='/page-assets', external_link=True),
            ],
            sticky="top",
            color="primary",
        ),
        html.Iframe(src="https://tr.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=1,2,4,6,66,97,18", width="100%" ,height='400px' ),        dcc.Location(id='url', refresh=False),
        dcc.Interval(
            id='interval-component',
            interval=60*1000,  # in milliseconds
            n_intervals=0
        ),
        jumbotron,
        second_jumbotron,
        dbc.Row(children=[
            dbc.Col(dbc.ListGroupItem(id='yahoo-fin-cont')),
            dbc.Col(dbc.ListGroupItem(id='wash-post-cont')),
            dbc.Col(dbc.ListGroupItem(id='fin-times-cont')),
        ], id='news-list-group'),
        html.Div(id='page-content')
    ]
)


@app.callback([Output('yahoo-fin-cont', 'children'),
               Output('wash-post-cont', 'children'),
               Output('fin-times-cont', 'children')],
              Input('interval-component', 'n_intervals'))
def update_news(refresh) :

    list_of_yf = []
    list_of_wp = []
    list_of_ft = []
    for source in parse_rss_data() :
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
                        html.Small("Plus some small print.", className="text-muted"),
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

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def page_changer(page) :
    if page == '/page-crypto' :
        return layouts.layout_crypto
    elif page == '/page-news' :
        return layouts.layout_news
    elif page == '/page-stock' :
        return layouts.layout_stock
    elif page == '/page-assets' :
        return layouts.layout_assets
    else :
        return html.Div('')


if __name__ == "__main__" :
    app.run_server(debug=True)
