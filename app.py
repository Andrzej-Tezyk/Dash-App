from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from assets.filters import filters

app = Dash(
    __name__,
    title="Dash Demo",
    external_stylesheets=[
        dbc.themes.JOURNAL,
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200",  # Icons
        "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap",  # Font
    ],
)
server = app.server

app.layout = html.Div(
    [
        dbc.Container(
            dbc.Stack(
                [
                    dcc.Markdown(
                        "*Data for this app is pulled from CompanyName excel",
                        id="attribution",
                    ),
                    filters,
                ],
                gap=3,
            ),
            id="content",
            className="p-3",
        ),
    ],
    id="page",
)

if __name__ == "__main__":
    app.run(debug=True)
