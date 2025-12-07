# executes aggregates and structures results for home page callback

from src.metrics.metrics_helpers import compute_cogs_percentage, compute_total_costs, compute_total_revenue
from src.utils import dates
from src.services import budget, event_service, restaurant_service

def get_combined_monthly_revenue_metrics(month: int, year: int) -> dict:
    """
    Retrieves monthly revenue metrics for the given month and year.

    Args:
        month (int): The calendar month (1-12).
        year (int): The calendar year.

    Returns:
        dict: A dictionary containing the budgeted revenue, restaurant revenue, event revenue, total revenue,
        and variance for the given period.
    """
    start, end = dates.monthly_date_range(month, year)

    budgeted_revenue = budget.combined_budget_service.get_combined_monthly_budgeted_revenue(month, year)
    restaurant_revenue = restaurant_service.get_total_restaurant_sales(start, end)
    events_revenue = event_service.get_total_event_sales(start, end)
    total_revenue = compute_total_revenue(restaurant_revenue, events_revenue)
    variance = total_revenue - budgeted_revenue

    return {
        'month': month,
        'year': year,
        'budgeted_revenue': budgeted_revenue,
        'restaurant_revenue': restaurant_revenue,
        'events_revenue': events_revenue,
        'total_revenue': total_revenue,
        'variance': variance
    }


def get_combined_ytd_revenue_metrics(month: int, year: int) -> dict:
    """
    Retrieves year-to-date (YTD) revenue metrics for the given month and year.

    Args:
        month (int): The calendar month (1-12).
        year (int): The calendar year.

    Returns:
        dict: A dictionary containing the budgeted revenue, restaurant revenue, event revenue, total revenue,
        and variance for the given period.
    """
    start, end = dates.ytd_date_range(month, year)

    budgeted_revenue = budget.combined_budget_service.get_combined_ytd_budgeted_revenue(month, year)
    restaurant_revenue = restaurant_service.get_total_restaurant_sales(start, end)
    budgeted_restaurant_revenue = budget.restaurant_budget_service.get_ytd_budgeted_restaurant_revenue(month, year)
    event_revenue = event_service.get_total_event_sales(start, end)
    budgeted_event_revenue = budget.event_budget_service.get_ytd_budgeted_event_revenue(month, year)
    total_revenue = compute_total_revenue(restaurant_revenue, event_revenue)
    variance = total_revenue - budgeted_revenue

    return {
        'month': month,
        'year': year,
        'budgeted_revenue': budgeted_revenue,
        'restaurant_revenue': restaurant_revenue,
        'budgeted_restaurant_revenue': budgeted_restaurant_revenue,
        'event_revenue': event_revenue,
        'budgeted_event_revenue': budgeted_event_revenue,
        'total_revenue': total_revenue,
        'variance': variance
    }


def get_combined_ytd_cost_metrics(month: int, year: int) -> dict:
    """
    Retrieves year-to-date (YTD) cost metrics for the given month and year.

    Args:
        month (int): The calendar month (1-12).
        year (int): The calendar year.

    Returns:
        dict: A dictionary containing the restaurant costs, event costs, actual total costs,
        budgeted restaurant costs, budgeted event costs, and budgeted total costs for the given period.
    """
    start, end = dates.ytd_date_range(month, year)

    restaurant_costs = restaurant_service.get_total_restaurant_costs(start, end)
    event_costs = event_service.get_total_event_costs(start, end)
    actual_total_costs = compute_total_costs(restaurant_costs, event_costs)
    budgeted_restaurant_costs = budget.restaurant_budget_service.get_ytd_budgeted_restaurant_cost(month, year)
    budgeted_event_costs = budget.event_budget_service.get_ytd_budgeted_event_cost(month, year)
    budgeted_total_costs = compute_total_costs(budgeted_restaurant_costs, budgeted_event_costs)

    return {
        'month': month,
        'year': year,
        'restaurant_costs': restaurant_costs,
        'event_costs': event_costs,
        'actual_total_costs': actual_total_costs,
        'budgeted_restaurant_costs': budgeted_restaurant_costs,
        'budgeted_event_costs': budgeted_event_costs,
        'budgeted_total_costs': budgeted_total_costs
    }


def compute_cogs_pct_metrics(revenue_metrics: dict, cost_metrics: dict) -> dict:
    """
    Computes the cost of goods sold (COGS) as a percentage
    
    Args:
        revenue_metrics (dict): A dictionary containing the total revenue for restaurant and event sales.
        cost_metrics (dict): A dictionary containing the total cost for restaurant and event sales.

    Returns:
        dict: A dictionary containing the computed COGS percentages for restaurant and event sales.
    """
    restaurant_actual_cogs_pct = compute_cogs_percentage(
        cost_metrics['restaurant_costs'],
        revenue_metrics['restaurant_revenue']
    )
    restaurant_budgeted_cogs_pct = compute_cogs_percentage(
        cost_metrics['budgeted_restaurant_costs'],
        revenue_metrics['budgeted_restaurant_revenue']
    )
    event_actual_cogs_pct = compute_cogs_percentage(
        cost_metrics['event_costs'],
        revenue_metrics['event_revenue']
    )
    event_budgeted_cogs_pct = compute_cogs_percentage(
        cost_metrics['budgeted_event_costs'],
        revenue_metrics['budgeted_event_revenue']
    )

    return {
        'restaurant_actual_cogs_pct': restaurant_actual_cogs_pct,
        'restaurant_budgeted_cogs_pct': restaurant_budgeted_cogs_pct,
        'event_actual_cogs_pct': event_actual_cogs_pct,
        'event_budgeted_cogs_pct': event_budgeted_cogs_pct
    }


def compute_gross_profit(actual_revenue : float,
                         actual_costs: float,
                         budgeted_revenue: float,
                         budgeted_costs: float
) -> dict:
    """
    Computes the gross profit from passing actual and budgeted revenue and costs values

    Args:
        actual_revenue (float): The actual revenue.
        actual_costs (float): The actual costs.
        budgeted_revenue (float): The budgeted revenue.
        budgeted_costs (float): The budgeted costs.

    Returns:
        dict: A dictionary containing the computed actual and budgeted gross profit values.
    """
    return {
        "actual": actual_revenue - actual_costs,
        "budgeted": budgeted_revenue - budgeted_costs
    }


def get_top_menu_item(period: str, month: int, year: int) -> dict:
    """
    Retrieves the top selling menu item for a given period (monthly or ytd).

    Args:
        period (str): The period for which to retrieve the top selling menu item. Can be "monthly" or "ytd". 
        month (int): The calendar month (1-12) for which to retrieve the top selling menu item.
        year (int): The calendar year for which to retrieve the top selling menu item.

    Returns:
        dict: A dictionary containing the name and total sales of the top selling menu item, or None if no items are found.
    """
    start, end = dates.get_period_range(period, month, year)
    items = restaurant_service.get_top_selling_menu_items(start, end, limit=1)
    if items:
        item = items[0]
        return {"name": item["name"], "total_sales": item["total_sales"]}
    return None


def get_top_event(period: str, month: int, year: int) -> dict:
    """
    Retrieves the top selling event for a given period (monthly or ytd).

    Args:
        period (str): The period for which to retrieve the top selling event. Can be "monthly" or "ytd". 
        month (int): The calendar month (1-12) for which to retrieve the top selling event.
        year (int): The calendar year for which to retrieve the top selling event.

    Returns:
        dict: A dictionary containing the name and total sales of the top selling event, or None if no events are found.
    """
    start, end = dates.get_period_range(period, month, year)
    events = event_service.get_event_with_highest_sales(start, end, limit=1)
    if events:
        event = events[0]
        return {"name": event["display_name"], "total_sales": event["total_sales"]}
    return None