from datetime import date
import random
from src.models.budget import Budget
from src.models.event import Event
from src.models.restaurant_sale import RestaurantSale
from src.seeds import seed_constants as sc


def apply_variance(base: float, min_pct: float, max_pct: float) -> float:
    """
    Applies a random percentage variance to a base value.

    Args:
        base (float): The original numeric value.
        min_pct (float): The minimum percentage multiplier.
        max_pct (float): The maximum percentage multiplier.

    Returns:
        float: The adjusted value after applying a random variance.
    """
    return round(base * random.uniform(min_pct, max_pct), 2)


def date_range(year: int, month: int) -> tuple[date, date]:
    """
    Generates the start and end dates for a given year and month.

    Args:
        year (int): The calendar year.
        month (int): The calendar month (1-12).

    Returns:
        tuple[date, date]: A tuple containing the first day of the month
        and the first day of the following month.
    """
    start = date(year, month, 1)
    if month == 12:
        end = date(year + 1, 1, 1)
    else:
        end = date(year, month + 1, 1)
    return start, end


def get_restaurant_data(year: int, month: int) -> list:
    """
    Aggregates restaurant sales and cost totals grouped by category for a given month.

    Args:
        year (int): The calendar year.
        month (int): The calendar month (1-12).

    Returns:
        list: A list of aggregation results, where each item contains the
        category, total sales, and total cost for that category.
    """
    start_date, end_date = date_range(year, month)

    restaurant_data = RestaurantSale.objects(
        sales_date__gte=start_date,
        sales_date__lt=end_date)
    
    restaurant_pipeline = [
        {
            "$group": {
                "_id": "$category",
                "total_sales": {"$sum": "$total_sales"},
                "total_cost": {"$sum": "$total_cost"}
            }
        }
    ]

    return list(restaurant_data.aggregate(*restaurant_pipeline))


def get_event_data(year: int, month: int) -> list:
    """
    Aggregates total event sales and cost for a given month.

    Args:
        year (int): The calendar year.
        month (int): The calendar month (1-12).

    Returns:
        list: A list containing a single aggregation result with
        total sales and total cost for all events in the month.
    """
    start_date, end_date = date_range(year, month)

    event_data = Event.objects(
        event_date__gte=start_date,
        event_date__lt=end_date
    )

    event_pipeline = [
        {
            "$group": {
                "_id": None,
                "total_sales": {"$sum": "$total_sales"},
                "total_cost": {"$sum": "$total_cost"}
            }
        }
    ]

    return list(event_data.aggregate(*event_pipeline))


def make_budget(year: int, month: int) -> Budget:
    """
    Generates a budget for a given month by aggregating restaurant and event data
    and applying variance adjustments to sales and cost figures.

    Args:
        year (int): The calendar year.
        month (int): The calendar month (1-12).

    Returns:
        Budget: A Budget document containing adjusted sales and cost values
        for food, beverage, and event operations.
    """
    # initialize totals
    food_sales = 0
    food_cost = 0
    bev_sales = 0
    bev_cost = 0
    event_sales = 0
    event_cost = 0

    # fetch aggregated restaurant data
    restaurant_results = get_restaurant_data(year, month)

    # map categories into local variables
    for result in restaurant_results:
        if result["_id"] == "Food":
            food_sales = result["total_sales"]
            food_cost = result["total_cost"]
        elif result["_id"] == "Beverage":
            bev_sales = result["total_sales"]
            bev_cost = result["total_cost"]
    
    # fetch aggregated event data
    event_results = get_event_data(year, month)

    # map into local variables
    for result in event_results:
        event_sales = result["total_sales"]
        event_cost = result["total_cost"]
    
    # apply random variance to sales numbers
    adjusted_food_sales = apply_variance(food_sales, sc.MIN_SALES_VARIANCE, sc.MAX_SALES_VARIANCE)
    adjusted_bev_sales = apply_variance(bev_sales, sc.MIN_SALES_VARIANCE, sc.MAX_SALES_VARIANCE)
    adjusted_event_sales = apply_variance(event_sales, sc.MIN_SALES_VARIANCE, sc.MAX_SALES_VARIANCE)

    # apply random variance to cost numbers
    adjusted_food_cost = apply_variance(food_cost, sc.MIN_COST_VARIANCE, sc.MAX_COST_VARIANCE)
    adjusted_bev_cost = apply_variance(bev_cost, sc.MIN_COST_VARIANCE, sc.MAX_COST_VARIANCE)
    adjusted_event_cost = apply_variance(event_cost, sc.MIN_COST_VARIANCE, sc.MAX_COST_VARIANCE)
    
    # create the budget doc
    budget = Budget(
        month=month,
        year=year,
        food_sales=adjusted_food_sales,
        bev_sales=adjusted_bev_sales,
        event_sales=adjusted_event_sales,
        food_cost=adjusted_food_cost,
        bev_cost=adjusted_bev_cost,
        event_cost=adjusted_event_cost
    )

    return budget


def seed_budget() -> None:
    """
    Creates budget records for each month between the configured start
    and end dates.

    Returns:
        None
    """
    # iterate through each year in the configured range
    for year in range(sc.START_DATE.year, sc.END_DATE.year + 1):
        # iterate through each month in the configured range
        for month in range(sc.START_DATE.month, sc.END_DATE.month + 1):
            # make budget and save to collection
            budget = make_budget(year, month)
            budget.save()
            