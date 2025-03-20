import dash_bootstrap_components as dbc
from dash import html

navbar = dbc.NavbarSimple(
    dbc.NavItem(
        dbc.NavLink(
            dbc.Button(
                html.Span(
                    "info",
                    className="material-symbols-outlined d-flex nav-span",
                ),
                color="danger",
                id="page-info-btn",
                n_clicks=0,
            )
        )
    ),
    brand="Dashboard Info",
    brand_href="/",
    id="navbar",
    color="danger",
    dark=True,  # text color
)
