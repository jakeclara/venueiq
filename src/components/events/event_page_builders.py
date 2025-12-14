# builds the charts and cards for the events page

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

from src.components.core import cards, charts
from src.components.core.ui_helpers import get_variance_color
from src.utils.constants import THEME_COLORS


#------- charts -------
def build_event_type_pie_chart(events_by_type_df: pd.DataFrame) -> go.Figure:
    """
    Builds a pie chart of total sales grouped by event type.

    Args:
        events_by_type_df (pd.DataFrame): A pandas DataFrame containing the event type and total sales for each event type.

    Returns:
        go.Figure: A pie chart of total sales grouped by event type.
    """
    event_type_pie_chart_colors = {
            "Holiday Party": THEME_COLORS["success"],
            "Corporate": THEME_COLORS["info"],
            "Anniversary": THEME_COLORS["primary"],
            "Wedding": THEME_COLORS["warning"],
            "Other": THEME_COLORS["danger"],
            "Birthday Party": THEME_COLORS["secondary"],
        }

    event_type_pie_chart = charts.make_pie_chart(
        data=events_by_type_df,
        names="event_type",
        values="total_sales",
        color_map=event_type_pie_chart_colors,
        title="",
    )

    return event_type_pie_chart

def build_events_ytd_bar_chart(ytd_summary_metrics: dict) -> go.Figure:
    """
    Builds a plotly.graph_objects.Figure containing a bar chart of year-to-date (YTD) summary metrics.

    Args:
        ytd_summary_metrics (dict): A dictionary containing the YTD summary metrics.

    Returns:
        go.Figure: A plotly.graph_objects.Figure object containing a bar chart of YTD summary metrics.
    """
    events_ytd_bar_chart_colors = {
            "actual": THEME_COLORS["success"],
            "budgeted": THEME_COLORS["info"],
            "prior year": THEME_COLORS["warning"],
        }

    events_ytd_bar_chart = charts.make_grouped_revenue_bar_chart(
        ytd_summary_metrics,
        color_map=events_ytd_bar_chart_colors
    )

    return events_ytd_bar_chart


#------- cards -------
def build_events_monthly_summary_card(
        monthly_revenue_metrics: dict, 
        py_monthly_revenue_metrics: dict
) -> dbc.Card:
    """
    Builds a dbc.Card containing a monthly summary of events revenue.

    Args:
        monthly_revenue_metrics (dict): A dictionary containing the current month's revenue metrics.
        py_monthly_revenue_metrics (dict): A dictionary containing the prior month's revenue metrics.

    Returns:
        dbc.Card: A dbc.Card object containing a monthly summary of events revenue.
    """
    event_monthly_summary_card = cards.make_revenue_by_dept_card(
            title="Monthly Summary",
            current=monthly_revenue_metrics,
            prior=py_monthly_revenue_metrics,
            departments=["Food", "Beverage"],
            current_variance_color=get_variance_color(monthly_revenue_metrics['variance']),
            py_variance_color=get_variance_color(py_monthly_revenue_metrics['variance'])
        )

    return event_monthly_summary_card


def build_num_events_card(
        num_events_monthly: list[dict],
        num_events_ytd: list[dict]
) -> dbc.Card:
    """
    Builds a dbc.Card object containing two metrics of the number of events for a given month and year.

    Args:
        num_events_monthly (list[dict]): A list containing two dictionaries. 
            The first dictionary contains the name "Current" and the number of events for the current year. 
            The second dictionary contains the name "Prior Year" and the number of events for the prior year.
        num_events_ytd (list[dict]): A list containing two dictionaries. 
            The first dictionary contains the name "Current" and the number of events for the current year.
            The second dictionary contains the name "Prior Year" and the number of events for the prior year.

    Returns:
        dbc.Card: A dbc.Card object containing two metrics of the number of events for a given month and year.
    """
    num_events_card_metrics = [
            {
                "name": "Monthly",
                "value": num_events_monthly[0]["num_events"],
                "variance": num_events_monthly[0]["num_events"] - num_events_monthly[1]["num_events"],
            },
            {
                "name": "YTD",
                "value": num_events_ytd[0]["num_events"],
                "variance": num_events_ytd[0]["num_events"] - num_events_ytd[1]["num_events"],
            }
        ]

    num_events_card = cards.make_two_metrics_card(
        title="Number of Events",
        metrics=num_events_card_metrics,
        footer="vs. Prior Year",
        symbol=""
    )

    return num_events_card


def build_num_high_value_events_card(
        num_high_value_events_monthly: list[dict],
        num_high_value_events_ytd: list[dict]
) -> dbc.Card:
    """
    Builds a dbc.Card object containing two metrics of the number of high value events for a given month and year.

    Args:
        num_high_value_events_monthly (list[dict]): A list containing two dictionaries. 
            The first dictionary contains the name "Current" and the number of high value events for the current year. 
            The second dictionary contains the name "Prior Year" and the number of high value events for the prior year.
        num_high_value_events_ytd (list[dict]): A list containing two dictionaries. 
            The first dictionary contains the name "Current" and the number of high value events for the current year.
            The second dictionary contains the name "Prior Year" and the number of high value events for the prior year.

    Returns:
        dbc.Card: A dbc.Card object containing two metrics of the number of high value events for a given month and year.
    """
    num_high_value_events_card_metrics = [
            {
                "name": "Monthly",
                "value": num_high_value_events_monthly[0]["num_events"],
                "variance": num_high_value_events_monthly[0]["num_events"] - num_high_value_events_monthly[1]["num_events"],
            },
            {
                "name": "YTD",
                "value": num_high_value_events_ytd[0]["num_events"],
                "variance": num_high_value_events_ytd[0]["num_events"] - num_high_value_events_ytd[1]["num_events"],
            }
        ]

    num_high_value_events_card = cards.make_two_metrics_card(
        title="High Value Events",
        metrics=num_high_value_events_card_metrics,
        footer="$4,000+ | vs. Prior Year",
        symbol=""
    )

    return num_high_value_events_card


def build_avg_event_sales_card(
        avg_event_sales_monthly: list[dict],
        avg_event_sales_ytd: list[dict]
) -> dbc.Card:
    """
    Builds a dbc.Card object containing two metrics of the average event sales for a given month and year.

    Args:
        avg_event_sales_monthly (list[dict]): A list containing two dictionaries. 
            The first dictionary contains the name "Current" and the average event sales for the current year. 
            The second dictionary contains the name "Prior Year" and the average event sales for the prior year.
        avg_event_sales_ytd (list[dict]): A list containing two dictionaries. 
            The first dictionary contains the name "Current" and the average event sales for the current year.
            The second dictionary contains the name "Prior Year" and the average event sales for the prior year.

    Returns:
        dbc.Card: A dbc.Card object containing two metrics of the average event sales for a given month and year.
    """
    avg_event_sales_card_metrics = [
            {
                "name": "Monthly",
                "value": avg_event_sales_monthly[0]["avg_sales"],
                "variance": avg_event_sales_monthly[0]["avg_sales"] - avg_event_sales_monthly[1]["avg_sales"],
            },
            {
                "name": "YTD",
                "value": avg_event_sales_ytd[0]["avg_sales"],
                "variance": avg_event_sales_ytd[0]["avg_sales"] - avg_event_sales_ytd[1]["avg_sales"],
            }
        ]

    avg_event_sales_card = cards.make_two_metrics_card(
        title="Average Event Sales",
        metrics=avg_event_sales_card_metrics,
        footer="vs. Prior Year",
        symbol="$"
    )

    return avg_event_sales_card


def build_top_five_monthly_events_card(top_five_events_monthly: list[dict]) -> dbc.Card:
    """
    Builds a dbc.Card object containing the top 5 events by total sales for a given month.

    Args:
        top_five_events_monthly (list[dict]): A list of dictionaries containing the name and total sales of each event.

    Returns:
        dbc.Card: A dbc.Card object containing the top 5 events by total sales for a given month.
    """
    top_five_events_monthly_card = cards.make_top_n_card(
            title="Top 5 Events",
            headers=["Event", "Total Sales"],
            metrics=top_five_events_monthly,
            footer="Monthly",
            symbol="$"
        )

    return top_five_events_monthly_card
