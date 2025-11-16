# restaurant snapshot page: an at-a-glance view of restaurant KPIs and metrics

import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, title="Restaurant Snapshot")

# define chart divs to hold callback otput
restaurant_mtd_summary_bar_chart = html.Div("Bar chart with MTD Actual, Monthly Budget, PY Actual", id="restaurant-mtd-summary-bar-chart")
restaurant_ytd_summary_bar_chart = html.Div("Bar chart with YTD Actual, YTD Budget, PY Actual", id="restaurant-ytd-summary-bar-chart")
top_five_food_items_bar_chart = html.Div("Top 5 selling food items", id="top-five-food-items-bar-chart")
restaurant_revenue_mix_chart = html.Div("Restaurant revenue mix", id="restaurant-revenue-mix-pie-chart")
hot_menu_items_card = html.Div("Menu item trending up", id="hot-menu-items-card")
cold_menu_items_card = html.Div("Menu item trending down", id="cold-menu-items-card")

# define layout with dbc rows and cols, add divs with visualizations to the columns
layout = html.Div([
    html.H1('This is our Restaurant Snapshot page'),
    html.Div('This is our Restaurant Snapshot page content.'),
    
    dbc.Row([dbc.Col(restaurant_mtd_summary_bar_chart), dbc.Col(restaurant_ytd_summary_bar_chart)],
            className="mb-2",
            id="restaurant-snapshot-row-1"),

    dbc.Row([dbc.Col(top_five_food_items_bar_chart),dbc.Col(restaurant_revenue_mix_chart)],
            className="mb-2",
            id="restaurant-snapshot-row-2"),

    dbc.Row([dbc.Col(hot_menu_items_card), dbc.Col(cold_menu_items_card)],
            className="mb-2",
            id="restaurant-snapshot-row-3")
])