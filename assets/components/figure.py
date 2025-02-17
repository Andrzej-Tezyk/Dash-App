import dash_bootstrap_components as dbc
from dash import html, dcc


class Figure(dbc.Card):
    def __init__(self, title, fig_id, description=None):
        super().__init__(
            children=[
                html.Div(  # plot header
                    [
                        html.H5(title, className="m-0 align-center"),
                        dbc.Button(
                            html.Span(
                                "help",  # icon
                                className="material-symbols-outlined d-flex",  # icon style
                            ),
                            id={"type": "graph-info-btn", "index": fig_id},
                            # a dictionary ID pattern to allow callback functions to target specific buttons dynamically
                            # MATCH - do somehthing on multiple elements for the same data
                            # ALL - do something on all elements of this type
                            n_clicks=0,
                            color="light",
                        ),
                    ],
                    className="d-flex justify-content-between align-center p-3",
                ),
                dbc.Spinner(  # spinner when plot is loading
                    dcc.Graph(
                        id={"type": "graph", "index": fig_id},
                        responsive=True,
                        style={"padding": "0.3rem", "height": "100%"},
                    ),
                    size="lg",
                    color="danger",
                    delay_show=750,
                ),
                dbc.Modal(  # popup on help button click
                    [
                        dbc.ModalHeader(html.H4(title)),
                        dbc.ModalBody(dcc.Markdown(description, link_target="_blank")),
                    ],
                    id={"type": "graph-modal", "index": fig_id},
                    is_open=False,
                    size="md",
                ),
            ],
            className="mb-3 figure-card",
            style={"border-radius": "20px"},
        )
