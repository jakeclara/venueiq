import dash_bootstrap_components as dbc
from dash import dcc
from utils.constants import MONTHS, YEARS


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

card_content = [
    dbc.CardHeader("Select a period"),
    dbc.CardBody(filter_dropdowns)
]

month_year_filters = dbc.Row(
        dbc.Col(
            dbc.Card(card_content, color="light", outline=True),
            className="col-12 col-sm-12 col-md-8 col-lg-5"
        )
    )
