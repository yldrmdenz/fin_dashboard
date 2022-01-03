import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import layouts
import callbacks
from app import app,server
app.layout = html.Div(
    children=[
        dbc.Navbar(
            class_name="navbar navbar-expand-lg navbar-light bg-light",
            className='nav-bar',
            children=[
                dbc.NavLink('Home', id='news-page', href='/', external_link=True),
                dbc.NavLink('Crypto Currencies', id='crypto-page', href='/page-crypto', external_link=True),
                dbc.NavLink('Stock Data', id='stock-page', href='/page-stock', external_link=True),
                dbc.NavLink('My Assets', id='assets-page', href='/page-assets', external_link=True,disabled=True),
                dbc.NavLink('Predictions & Analysis', id='ml-page', href='/page-ml', external_link=True,disabled=True),
            ],
            sticky="top",
            color="primary",
        ), dcc.Location(id='url', refresh=False),
        dcc.Interval(
            id='interval-component',
            interval=60*1000,  # in milliseconds
            n_intervals=0
        ),
        html.Div(id='page-content')
    ]
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def page_changer(page) :
    if page == '/' :
        return layouts.layout_home
    elif page == '/page-crypto' :
        return layouts.layout_crypto
    elif page == '/page-stock' :
        return layouts.layout_stock
    elif page == '/page-assets' :
        return layouts.layout_assets
    else :
        return html.Div('')


if __name__ == "__main__" :
    app.run_server(debug=True)
