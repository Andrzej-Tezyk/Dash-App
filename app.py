import dash
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

from assets.filters import filters
from assets.navbar import navbar
from assets.dashboard import dashboard

app = Dash(
    __name__,
    title="Python data visualisation",
    external_stylesheets=[
        dbc.themes.LITERA,
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200",  # Icons
        "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap",  # Font
    ],
)
server = app.server

app.layout = html.Div(
    [
        dcc.Store(
            id="filters-store",
            data={
                "company": [],
                "emission-type": [],
                "range": [],
            },
        ),
        navbar,
        dbc.Container(
            dbc.Stack(
                [
                    filters,
                    dashboard,
                ],
                gap=3,
            ),
            id="content",
            className="p-3",
        ),
    ],
    id="page",
)


# Layout callbacks (collapse, modals, etc)
@app.callback(  # filter header
    Output("filter-collapse", "is_open"),
    Input("filter-header-btn", "n_clicks"),
    State("filter-collapse", "is_open"),
)
def open_close_filter_collapse(n, current_state):
    if n == 0:
        raise dash.exceptions.PreventUpdate()
    return not current_state


@app.callback(  # filter header icon
    Output("filter-header-icon", "children"), Input("filter-collapse", "is_open")
)
def switch_filter_header_icon(is_open):
    if is_open:
        return "keyboard_arrow_up"
    else:
        return "keyboard_arrow_down"


# Filter callbacks (initialization, storing, clearing)


if __name__ == "__main__":
    app.run(debug=True)
