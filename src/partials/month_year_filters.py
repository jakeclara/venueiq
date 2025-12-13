# month/year dropdowns for filtering charts (Bootsrap card component)

import dash_bootstrap_components as dbc
from dash import dcc
from dash.development.base_component import Component

from src.utils.constants import MONTHS, YEARS

def make_month_year_filters() -> Component:
    """
    Returns a dbc.Row containing a dbc.Col with a Card that has a body
    holding Month and Year dropdowns arranged in a two-column Row.
    """
    # row containing the Month and Year dropdowns
    filter_dropdowns = dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="month-dropdown", 
                        options=MONTHS,
                        value=1,
                        searchable=False,
                        clearable=False,
                        ), 
                        width=6),
                dbc.Col(
                    dcc.Dropdown(
                        id="year-dropdown", 
                        options=YEARS,
                        value=2025,
                        searchable=False,
                        clearable=False,
                        ), 
                        width=6)
            ],
            className="g-3"
        )

    # card content: header + dropdowns
    card_content = [
        dbc.CardHeader("Select a period"),
        dbc.CardBody(filter_dropdowns)
    ]

    # full component: responsive Card inside a Row/Col wrapper
    return dbc.Row(
            dbc.Col(
                dbc.Card(card_content, color="secondary", outline=True),
            )
        )
