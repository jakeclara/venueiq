# contains helper functions for metrics operations

from src.utils.constants import THEME_COLORS

def format_metric(value: float, symbol: str="$") -> str:
    """
    Format a given value with a symbol.
    
    Args:
        value (float): The value to be formatted.
        symbol (str): The symbol to be used for formatting. Defaults to "$".
    
    Returns:
        str: The formatted value as a string.
    """
    if symbol == "$":
        return f"${value:,.0f}"
    elif symbol == "%":
        return f"{value:,.2f}%"

    return f"{value:,.0f}"


def compute_cogs_percentage(total_cost: float, total_sales: float) -> float:
    """
    Computes the cost of goods sold (COGS) as a percentage from passing total cost and sales values

    Args:
        total_cost (float): The total cost of goods.
        total_sales (float): The total sales of goods.

    Returns:
        float: The COGS as a percentage, rounded to 2 decimal places.

    Notes:
        If total_sales is 0.0, the function returns 0.0 as the COGS percentage.
    """
    return round((total_cost / total_sales) * 100, 2) if total_sales > 0 else 0.0


def compute_total_revenue(restaurant_sales: float, event_sales: float) -> float:
    """
    Computes the total revenue from passing restaurant and event sales values

    Args:
        restaurant_sales (float): The total sales of restaurant.
        event_sales (float): The total sales of events.

    Returns:
        float: The total revenue from restaurant and event sales, rounded to 2 decimal places.
    """
    return restaurant_sales + event_sales


def compute_total_costs(restaurant_cost: float, event_cost: float) -> float:
    """
    Computes the total cost from passing restaurant and event cost values

    Args:
        restaurant_cost (float): The total cost of restaurant.
        event_cost (float): The total cost of events.

    Returns:
        float: The total cost from restaurant and event costs, rounded to 2 decimal places.
    """
    return restaurant_cost + event_cost