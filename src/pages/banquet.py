# banquet page: an at-a-glance view of banuquet event KPIs and metrics

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from src.components.core import cards
from src.partials import make_page_header, make_month_year_filters

dash.register_page(__name__,
                   name="Banquet",
                   description="YTD and monthly event metrics"
)

# define chart divs to hold callback otput
monthly_summary_card =  html.Div(id="event-monthly-summary-card")
ytd_bar_chart = dcc.Graph(
    id="event-ytd-bar-chart",
    figure={},
    style={"height": "var(--chart-height)"}
)
num_events_card = html.Div(id="num-events-card")
num_high_value_events_card = html.Div(id="num-high-value-events-card")
avg_event_sales_card = html.Div(id="avg-event-sales-card")
top_five_events_card = html.Div(id="top-five-events-card")
event_type_pie_chart = dcc.Graph(
    id="event-type-pie-chart",
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
            monthly_summary_card
        ], xs=12, lg=6, className="mb-4"),
        dbc.Col([
            cards.make_chart_card(
                "YTD Summary",
                ytd_bar_chart
            )
        ], xs=12, lg=6, className="mb-4"),
    ]),

    dbc.Row([
        dbc.Col([
            num_events_card
        ], xs=12, lg=4, className="mb-4"),
        dbc.Col([
            num_high_value_events_card
        ], xs=12, lg=4, className="mb-4"),
        dbc.Col([
            avg_event_sales_card
        ], xs=12, lg=4, className="mb-4"),
    ]),

    dbc.Row([
        dbc.Col([
            top_five_events_card
        ], xs=12, lg=6, className="mb-4"),
        dbc.Col([
            cards.make_chart_card(
                "Sales by Event Type",
                event_type_pie_chart,
                "YTD"
            )
        ], xs=12, lg=6, className="mb-4"),
    ]),
])