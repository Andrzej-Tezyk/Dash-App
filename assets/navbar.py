import dash_bootstrap_components as dbc
from dash import html

navbar = dbc.NavbarSimple(
    [
        dbc.NavItem(
            dbc.NavLink(
                html.Img(
                    src="utils/plotly-logo.png",
                    alt="Plotly Dash Info",
                    id="plotly-dash-logo",
                ),
                href="https://plotly.com/",
                target="_blank", # open document in a new window tab
                className="p-1",
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                dbc.Button(
                    html.Span(
                        "info",
                        className="material-symbols-outlined d-flex nav-span",
                    ),
                    color="primary",
                    id="page-info-btn",
                    n_clicks=0,
                )
            )
        ),
    ],
    brand="Dashboard Info",
    brand_href="/",
    id="navbar",
    color="primary",
    dark=True, # text color
)