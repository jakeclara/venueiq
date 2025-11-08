import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

# define chart divs to hold callback otput
restaurant_statement_table = html.Div("Table to display restaurant financials similar to P&L", id="restaurant-statement-table")


# define layout with dbc rows and cols, add divs with visualizations to the columns
layout = html.Div([
    html.H1('This is our Restaurant Statement page'),
    html.Div('This is our Restaurant Statement page content.'),
    
    dbc.Row(dbc.Col(restaurant_statement_table),
            className="mb-2",
            id="restaurant-statement-row-1")
])