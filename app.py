import dash
import dash_bootstrap_components as dbc
import flask
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, "assets/style.css"],suppress_callback_exceptions=True)

server = app.server