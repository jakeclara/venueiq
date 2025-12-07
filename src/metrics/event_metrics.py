# executes aggregates and structures results for banquet page callback

from src.metrics.metrics_helpers import compute_total_revenue
from src.services import budget, event_service
from src.utils import dates

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
    total_revenue = compute_total_revenue(food_revenue, beverage_revenue)
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


def get_events_ytd_revenue_metrics(month: int, year: int) -> dict:
    """
    Retrieves year-to-date (YTD) revenue metrics for events.

    Args:
        month (int): The month for which to retrieve the YTD revenue metrics.
        year (int): The year for which to retrieve the YTD revenue metrics

    Returns:
        dict: A dictionary containing the current year's and previous year's food revenue, beverage revenue,
        total revenue, and budgeted total revenue for the given period
    """
    current_start, current_end = dates.ytd_date_range(month, year)
    py_start, py_end = dates.ytd_date_range(month, year - 1)

    actual_food_revenue = event_service.get_total_event_food_sales(current_start, current_end)
    py_food_revenue = event_service.get_total_event_food_sales(py_start, py_end)

    actual_bev_revenue = event_service.get_total_event_bev_sales(current_start, current_end)
    py_bev_revenue = event_service.get_total_event_bev_sales(py_start, py_end)

    actual_total_revenue = compute_total_revenue(actual_food_revenue, actual_bev_revenue)
    budgeted_total_revenue = budget.event_budget_service.get_ytd_budgeted_event_revenue(month, year)
    py_total_revenue = compute_total_revenue(py_food_revenue, py_bev_revenue)

    return {
        "food": {
            "actual": actual_food_revenue,
            "py": py_food_revenue
        },
        "beverage": {
            "actual": actual_bev_revenue,
            "py": py_bev_revenue
        },
        "total": {
            "actual": actual_total_revenue,
            "budgeted": budgeted_total_revenue,
            "py": py_total_revenue
        }
    }


def compute_num_events(period: str, year: int, month: int) -> list[dict]:
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


