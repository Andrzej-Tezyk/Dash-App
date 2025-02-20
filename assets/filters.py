import dash_bootstrap_components as dbc
from dash import html, dcc

filters = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        dbc.Tooltip(
                            "Click to show filters",
                            id="filter-tooltip",
                            placement="left",
                            target="filter-header-btn",
                        ),
                        dbc.Button(
                            [
                                html.P("Filters", className="m-0 fs-5"),
                                html.Span(
                                    "keyboard_arrow_down",
                                    id="filter-header-icon",
                                    className="material-symbols-outlined",
                                ),
                            ],
                            id="filter-header-btn",
                            className="w-100 p-3 d-flex justify-content-between",
                            color="light",
                            n_clicks=0,
                        ),
                    ],
                    className="m-0",
                    style={"padding": "0.1rem", "background-color": "white", "border": "none"},
                ),
                dbc.Collapse(
                    dbc.CardBody(
                        dbc.Stack(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Label(
                                                    "Company",
                                                    html_for="company",
                                                ),
                                                dcc.Dropdown(
                                                    id="company",
                                                    multi=True,
                                                    value=[],
                                                ),
                                            ],
                                            md=9,
                                            sm=12,
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Label(
                                                    "Range",
                                                    html_for="range",
                                                ),
                                                dcc.Checklist(
                                                    options={
                                                        "Z1": " Zakres 1",
                                                        "Z2": " Zakres 2",
                                                        "Z3": " Zakres 3",
                                                    },
                                                    value=["Z1", "Z2", "Z3"],
                                                    id="range",
                                                    className="d-flex justify-content-evenly",
                                                    inline=False,
                                                ),
                                            ],
                                            md=3,
                                            sm=12,
                                        ),
                                    ]
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Label(
                                                    "Emission type",
                                                    html_for="emission-type",
                                                ),
                                                dcc.Dropdown(
                                                    id="emission-type",
                                                    multi=True,
                                                    value=[],
                                                ),
                                            ],
                                            md=9,
                                            sm=12,
                                        )
                                    ],
                                    justify="center",
                                ),
                                dbc.Row(
                                    dbc.Col(
                                        dbc.Button(
                                            "Clear Filters",
                                            id="clear-filters-btn",
                                            color="link",
                                            n_clicks=0,
                                        ),
                                        className="d-flex justify-content-end",
                                    )
                                ),
                            ],
                            gap=3,
                        )
                    ),
                    id="filter-collapse",
                    is_open=False,
                ),
            ],
            style={"border-radius": "20px", "border": "none"},
        )
    ),
    id="filters",
)
