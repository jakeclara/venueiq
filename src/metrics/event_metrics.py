# executes aggregates and structures results for banquet page callback

import pandas as pd

from src.metrics.metrics_helpers import compute_total, compute_gross_profit
from src.services import budget, event_service
from src.utils import dates

def get_events_page_data(month: int, year: int) -> dict:
    """
    Retrieves a dictionary containing the monthly and year-to-date events metrics for a given month and year.

    Args:
        month (int): The month for which to retrieve the event metrics.
        year (int): The year for which to retrieve the event metrics.

    Returns:
        dict: A dictionary containing the monthly and year-to-date event metrics.
    """
    return {
        "monthly_revenue_metrics": get_events_monthly_revenue_metrics(month, year),
        "py_monthly_revenue_metrics": get_events_monthly_revenue_metrics(month, year - 1),
        "ytd_summary_metrics": get_events_ytd_summary_metrics(month, year),
        "num_events_monthly": compute_num_events("monthly", year, month),
        "num_events_ytd": compute_num_events("ytd", year, month),
        "num_high_value_events_monthly": compute_num_events_above_threshold("monthly", year, month, 4000),
        "num_high_value_events_ytd": compute_num_events_above_threshold("ytd", year, month, 4000),
        "avg_event_sales_monthly": compute_avg_event_sales("monthly", year, month),
        "avg_event_sales_ytd": compute_avg_event_sales("ytd", year, month),
        "top_five_events_monthly": get_top_n_events("monthly", year, month, 5),
        "events_by_type_df": get_events_by_type("ytd", year, month)
    }


def get_events_monthly_revenue_metrics(month: int, year: int) -> dict:
    """
    Retrieves monthly revenue metrics for events.

    Args:
        month (int): The month for which to retrieve the monthly revenue metrics.
        year (int): The year for which to retrieve the monthly revenue metrics.

    Returns:
        dict: A dictionary containing the budgeted revenue, food revenue, beverage revenue,
        total revenue, and variance for the given period.
    """
    start, end = dates.monthly_date_range(month, year)

    budgeted_revenue = budget.event_budget_service.get_monthly_budgeted_event_revenue(month, year)
    food_revenue = event_service.get_total_event_food_sales(start, end)
    beverage_revenue = event_service.get_total_event_bev_sales(start, end)
    total_revenue = compute_total(food_revenue, beverage_revenue)
    variance = total_revenue - budgeted_revenue

    return {
        'month': month,
        'year': year,
        'budgeted_revenue': budgeted_revenue,
        'food_revenue': food_revenue,
        'beverage_revenue': beverage_revenue,
        'total_revenue': total_revenue,
        'variance': variance
    }


def get_events_ytd_summary_metrics(month: int, year: int) -> dict:
    """
    Retrieves year-to-date (YTD) summary metrics for events.

    Args:
        month (int): The month for which to retrieve the YTD summary metrics.
        year (int): The year for which to retrieve the YTD summary metrics.

    Returns:
        dict: A dictionary containing the current year's actual revenue, budgeted revenue, previous year's revenue,
        current year's actual costs, budgeted costs, previous year's costs, current year's actual gross profit,
        budgeted gross profit, and previous year's gross profit.
    """
    current_start, current_end = dates.ytd_date_range(month, year)
    py_start, py_end = dates.ytd_date_range(month, year - 1)

    actual_total_revenue = event_service.get_total_event_sales(current_start, current_end)
    budgeted_total_revenue = budget.event_budget_service.get_ytd_budgeted_event_revenue(month, year)
    py_total_revenue = event_service.get_total_event_sales(py_start, py_end)
    
    actual_total_costs = event_service.get_total_event_costs(current_start, current_end)
    budgeted_total_costs = budget.event_budget_service.get_ytd_budgeted_event_cost(month, year)
    py_total_costs = event_service.get_total_event_costs(py_start, py_end)

    actual_gross_profit = compute_gross_profit(actual_total_revenue, actual_total_costs)
    budgeted_gross_profit = compute_gross_profit(budgeted_total_revenue, budgeted_total_costs)
    py_gross_profit = compute_gross_profit(py_total_revenue, py_total_costs)

    return {
        "revenue": {
            "actual": actual_total_revenue,
            "budgeted": budgeted_total_revenue,
            "prior year": py_total_revenue
        },
        "costs": {
            "actual": actual_total_costs,
            "budgeted": budgeted_total_costs,
            "prior year": py_total_costs
        },
        "gross profit": {
            "actual": actual_gross_profit,
            "budgeted": budgeted_gross_profit,
            "prior year": py_gross_profit
        }
    }


def compute_num_events(period: str, year: int, month: int) -> list[dict]:
    """
    Computes the number of events for a given period (monthly or ytd), year, and month.

    Args:
        period (str): The period for which to compute the number of events. Can be "monthly" or "ytd".
        year (int): The year for which to compute the number of events.
        month (int): The month for which to compute the number of events.

    Returns:
        list[dict]: A list containing two dictionaries. 
        The first dictionary contains the name "Current" and the number of events for the current year.
        The second dictionary contains the name "Prior Year" and the number of events for the prior year.
    """
    current_start, current_end = dates.get_period_range(period, month, year)
    py_start, py_end = dates.get_period_range(period, month, year - 1)
    current = event_service.get_num_events(current_start, current_end)
    prior_year = event_service.get_num_events(py_start, py_end)

    return [
        {
            "name": "Current",
            "num_events": current
        },
        {
            "name": "Prior Year",
            "num_events": prior_year
        }
    ]


def compute_num_events_above_threshold(period: str, year: int, month: int, threshold: float) -> int:
    """
    Computes the number of events with total sales above a given threshold 
    for a given period (monthly or ytd), year, and month.

    Args:
        period (str): The period for which to compute the number of events. Can be "monthly" or "ytd"
        year (int): The year for which to compute the number of events.
        month (int): The month for which to compute the number of events.
        threshold (float): The minimum total sales required for an event to be included in the count.

    Returns:
        list[dict]: A list containing two dictionaries. 
        The first dictionary contains the name "Current" and the number of events for the current year.
        The second dictionary contains the name "Prior Year" and the number of events for the prior year.
    """
    current_start, current_end = dates.get_period_range(period, month, year)
    py_start, py_end = dates.get_period_range(period, month, year - 1)
    current = event_service.get_num_events_above_threshold(current_start, current_end, threshold)
    prior_year = event_service.get_num_events_above_threshold(py_start, py_end, threshold)

    return [
        {
            "name": "Current",
            "num_events": current
        },
        {
            "name": "Prior Year",
            "num_events": prior_year
        }
    ]


def compute_avg_event_sales(period: str, year: int, month: int) -> float:
    """
    Computes the average total sales per event for a given period (monthly or ytd), year, and month.

    Args:
        period (str): The period for which to compute the average total sales per event. Can be "monthly" or "ytd"
        year (int): The year for which to compute the average total sales per event.
        month (int): The month for which to compute the average total sales per event.

    Returns:
        list[dict]: A list containing two dictionaries.
        The first dictionary contains the name "Current" and the average total sales per event for the current year.
        The second dictionary contains the name "Prior Year" and the average total sales per event for the prior year.
    """
    current_start, current_end = dates.get_period_range(period, month, year)
    py_start, py_end = dates.get_period_range(period, month, year - 1)
    current = event_service.get_average_event_sales(current_start, current_end)
    prior_year = event_service.get_average_event_sales(py_start, py_end)

    return [
        {
            "name": "Current",
            "avg_sales": current
        },
        {
            "name": "Prior Year",
            "avg_sales": prior_year
        }
    ]


def get_top_n_events(period: str, year: int, month: int, n: int) -> list[dict]:
    """
    Retrieves the top n events by total sales for a given period (monthly or ytd), year, and month.

    Args:
        period (str): The period for which to retrieve the top n events. Can be "monthly" or "ytd".
        year (int): The year for which to retrieve the top n events.
        month (int): The month for which to retrieve the top n events.
        n (int): The number of events to retrieve.

    Returns:
        list[dict]: A list of dictionaries containing the name and total sales of each event.
    """
    start, end = dates.get_period_range(period, month, year)
    top_n_events = event_service.get_events_with_highest_sales(start, end, limit=n)

    return [
        {
            "name": event["display_name"],
            "value": event["total_sales"]
        } for event in top_n_events
    ]


def get_events_by_type(period: str, year: int, month: int) -> pd.DataFrame:
    """
    Retrieves a pandas DataFrame containing the event type breakdown for a given period (monthly or ytd), year, and month.

    Args:
        period (str): The period for which to retrieve the event type breakdown. Can be "monthly" or "ytd".
        year (int): The year for which to retrieve the event type breakdown.
        month (int): The month for which to retrieve the event type breakdown.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the event type breakdown, with columns for the event type and total sales.
    """
    start, end = dates.get_period_range(period, month, year)
    events_by_type_data = event_service.get_event_type_breakdown(start, end)
    df = pd.DataFrame(events_by_type_data)
    return df
    