# restaurant snapshot page: an at-a-glance view of restaurant KPIs and metrics

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from src.components.core import cards
from src.partials import make_month_year_filters, make_page_header

dash.register_page(__name__,
                   title="Restaurant Snapshot",
                   name="Restaurant Snapshot",
                   description="Key restaurant KPIs")

# define chart divs to hold callback otput
avg_sales_by_day_line_chart = dcc.Graph(
    id="avg-sales-by-day-line-chart",
    figure={},
    style={"height": "var(--chart-height)"}
)
top_five_menu_items_card = html.Div(id="top-five-menu-items-card")
hot_menu_items_card = html.Div(id="hot-menu-items-card")
cold_menu_items_card = html.Div(id="cold-menu-items-card")
sales_by_category_pie_chart = dcc.Graph(
    id="sales-by-category-pie-chart",
    figure={},
    style={"height": "var(--chart-height)"}
)


# define layout with dbc rows and cols, add divs with visualizations to the columns
layout = html.Div([
    make_page_header(
        page_name=__name__,
        filter_component=make_month_year_filters()
    ),
    
    dbc.Row([
        dbc.Col([
            cards.make_chart_card(
                "Avg Sales by Day",
                avg_sales_by_day_line_chart,
                "Monthly"
            )
        ], xs=12, lg=6, className="mb-4"),
        dbc.Col([
            top_five_menu_items_card
        ], xs=12, lg=6, className="mb-4"),
    ]),

    dbc.Row([
        dbc.Col([
            hot_menu_items_card
        ], xs=12, lg=4, className="mb-4"),
        dbc.Col([
            cold_menu_items_card
        ], xs=12, lg=4, className="mb-4"),
        dbc.Col([
            cards.make_chart_card(
                "Sales by Category",
                sales_by_category_pie_chart,
                "YTD"
            )
        ], xs=12, lg=4, className="mb-4")
    ]),
])