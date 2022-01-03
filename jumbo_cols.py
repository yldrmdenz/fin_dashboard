import dash_bootstrap_components as dbc
import dash_html_components as html
"""
Creation of jumbotrons for a better Homepage display 
"""
left_jumbotron = dbc.Col(
    html.Div(
        [
            html.H2("Your Favorite Finance Hub", className="display-3"),
            html.Hr(className="my-2"),
            html.P(
                "Get the latest news from the news agencies "
                "And track the live Stock & Crypto data. Free."
            ),
        ],
        className="h-100 p-5 text-white bg-dark rounded-1",
    ),
    md=12,
)

right_jumbotron = dbc.Col(
    html.Div(
        [
            html.Hr(className="my-2"),
        ],
        className="h-100 p-5 bg-light border rounded-3",
    ),
    md=16,
)

jumbotron = dbc.Row(
    [left_jumbotron],
    className="align-items-md-stretch",
)
second_jumbotron = dbc.Row(children=[right_jumbotron],
                           className="align-items-md-stretch"
                           )
