import dash
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from assets.filters import filters
from assets.navbar import navbar
from assets.dashboard import dashboard

data_categories = pd.read_csv("data/data_emisje.csv")

data_scopes = pd.read_csv("data/data_zakresy.csv")

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
                "scope": [],
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


# layout callbacks (collapse, modals, etc)
@app.callback(  # filter header
    Output("filter-collapse", "is_open"),
    Input("filter-header-btn", "n_clicks"),
    State("filter-collapse", "is_open"),
)
def open_close_filter_collapse(n, current_state):
    if n == 0:
        raise dash.exceptions.PreventUpdate()
    return not current_state


# open-close filter tab
@app.callback(  # filter header icon
    Output("filter-header-icon", "children"), Input("filter-collapse", "is_open")
)
def switch_filter_header_icon(is_open):
    if is_open:
        return "keyboard_arrow_up"
    else:
        return "keyboard_arrow_down"


@app.callback(
    Output("company", "options"),  # update dropdown options
    Input("filters-store", "data"),  # trigger on app load (or stored filters)
)
def update_company_dropdown(_):
    companies = data_categories["spolka"].unique()
    return [{"label": company, "value": company} for company in companies]


@app.callback(
    Output("company", "value"),  # update selected value
    Input("company", "options"),  # when options update
)
def set_default_company(options):
    if options:
        return [
            option["value"] for option in options
        ]  # first company selected by default
    return []


"""
@app.callback(
    Output("company", "options"),  # Update dropdown options
    Input("filters-store", "data"),  # Trigger on app load (or stored filters)
)
def update_company_dropdown(_):
    companies = data_categories["Spolka"].unique()

    # Add "Select All" option
    options = [{"label": "Select All", "value": "ALL"}] + [
        {"label": company, "value": company} for company in companies
    ]

    return options

def set_default_company(options, selected_values):
    if not selected_values:
        return []

    all_companies = [opt["value"] for opt in options if opt["value"] != "ALL"]

    if "ALL" in selected_values:
        return all_companies  # all companies when "Select All" is chosen
    elif set(selected_values) == set(all_companies):
        return ["ALL"]  # all companies are manually selected, switch to "ALL"
    return selected_values
"""


@app.callback(
    Output(
        {"type": "graph", "index": "emisje_spolki"}, "figure"
    ),  # ID must match the figure in the layout
    Input("company", "value"),  # dropdown selection
)
def update_boxplot(selected_companies):
    if not selected_companies:
        raise dash.exceptions.PreventUpdate()

    # filter based on selected companies
    # filtered_df = data_categories[data_categories["Spolka"].isin(selected_companies)][["Spolka", "Emisja CO2", "Kategoria Emisji"]]

    filtered_df = data_categories[data_categories["spolka"].isin(selected_companies)]
    filtered_df = filtered_df.sort_values(
        by="emisja_co2", ascending=False
    )  # Sort by emission in descending order

    fig = px.bar(
        filtered_df,
        x="spolka",
        y="emisja_co2",
        color="kategoria_emisji",
    )

    fig.update_layout(
        xaxis_title="Company",
        yaxis_title="Emission Category",
        transition_duration=500,  # transition effect
    )

    return fig


"""
@app.callback(
    Output(
        {"type": "graph", "index": "emisje_kategorie"}, "figure"
    ),  # ID must match the figure in the layout
    Input("company", "value"),  # dropdown selection
)
def update_boxplot(selected_companies):
    if not selected_companies:
        raise dash.exceptions.PreventUpdate()

    # filter based on selected companies
    # filtered_df = data_categories[data_categories["Spolka"].isin(selected_companies)][["Spolka", "Emisja CO2", "Kategoria Emisji"]]

    filtered_df = data_categories[data_categories["Spolka"].isin(selected_companies)]
    filtered_df = filtered_df.sort_values(
        by="Emisja CO2", ascending=False
    )  # Sort by emission in descending order

    fig = px.bar(
        filtered_df,
        x="Kategoria Emisji",
        y="Emisja CO2",
        color="Spolka",
    )

    fig.update_layout(
        xaxis_title="Company",
        yaxis_title="Emission Category",
        transition_duration=500,  # transition effect
    )

    return fig
"""


if __name__ == "__main__":
    app.run(debug=True)
