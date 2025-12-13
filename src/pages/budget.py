# budget page: table view of combined (restaurant and banquet) venue budget (P&L-style)

import dash
from dash import html
import dash_bootstrap_components as dbc

from src.components.budget import budget_table
from src.partials import make_year_filter, make_page_header


dash.register_page(__name__,
                   name="Budget",
                   description="Budgeted P&L for venue")

# define chart divs to hold callback otput
budget_table = budget_table.make_budget_table(table_id="budget-table")


# define layout with dbc rows and cols, add divs with visualizations to the columns
layout = html.Div([
    make_page_header(
        page_name=__name__,
        filter_component=make_year_filter()
    ),
    
    dbc.Row(dbc.Col(budget_table),
            className="mb-3",
    )
])