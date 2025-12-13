# home page: an at-a-glance view of combined (restaurant and banquet) venue KPIs and metrics

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from src.components.core import cards
from src.partials import make_month_year_filters, make_page_header

# set path to '/' otherwise would auto to '/home'
dash.register_page(__name__, 
                   path='/',
                   title="Home | Main Dashboard",
                   name="Home",
                   description="Facility-wide summary (restaurant + events)")

# define charts and divs to hold callback otput
monthly_revenue_progress_chart = dcc.Graph(
    id="monthly-revenue-progress-chart",
    figure={},
    style={"height": "var(--chart-height)"}
)
monthly_summary_card =  html.Div(id="monthly-summary-card")
ytd_revenue_card =  html.Div(id="ytd-revenue-card")
cogs_kpi_card =  html.Div(id="cogs-kpi-card")
profit_card = html.Div(id="profit-card")
top_menu_item_card = html.Div(id="top-menu-item-card")
top_event_card = html.Div(id="top-event-card")
revenue_breakdown_pie_chart = dcc.Graph(
    id="revenue-breakdown-pie-chart",
    figure={},
    style={"height": "var(--chart-height)"}
)


# define layout with dbc rows and cols
layout = html.Div([
    make_page_header(
        page_name=__name__,
        filter_component=make_month_year_filters()
    ),

    dbc.Row([
        dbc.Col([
            cards.make_chart_card(
                "% of Budgeted Monthly Revenue",
                monthly_revenue_progress_chart
            )
        ], xs=12, lg=6, className="mb-4"),
        dbc.Col([
            monthly_summary_card
        ], xs=12, lg=6, className="mb-4"),
    ]),
    dbc.Row([
        dbc.Col([
            ytd_revenue_card
        ], xs=12, lg=4, className="mb-4"),
        dbc.Col([
            cogs_kpi_card
        ], xs=12, lg=4, className="mb-4"),
        dbc.Col([
            profit_card
        ], xs=12, lg=4, className="mb-4"),
    ]),
    dbc.Row([
        dbc.Col([
            top_menu_item_card
        ], xs=12, lg=4, className="mb-4"),
        dbc.Col([
            top_event_card
        ], xs=12, lg=4, className="mb-4"),
        dbc.Col([
            cards.make_chart_card(
                "Revenue Breakdown",
                revenue_breakdown_pie_chart
            )
        ], xs=12, lg=4, className="mb-4"),
    ]),
])