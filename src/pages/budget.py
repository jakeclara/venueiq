# budget page: table view of combined (restaurant and banquet) venue budget (P&L-style)

import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

# define chart divs to hold callback otput
budget_table = html.Div("Table to display budget similar to P&L", id="budget-table")


# define layout with dbc rows and cols, add divs with visualizations to the columns
layout = html.Div([
    html.H1('This is our Budget page'),
    html.Div('This is our Budget page content.'),
    
    dbc.Row(dbc.Col(budget_table),
            className="mb-2",
            id="budget-row-1")
])