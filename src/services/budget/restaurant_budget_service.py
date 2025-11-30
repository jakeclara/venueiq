# restaurant budget-related functions

from src.models.budget import Budget
from src.services.budget.budget_helpers import get_monthly_budget_total, get_ytd_budget_total

# ------- revenue -------
def get_monthly_budgeted_food_revenue(month: int, year: int) -> float:
    """
    Retrieves the monthly budgeted food revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the monthly budgeted food revenue.
        year (int): The year for which to retrieve the monthly budgeted food revenue.

    Returns:
        float: The monthly budgeted food revenue for the specified month and year.
    """
    return get_monthly_budget_total(Budget, month, year, 'food_sales')


def get_ytd_budgeted_food_revenue(month: int, year: int) -> float:
    """
    Retrieves the year-to-date (YTD) budgeted food revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted food revenue.
        year (int): The year for which to retrieve the YTD budgeted food revenue.

    Returns:
        float: The YTD budgeted food revenue for the specified month and year.
    """
    return get_ytd_budget_total(Budget, month, year, 'food_sales')


def get_monthly_budgeted_bev_revenue(month: int, year: int) -> float:
    """
    Retrieves the monthly budgeted beverage revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the monthly budgeted beverage revenue.
        year (int): The year for which to retrieve the monthly budgeted beverage revenue.

    Returns:
        float: The monthly budgeted beverage revenue for the specified month and year.
    """
    return get_monthly_budget_total(Budget, month, year, 'bev_sales')


def get_ytd_budgeted_bev_revenue(month: int, year: int) -> float:
    """
    Retrieves the year-to-date (YTD) budgeted beverage revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted beverage revenue.
        year (int): The year for which to retrieve the YTD budgeted beverage revenue.

    Returns:
        float: The YTD budgeted beverage revenue for the specified month and year.
    """
    return get_ytd_budget_total(Budget, month, year, 'bev_sales')


def get_monthly_budgeted_restaurant_revenue(month: int, year: int) -> float:
    """
    Computes the monthly budgeted restaurant revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the monthly budgeted restaurant revenue.
        year (int): The year for which to retrieve the monthly budgeted restaurant revenue.

    Returns:
        float: The monthly budgeted restaurant revenue for the specified month and year.
    """
    return get_monthly_budgeted_food_revenue(month, year) + get_monthly_budgeted_bev_revenue(month, year)


def get_ytd_budgeted_restaurant_revenue(month: int, year: int) -> float:
    """
    Computes the year-to-date (YTD) budgeted restaurant revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted restaurant revenue.
        year (int): The year for which to retrieve the YTD budgeted restaurant revenue.

    Returns:
        float: The YTD budgeted restaurant revenue for the specified month and year.
    """
    return get_ytd_budgeted_food_revenue(month, year) + get_ytd_budgeted_bev_revenue(month, year)


# ------- cost -------
def get_monthly_budgeted_food_cost(month: int, year: int) -> float:
    """
    Retrieves the monthly budgeted food cost for a given month and year.

    Args:
        month (int): The month for which to retrieve the monthly budgeted food cost.
        year (int): The year for which to retrieve the monthly budgeted food cost.

    Returns:
        float: The monthly budgeted food cost for the specified month and year.
    """
    return get_monthly_budget_total(Budget, month, year, 'food_cost')


def get_ytd_budgeted_food_cost(month: int, year: int) -> float:
    """
    Retrieves the year-to-date (YTD) budgeted food cost for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted food cost.
        year (int): The year for which to retrieve the YTD budgeted food cost.

    Returns:
        float: The YTD budgeted food cost for the specified month and year.
    """
    return get_ytd_budget_total(Budget, month, year, 'food_cost')


def get_monthly_budgeted_bev_cost(month: int, year: int) -> float:
    """
    Retrieves the monthly budgeted beverage cost for a given month and year.

    Args:
        month (int): The month for which to retrieve the monthly budgeted beverage cost.
        year (int): The year for which to retrieve the monthly budgeted beverage cost.

    Returns:
        float: The monthly budgeted beverage cost for the specified month and year.
    """
    return get_monthly_budget_total(Budget, month, year, 'bev_cost')


def get_ytd_budgeted_bev_cost(month: int, year: int) -> float:
    """
    Retrieves the year-to-date (YTD) budgeted beverage cost for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted beverage cost.
        year (int): The year for which to retrieve the YTD budgeted beverage cost.

    Returns:
        float: The YTD budgeted beverage cost for the specified month and year.
    """
    return get_ytd_budget_total(Budget, month, year, 'bev_cost')


def get_monthly_budgeted_restaurant_cost(month: int, year: int) -> float:
    """
    Computes the monthly budgeted restaurant cost for a given month and year.

    Args:
        month (int): The month for which to retrieve the monthly budgeted restaurant cost.
        year (int): The year for which to retrieve the monthly budgeted restaurant cost.

    Returns:
        float: The monthly budgeted restaurant cost for the specified month and year.
    """
    return get_monthly_budgeted_food_cost(month, year) + get_monthly_budgeted_bev_cost(month, year)


def get_ytd_budgeted_restaurant_cost(month: int, year: int) -> float:
    """
    Computes the year-to-date (YTD) budgeted restaurant cost for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted restaurant cost.
        year (int): The year for which to retrieve the YTD budgeted restaurant cost.

    Returns:
        float: The YTD budgeted restaurant cost for the specified month and year.
    """
    return get_ytd_budgeted_food_cost(month, year) + get_ytd_budgeted_bev_cost(month, year)


# ------- profit -------
def get_monthly_budgeted_restaurant_profit(month: int, year: int) -> float:
    """
    Computes the monthly budgeted restaurant profit for a given month and year.

    Args:
        month (int): The month for which to retrieve the monthly budgeted restaurant profit.
        year (int): The year for which to retrieve the monthly budgeted restaurant profit.

    Returns:
        float: The monthly budgeted restaurant profit for the specified month and year.
    """
    return get_monthly_budgeted_restaurant_revenue(month, year) - get_monthly_budgeted_restaurant_cost(month, year)


def get_ytd_budgeted_restaurant_profit(month: int, year: int) -> float:
    """
    Computes the year-to-date (YTD) budgeted restaurant profit for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted restaurant profit.
        year (int): The year for which to retrieve the YTD budgeted restaurant profit.

    Returns:
        float: The YTD budgeted restaurant profit for the specified month and year.
    """
    return get_ytd_budgeted_restaurant_revenue(month, year) - get_ytd_budgeted_restaurant_cost(month, year)
