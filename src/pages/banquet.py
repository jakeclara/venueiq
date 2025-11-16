# banquet page: an at-a-glance view of banuquet event KPIs and metrics

import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

# define chart divs to hold callback otput
num_events_mtd_card = html.Div("Number of events MTD", id="num-events-mtd-card")
num_events_ytd_card = html.Div("Number of events YTD", id="num-events-ytd-card")
event_mtd_summary_bar_chart = html.Div("Bar chart with MTD Actual, Monthly Budget, PY Actual", id="event-mtd--bar-chart")
event_ytd_summary_bar_chart = html.Div("Bar chart with YTD Actual, YTD Budget, PY Actual", id="event-ytd--bar-chart")
num_high_revenue_events_card = html.Div("Number of events generating $5,000+", id="num-high-revenue-events-card")
top_five_grossing_events_bar_chart = html.Div("Top 5 grossing events", id="top-five-grossing-events-bar-chart")
avg_revenue_per_event_card = html.Div("Average revenue per event (MTD)", id="avg-revenue-per-event-card")
event_type_mix_chart = html.Div("Event type mix", id="event-type-mix-pie-chart")

# define layout with dbc rows and cols, add divs with visualizations to the columns
layout = html.Div([
    html.H1('This is our Banquet page'),
    html.Div('This is our Banquet page content.'),
    
    dbc.Row([dbc.Col(num_events_mtd_card), dbc.Col(num_events_ytd_card)],
            className="mb-2",
            id="banquet-row-1"),

    dbc.Row([dbc.Col(event_mtd_summary_bar_chart),dbc.Col(event_ytd_summary_bar_chart)],
            className="mb-2",
            id="banquet-row-2"),

    dbc.Row([dbc.Col(num_high_revenue_events_card), dbc.Col(top_five_grossing_events_bar_chart)],
            className="mb-2",
            id="banquet-row-3"),

    dbc.Row([dbc.Col(avg_revenue_per_event_card), dbc.Col(event_type_mix_chart)],
            className="mb-2",
            id="banquet-row-4"),
])