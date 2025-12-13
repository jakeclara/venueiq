# restaurant statement page: table view of restaurant financials (P&L-style)

import dash
from dash import html
import dash_bootstrap_components as dbc

from src.components.core import statement_table
from src.partials import make_month_year_filters, make_page_header

dash.register_page(__name__,
                   title="Restaurant Statement",
                   name="Restaurant Statement",
                   description="Restaurant P&L statement")

# define table to hold callback otput
restaurant_statement_table = statement_table.make_statement_table(
    table_id="restaurant-statement-table"
)


# define layout with dbc rows and cols, add divs with visualizations to the columns
layout = html.Div([
    make_page_header(
        page_name=__name__,
        filter_component=make_month_year_filters()
    ),
    
    dbc.Row(dbc.Col(restaurant_statement_table),
            className="mb-3")
])