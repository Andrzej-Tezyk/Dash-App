import dash_bootstrap_components as dbc
from dash import html



dashboard = dbc.Row(
    dbc.Col(
        [
            dbc.Row(dbc.Col(html.Div(figure))),
            dbc.Row(dbc.Col(html.Div(figure))),
            dbc.Row([dbc.Col(html.Div(figure)), dbc.Col(html.Div(figure))]),
        ]
    )
)
