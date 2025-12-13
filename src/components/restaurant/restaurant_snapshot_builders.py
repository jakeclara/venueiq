# builds the charts and cards for the restaurant snapshot

import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

from src.components.core import cards, charts
from src.utils.constants import THEME_COLORS

# ------- charts -------
def build_avg_Sales_by_day_chart(avg_sales_by_day: list[dict]) -> go.Figure:
    """
    Builds a line chart of average total sales per day of the week.

    Args:
        avg_sales_by_day (list[dict]): A list of dictionaries containing the day of the week and the average 
        total sales for each day.

    Returns:
        go.Figure: A line chart of average total sales per day of the week.
    """
    avg_sales_by_day_df = pd.DataFrame(avg_sales_by_day)
    avg_sales_by_day_line_chart = charts.make_line_chart(
        avg_sales_by_day_df,
        x="day_of_week",
        y="average_sales",
        markers=True,
        labels={
            "day_of_week": "Day of Week",
            "average_sales": "Average Sales"
        },
        color_discrete_sequence = [THEME_COLORS["info"]]
    )
    avg_sales_by_day_line_chart.update_yaxes(
        tickprefix="$",
        separatethousands=True,
        tickformat=",.0f"
    )

    return avg_sales_by_day_line_chart


def build_sales_by_category_pie_chart(sales_by_category: dict) -> go.Figure:
    """
    Builds a pie chart of total sales grouped by category.

    Args:
        sales_by_category (dict): A dictionary containing the category and total sales for each category.

    Returns:
        go.Figure: A pie chart of total sales grouped by category.
    """
    sales_by_category_df = pd.DataFrame(sales_by_category)
    sales_by_category_pie_chart_colors = {
            "Food": THEME_COLORS["danger"],
            "Beverage": THEME_COLORS["info"],
    }
    sales_by_category_pie_chart = charts.make_pie_chart(
            data=sales_by_category_df,
            names="Category",
            values="Total Sales",
            color_map=sales_by_category_pie_chart_colors,
            title="",
        )
    
    return sales_by_category_pie_chart


# ------- cards -------
def build_top_five_menu_items_card(top_five_menu_items: list[dict]) -> dbc.Card:
    """
    Builds a dbc.Card object with the title, top 5 menu items, and footer.

    Args:
        top_five_menu_items (list[dict]): A list of dictionaries containing the name and total sales of the top 5 menu items.

    Returns:
        dbc.Card: A dbc.Card object with the title, top 5 menu items, and footer.
    """
    top_five_menu_items_card = cards.make_top_n_card(
            title="Top 5 Menu Items",
            headers=["Item", "Total Sales"],
            metrics=top_five_menu_items,
            footer="YTD",
        )
    
    return top_five_menu_items_card


def build_hot_menu_items_card(hot_menu_items: list[dict]) -> dbc.Card:
    """
    Builds a dbc.Card object with the title, hot menu items, and footer.

    Args:
        hot_menu_items (list[dict]): A list of dictionaries containing the name and growth of the hot menu items.

    Returns:
        dbc.Card: A dbc.Card object with the title, hot menu items, and footer.
    """
    hot_menu_items_card = cards.make_top_n_card(
            title="Hot Menu Items",
            headers=["Item", "Growth"],
            metrics=hot_menu_items,
            footer="vs. Previous Month",
            symbol="%"
        )
    
    return hot_menu_items_card


def build_cold_menu_items_card(cold_menu_items: list[dict]) -> dbc.Card:
    """
    Builds a dbc.Card object with the title, cold menu items, and footer.

    Args:
        cold_menu_items (list[dict]): A list of dictionaries containing the name and decline of the cold menu items.

    Returns:
        dbc.Card: A dbc.Card object with the title, cold menu items, and footer.
    """
    cold_menu_items_card = cards.make_top_n_card(
            title="Cold Menu Items",
            headers=["Item", "Decline"],
            metrics=cold_menu_items,
            footer="vs. Previous Month",
            symbol="%"
        )
    
    return cold_menu_items_card
