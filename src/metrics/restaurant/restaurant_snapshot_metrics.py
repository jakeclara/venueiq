# executes aggregates and structures results for restaurant pages callbacks

import pandas as pd

from src.components.core.ui_helpers import get_variance_color
from src.services import restaurant_service
from src.utils import dates
from src.utils.constants import DAYS_OF_WEEK


def get_restaurant_snapshot_page_data( month: int, year: int) -> dict:
    """
    Retrieves aggregated data for the restaurant snapshot page.

    Args:
        month (int): The calendar month (1-12) for which to retrieve the data.
        year (int): The calendar year for which to retrieve the data.

    Returns:
        dict: A dictionary containing data for the restaurant snapshot page.
    """
    return {
        "avg_sales_by_day": get_avg_sales_by_day("monthly", month, year),
        "top_five_menu_items": get_top_n_menu_items("ytd", month, year, 5),
        "hot_menu_items": get_monthly_hot_or_cold_menu_items(month, year, limit=3, hot_items=True),
        "cold_menu_items": get_monthly_hot_or_cold_menu_items(month, year, limit=3, hot_items=False),
        "sales_by_category": get_sales_by_category("ytd", month, year)
    }


def get_avg_sales_by_day(period: str, month: int, year: int) -> list[dict]:
    """
    Retrieves the average total sales per day of the week within a given date range.

    Args:
        period (str): The period for which to retrieve the average total sales per day. Can be "monthly" or "ytd".
        month (int): The calendar month (1-12) for which to retrieve the average total sales per day.
        year (int): The calendar year for which to retrieve the average total sales per day.

    Returns:
        list[dict]: A list of dictionaries containing the day of the week and the average total sales for each day.
    """
    start, end = dates.get_period_range(period, month, year)
    
    data = restaurant_service.get_average_sales_by_day(start, end)

    return [
        {
            "day_of_week": DAYS_OF_WEEK[day["day_of_week"]],
            "average_sales": day["average_sales"],
        }
        for day in data
    ]


def get_sales_by_category(period: str, month: int, year: int) -> dict:
    """
    Retrieves the total restaurant sales grouped by category within a given date range.

    Args:
        period (str): The period for which to retrieve the total restaurant sales grouped by category. Can be "monthly" or "ytd".
        month (int): The calendar month (1-12) for which to retrieve the total restaurant sales grouped by category.
        year (int): The calendar year for which to retrieve the total restaurant sales grouped by category.

    Returns:
        dict: A pandas DataFrame containing the category and total sales for each category.
    """
    start, end = dates.get_period_range(period, month, year)
    sales_by_category = restaurant_service.get_restaurant_sales_by_category(start, end)
    df = pd.DataFrame(sales_by_category)
    df = df.rename(columns={"_id": "Category", "total_sales": "Total Sales"})
    return df


def get_top_n_menu_items(period: str, month: int, year: int, n: int) -> list[dict]:
    """
    Retrieves the top n selling menu items within a given date range.

    Args:
        period (str): The period for which to retrieve the top n selling menu items. Can be "monthly" or "ytd".
        month (int): The calendar month (1-12) for which to retrieve the top n selling menu items.
        year (int): The calendar year for which to retrieve the top n selling menu items.
        n (int): The number of top selling menu items to retrieve.

    Returns:
        list[dict]: A list of dictionaries containing the name and total sales of the top n selling menu items.
    """
    start, end = dates.get_period_range(period, month, year)
    top_menu_items = restaurant_service.get_top_selling_menu_items(start, end, n)
    return [
        {
            "name": item["name"],
            "value": item["total_sales"]
        } for item in top_menu_items
    ]


def get_monthly_hot_or_cold_menu_items(month: int, year: int, limit: int, hot_items: bool = True) -> list[dict]:
    """
    Retrieves the top n selling menu items that have increased or decreased in sales
    compared to the previous month.

    Args:
        month (int): The calendar month (1-12) for which to retrieve the top n selling menu items.
        year (int): The calendar year for which to retrieve the top n selling menu items.
        limit (int): The number of top selling menu items to retrieve.
        hot_items (bool): If True, returns the top n selling menu items that have increased in sales compared to the previous month.
            If False, returns the top n selling menu items that have decreased in sales compared to the previous month.

    Returns:
        list[dict]: A list of dictionaries containing the name, percent change, and color of the top n selling menu items
    """
    current_start, current_end = dates.get_period_range("monthly", month, year)

    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year

    prior_start, prior_end = dates.get_period_range("monthly", prev_month, prev_year)

    sort_order = not hot_items

    hot_menu_items = restaurant_service.get_hot_or_cold_menu_items(
        current_start,
        current_end,
        prior_start,
        prior_end,
        limit,
        sort_by_ascending=sort_order
    )

    return [
        {
            "name": item["name"],
            "value": item["percent_change"],
            "color": get_variance_color(item["percent_change"])
        } for item in hot_menu_items
    ]
