# year dropdown for filtering budget charts (Bootsrap card component)

import dash_bootstrap_components as dbc
from dash import dcc
from dash.development.base_component import Component

from src.utils.constants import BUDGET_YEARS

def make_year_filter() -> Component:
    """Returns a dbc.Row object with a Year dropdown for filtering budget charts."""
    # row containing the Year dropdown
    filter_dropdown = dbc.Row(
            [

                dbc.Col(
                    dcc.Dropdown(
                        id="year-dropdown", 
                        options=BUDGET_YEARS,
                        value=2025,
                        searchable=False,
                        clearable=False,
                        ), 
                        width=12)
            ],
        )

    # card content: header + dropdowns
    card_content = [
        dbc.CardHeader("Select a Budget Year"),
        dbc.CardBody(filter_dropdown)
    ]

    # full component: responsive Card inside a Row/Col wrapper
    return dbc.Row([
            # empty column for spacing
            dbc.Col(xs=0, lg=6),
            dbc.Col([
                dbc.Card(card_content, color="secondary", outline=True),
            ], xs=6, lg=6),
        ])
