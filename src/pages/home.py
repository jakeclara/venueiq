# home page: an at-a-glance view of combined (restaurant and banquet) venue KPIs and metrics

import dash
from dash import html
import dash_bootstrap_components as dbc

# set path to '/' otherwise would auto to '/home'
dash.register_page(__name__, path='/', title="VenueIQ Main Dashboard")

# define chart divs to hold callback otput
mtd_revenue_progress_chart = html.Div("Percentage of Budget", id="mtd-revenue-progress-chart")
line_chart_ytd =  html.Div("Line chart for YTD figures", id="line-chart-ytd")
home_mtd_summary_card =  html.Div("Text or small card with MTD Actual, Monthly Budget, Variance to budget, PY Actual", id="home-mtd-summary-card")
home_mtd_summary_bar_chart = html.Div("Bar chart with MTD Actual, Monthly Budget, PY Actual", id="home-mtd-summary-bar-chart")
top_menu_item = html.Div("Top selling menu item", id="top-menu-item")
top_grossing_event = html.Div("Top grossing event", id="top-grossing-event")

# define layout with dbc rows and cols, add divs with visualizations to the columns
layout = html.Div([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
    
    dbc.Row([dbc.Col(mtd_revenue_progress_chart), dbc.Col(line_chart_ytd)],
            className="mb-2",
            id="home-row-1"),

    dbc.Row([dbc.Col(home_mtd_summary_card),dbc.Col(home_mtd_summary_bar_chart)],
            className="mb-2",
            id="home-row-2"),

    dbc.Row([dbc.Col(top_menu_item), dbc.Col(top_grossing_event)],
            className="mb-2",
            id="home-row-3")
])