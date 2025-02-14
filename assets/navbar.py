import dash_bootstrap_components as dbc
from dash import html

navbar = dbc.NavbarSimple(
    [
        dbc.NavItem(
            dbc.NavLink(
                html.Img(
                    src="utils/github-mark-white.png",
                    alt="Plotly Dash Info",
                    id="plotly-dash-logo",
                ),
                href="https://plotly.com/",
                target="_blank",
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
                    color="dark",
                    id="page-info-btn",
                    n_clicks=0,
                )
            )
        ),
    ],
    brand="Streaming Metrics",
    brand_href="/",
    id="navbar",
    color="dark",
    dark=True,
)