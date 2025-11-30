# event budget-related services

from src.models.budget import Budget
from src.services.budget.budget_helpers import get_monthly_budget_total, get_ytd_budget_total

# ------- revenue -------
def get_monthly_budgeted_event_revenue(month: int, year: int) -> float:
    """
    Retrieves the monthly budgeted event revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the monthly budgeted event revenue.
        year (int): The year for which to retrieve the monthly budgeted event revenue.

    Returns:
        float: The monthly budgeted event revenue for the specified month and year.
    """
    return get_monthly_budget_total(Budget, month, year, 'event_sales')


def get_ytd_budgeted_event_revenue(month: int, year: int) -> float:
    """
    Retrieves the year-to-date (YTD) budgeted event revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted event revenue.
        year (int): The year for which to retrieve the YTD budgeted event revenue.

    Returns:
        float: The YTD budgeted event revenue for the specified month and year.
    """
    return get_ytd_budget_total(Budget, month, year, 'event_sales')


# ------- cost -------
def get_monthly_budgeted_event_cost(month: int, year: int) -> float:
    """
    Retrieves the monthly budgeted event cost for a given month and year.

    Args:
        month (int): The month for which to retrieve the monthly budgeted event cost.
        year (int): The year for which to retrieve the monthly budgeted event cost.

    Returns:
        float: The monthly budgeted event cost for the specified month and year.
    """
    return get_monthly_budget_total(Budget, month, year, 'event_cost')


def get_ytd_budgeted_event_cost(month: int, year: int) -> float:
    """
    Retrieves the year-to-date (YTD) budgeted event cost for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted event cost.
        year (int): The year for which to retrieve the YTD budgeted event cost.

    Returns:
        float: The YTD budgeted event cost for the specified month and year.
    """
    return get_ytd_budget_total(Budget, month, year, 'event_cost')
