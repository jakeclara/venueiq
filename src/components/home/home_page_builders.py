# builds the charts and cards for the home page

import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

from src.components.core import cards, charts
from src.components.core.ui_helpers import get_donut_chart_colors, get_variance_color
from src.utils.constants import THEME_COLORS

# ------- charts -------
def build_donut_chart(monthly_revenue_metrics: dict) -> go.Figure:
    """
    Builds a donut chart based on the given monthly revenue metrics.

    Parameters:
    monthly_revenue_metrics (dict): A dictionary containing the total revenue, budgeted revenue,
        and variance for the month.

    Returns:
    go.Figure: A donut chart figure object.
    """
    donut_colors = get_donut_chart_colors(
            monthly_revenue_metrics['total_revenue'],
            monthly_revenue_metrics['budgeted_revenue']
        )

    donut_chart = charts.make_budget_donut(
        actual=monthly_revenue_metrics['total_revenue'],
        budgeted=monthly_revenue_metrics['budgeted_revenue'],
        color_map=donut_colors
    )

    return donut_chart


def build_revenue_breakdown_pie_chart(ytd_revenue_metrics: dict) -> go.Figure:
    """
    Builds a plotly.graph_objects.Figure containing a pie chart of year-to-date (YTD) revenue breakdown metrics.

    Parameters:
        ytd_revenue_metrics (dict): A dictionary containing the YTD revenue breakdown metrics.

    Returns:
        go.Figure: A plotly.graph_objects.Figure object containing a pie chart of YTD revenue breakdown metrics.
    """
    revenue_breakdown_pie_chart_colors = {
            "Restaurant": THEME_COLORS["info"],
            "Events": THEME_COLORS["danger"],
        }

    revenue_breakdown_df = pd.DataFrame([
        {
            "name": "Restaurant",
            "value": ytd_revenue_metrics['restaurant_revenue'],

        },
        {
            "name": "Events",
            "value": ytd_revenue_metrics['event_revenue'],
        }
    ])

    revenue_breakdown_pie = charts.make_pie_chart(
        data=revenue_breakdown_df,
        names="name",
        values="value",
        color_map=revenue_breakdown_pie_chart_colors
    )

    return revenue_breakdown_pie


# ------- cards -------
def build_monthly_summary_card(
        monthly_revenue_metrics: dict,
        py_monthly_revenue_metrics: dict
) -> dbc.Card:
    """
    Builds a dbc.Card object containing a monthly summary of revenue by department.

    Parameters:
        monthly_revenue_metrics (dict): A dictionary containing the total revenue, budgeted revenue,
            and variance for the month.
        py_monthly_revenue_metrics (dict): A dictionary containing the total revenue, budgeted revenue,
            and variance for the prior month.

    Returns:
        dbc.Card: A dbc.Card object containing a monthly summary of revenue by department.
    """
    monthly_summary_card = cards.make_revenue_by_dept_card(
            title="Monthly Summary",
            current=monthly_revenue_metrics,
            prior=py_monthly_revenue_metrics,
            departments=["Restaurant", "Events"],
            current_variance_color=get_variance_color(monthly_revenue_metrics['variance']),
            py_variance_color=get_variance_color(py_monthly_revenue_metrics['variance'])
        )

    return monthly_summary_card


def build_ytd_revenue_card(
          ytd_revenue_metrics: dict,
          py_ytd_revenue_metrics: dict
) -> dbc.Card:
    """
    Builds a dbc.Card object containing year-to-date (YTD) revenue metrics.

    Parameters:
        ytd_revenue_metrics (dict): A dictionary containing the total revenue, budgeted revenue,
            and variance for the YTD period.
        py_ytd_revenue_metrics (dict): A dictionary containing the total revenue, budgeted revenue,
            and variance for the prior YTD period.

    Returns:
        dbc.Card: A dbc.Card object containing YTD revenue metrics.
    """
    ytd_revenue_card_metrics = [
            {
                "name": "Actual",
                "value": ytd_revenue_metrics['total_revenue'],
                "budget": ytd_revenue_metrics['budgeted_revenue'],
                "variance": ytd_revenue_metrics['variance'],
            },
            {
                "name": "Prior Year",
                "value": py_ytd_revenue_metrics['total_revenue'],
                "budget": py_ytd_revenue_metrics['budgeted_revenue'],
                "variance": py_ytd_revenue_metrics['variance'],
            },
        ]

    ytd_revenue_card = cards.make_two_metrics_card(
        title="YTD Revenue",
        metrics=ytd_revenue_card_metrics,
        footer="vs. Budget",
        symbol="$"
    )

    return ytd_revenue_card


def build_cogs_kpi_card(cogs_pct_metrics: dict) -> dbc.Card:
    """
    Builds a dbc.Card object containing year-to-date (YTD) cost of goods sold (COGS) metrics.

    Parameters:
        cogs_pct_metrics (dict): A dictionary containing the actual and budgeted COGS percentages
            for restaurant and event sales.

    Returns:
        dbc.Card: A dbc.Card object containing YTD COGS metrics.
    """
    cogs_kpi_card_metrics = [
            {
                "name": "Restaurant",
                "value": cogs_pct_metrics['restaurant_actual_cogs_pct'],
                "budget": cogs_pct_metrics['restaurant_budgeted_cogs_pct'],
                "variance": cogs_pct_metrics['restaurant_actual_cogs_pct'] - cogs_pct_metrics['restaurant_budgeted_cogs_pct'],
            },
            {
                "name": "Events",
                "value": cogs_pct_metrics['event_actual_cogs_pct'],
                "budget": cogs_pct_metrics['event_budgeted_cogs_pct'],
                "variance": cogs_pct_metrics['event_actual_cogs_pct'] - cogs_pct_metrics['event_budgeted_cogs_pct'],
            },
        ]

    cogs_kpi_card = cards.make_two_metrics_card(
        title="YTD Cost of Goods Sold",
        metrics=cogs_kpi_card_metrics,
        footer="vs. Budget",
        symbol="%",
    )

    return cogs_kpi_card


def build_profit_card(ytd_gross_profit: float, budgeted_ytd_gross_profit: float) -> dbc.Card:
    """
    Builds a dbc.Card object containing the year-to-date (YTD) gross profit metric.

    Parameters:
        ytd_gross_profit (float): The actual YTD gross profit.
        budgeted_ytd_gross_profit (float): The budgeted YTD gross profit.

    Returns:
        dbc.Card: A dbc.Card object containing the YTD gross profit metric.
    """
    profit_card_metrics = [
            {
                "name": "Actual",
                "value": ytd_gross_profit,
                "budget": budgeted_ytd_gross_profit,
                "variance": ytd_gross_profit - budgeted_ytd_gross_profit,
            },
        ]

    profit_card = cards.make_one_metric_card(
        title="YTD Gross Profit",
        metric=profit_card_metrics[0],
        footer="vs. Budget",
        symbol="$",
    )

    return profit_card


def build_top_menu_item_card(top_menu_item: dict, py_top_menu_item: dict) -> dbc.Card:
    """
    Builds a dbc.Card object containing the top selling menu item metric.

    Parameters:
        top_menu_item (dict): A dictionary containing the name and total sales of the top selling menu item.
        py_top_menu_item (dict): A dictionary containing the name and total sales of the top selling menu item 
            for the prior year.

    Returns:
        dbc.Card: A dbc.Card object containing the top selling menu item metric.
    """
    top_menu_item_metrics = {
                "name": top_menu_item["name"],
                "value": top_menu_item["total_sales"],
                "variance": top_menu_item["total_sales"] - py_top_menu_item["total_sales"],
        }

    top_menu_item_card = cards.make_one_metric_card(
        title="Top Selling Menu Item",
        metric=top_menu_item_metrics,
        footer="YTD vs. Same Item Sales Prior Year",
        symbol="$",
    )

    return top_menu_item_card


def build_top_event_card(top_selling_event: dict, py_top_selling_event: dict) -> dbc.Card:
    """
    Builds a dbc.Card object containing the top selling event metric.

    Parameters:
        top_selling_event (dict): A dictionary containing the name and total sales of the top selling event.
        py_top_selling_event (dict): A dictionary containing the name and total sales of the top selling event
            for the prior year.

    Returns:
        dbc.Card: A dbc.Card object containing the top selling event metric.
    """
    top_event_card_metrics = {
                "name": top_selling_event["name"],
                "value": top_selling_event["total_sales"],
                "variance": top_selling_event["total_sales"] - py_top_selling_event["total_sales"],
        }

    top_event_card = cards.make_one_metric_card(
        title="Top Selling Event",
        metric=top_event_card_metrics,
        footer="YTD vs. Top Selling Event Prior Year",
        symbol="$",
    )

    return top_event_card
