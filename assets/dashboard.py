import dash_bootstrap_components as dbc
from dash import html

from .components.figure import Figure

dashboard = dbc.Row(
    dbc.Col(
        [
            dbc.Row(
                dbc.Col(
                    Figure("Emisje tCO2 - Spółki", id="emisje_spolki"),
                    width=12,
                    ),
                    class_name="row-dashboard",
                ),
            dbc.Row(
                dbc.Col(
                    Figure("Emisje tCO2 - Kategorie", id="emisje_kategorie"), 
                    width=12,
                    ),
                    class_name="row-dashboard",
                ),
            dbc.Row(
                [
                    dbc.Col(
                        Figure("Emisje tCO2 - Zakresy", id="emisje_zakresy"),
                        sm=12, # take max width on a large screen
                        md=6, # 6/12 grid places if screen is medium
                        ), 
                    dbc.Col(
                        Figure("Emisje tCO2 - Grupa Lącznie", id="emisje_zakresy_lacznie"),
                        sm=12,
                        md=6,
                        ),
                ],
                class_name="row-dashboard",
            ),
        ],
    ),
)
