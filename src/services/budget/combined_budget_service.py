# combined budget-related services

from src.models.budget import Budget
from src.services.budget.budget_helpers import get_monthly_budget_total, get_ytd_budget_total

#-------- full annual budget -------
def get_annual_budget_docs(year: int) -> list:
    """
    Retrieves a list of budget documents for a given year.

    Args:
        year (int): The year for which to retrieve the budget documents.

    Returns:
        list: A list of budget documents for the specified year.
    """
    return list(Budget.objects(year=year).order_by('month'))


# ------- revenue -------
def get_combined_monthly_budgeted_revenue(month: int, year: int) -> float:
    """
    Retrieves the combined monthly budgeted revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the combined monthly budgeted revenue.
        year (int): The year for which to retrieve the combined monthly budgeted revenue.

    Returns:
        float: The combined monthly budgeted revenue for the specified month and year.
    """
    return get_monthly_budget_total(Budget, month, year, 'total_sales')


def get_combined_ytd_budgeted_revenue(month: int, year: int) -> float:
    """
    Retrieves the year-to-date (YTD) budgeted revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted revenue.
        year (int): The year for which to retrieve the YTD budgeted revenue.

    Returns:
        float: The YTD budgeted revenue for the specified month and year.
    """
    return get_ytd_budget_total(Budget, month, year, 'total_sales')


# ------- cost -------
def get_combined_monthly_budgeted_cost(month: int, year: int) -> float:
    """
    Retrieves the combined monthly budgeted cost for a given month and year.

    Args:
        month (int): The month for which to retrieve the combined monthly budgeted cost.
        year (int): The year for which to retrieve the combined monthly budgeted cost.

    Returns:
        float: The combined monthly budgeted cost for the specified month and year.
    """
    return get_monthly_budget_total(Budget, month, year, 'total_cost')


def get_combined_ytd_budgeted_cost(month: int, year: int) -> float:
    """
    Retrieves the year-to-date (YTD) budgeted cost for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted cost.
        year (int): The year for which to retrieve the YTD budgeted cost.

    Returns:
        float: The YTD budgeted cost for the specified month and year.
    """
    return get_ytd_budget_total(Budget, month, year, 'total_cost')


# ------- profit -------
def get_combined_monthly_budgeted_profit(month: int, year: int) -> float:
    """
    Retrieves the combined monthly budgeted profit for a given month and year.

    Args:
        month (int): The month for which to retrieve the combined monthly budgeted profit.
        year (int): The year for which to retrieve the combined monthly budgeted profit.

    Returns:
        float: The combined monthly budgeted profit for the specified month and year.
    """
    return get_monthly_budget_total(Budget, month, year, 'gross_profit')


def get_combined_ytd_budgeted_profit(month: int, year: int) -> float:
    """
    Retrieves the year-to-date (YTD) budgeted profit for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted profit.
        year (int): The year for which to retrieve the YTD budgeted profit.

    Returns:
        float: The YTD budgeted profit for the specified month and year.
    """
    return get_ytd_budget_total(Budget, month, year, 'gross_profit')
