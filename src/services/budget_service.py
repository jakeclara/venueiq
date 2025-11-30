# data service for budget-related operations
from datetime import datetime
from src.models.budget import Budget

from src.services.db_service import init_db
from dotenv import load_dotenv

load_dotenv(".env")

# combined functions
def get_monthly_budgeted_revenue(month: int, year: int) -> float:
    """
    Computes the budgeted revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the budgeted revenue.
        year (int): The year for which to retrieve the budgeted revenue.

    Returns:
        float: The monthly budgeted revenue for the specified month and year.
    """
    budget_doc = Budget.objects(month=month, year=year).first()
    if budget_doc:
        return budget_doc.total_sales
    return 0.0


def get_ytd_budgeted_revenue(month: int, year: int) -> float:
    """
    Computes the year-to-date (YTD) budgeted revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted revenue.
        year (int): The year for which to retrieve the YTD budgeted revenue.

    Returns:
        float: The YTD budgeted revenue for the specified month and year.
    """
    pipeline = [
        {
            '$match': {
                'year': year,
                'month': {'$lte': month}
            }
        },
        {
            '$group': {
                '_id': None,
                'total_sales': {'$sum': '$total_sales'}
            }
        }
    ]
    result = Budget.objects.aggregate(*pipeline)
    budgeted_revenue = next(result, {}).get('total_sales', 0.0)
    return budgeted_revenue


# event functions
def get_monthly_budgeted_event_revenue(month: int, year: int) -> float:
    """
    Computes the budgeted event revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the budgeted event revenue.
        year (int): The year for which to retrieve the budgeted event revenue.

    Returns:
        float: The monthly budgeted event revenue for the specified month and year.
    """
    budget_doc = Budget.objects(month=month, year=year).first()
    if budget_doc:
        return budget_doc.event_sales
    return 0.0


def get_ytd_budgeted_event_revenue(month: int, year: int) -> float:
    """
    Computes the YTD budgeted event revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted event revenue.
        year (int): The year for which to retrieve the YTD budgeted event revenue.

    Returns:
        float: The YTD budgeted event revenue for the specified month and year.
    """
    pipeline = [
        {
            '$match': {
                'year': year,
                'month': {'$lte': month}
            }
        },
        {
            '$group': {
                '_id': None,
                'event_sales': {'$sum': '$event_sales'}
            }
        }
    ]
    result = Budget.objects.aggregate(*pipeline)
    budgeted_revenue = next(result, {}).get('event_sales', 0.0)
    return budgeted_revenue


# restaurant functions
def get_monthly_budgeted_restaurant_revenue(month: int, year: int) -> dict:
    """
    Retrieves the budgeted restaurant revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the budgeted restaurant revenue.
        year (int): The year for which to retrieve the budgeted restaurant revenue.

    Returns:
        dict: A dictionary containing the budgeted food and beverage sales for the specified month and year.
    """
    budget_doc = Budget.objects(month=month, year=year).first()
    if budget_doc:
        return {
            'food_sales': budget_doc.food_sales,
            'bev_sales': budget_doc.bev_sales
        }
    return {'food_sales': 0.0, 'bev_sales': 0.0}


def get_ytd_budgeted_restaurant_revenue(month: int, year: int) -> float:
    """
    Retrieves the year-to-date (YTD) budgeted restaurant revenue for a given month and year.

    Args:
        month (int): The month for which to retrieve the YTD budgeted restaurant revenue.
        year (int): The year for which to retrieve the YTD budgeted restaurant revenue.

    Returns:
        float: The YTD budgeted restaurant revenue for the specified month and year.
        This value is computed as the sum of food and beverage sales.
    """
    pipeline = [
        {
            '$match': {
                'year': year,
                'month': {'$lte': month}
            }
        },
        {
            '$group': {
                '_id': None,
                'food_sales': {'$sum': '$food_sales'},
                'bev_sales': {'$sum': '$bev_sales'},
                'restaurant_sales': {'$sum': {'$add': ['$food_sales', '$bev_sales']}}
            }
        }
    ]
    result = Budget.objects.aggregate(*pipeline)
    budgeted_revenue = next(result, {'food_sales': 0.0, 'bev_sales': 0.0, 'restaurant_sales': 0.0})
    return budgeted_revenue


if __name__ == "__main__":
    if init_db():
        print(get_monthly_budgeted_revenue(4, 2024))
        print(get_ytd_budgeted_revenue(4, 2024))
        print(get_monthly_budgeted_event_revenue(4, 2024))
        print(get_ytd_budgeted_event_revenue(4, 2024))
        budgeted = get_monthly_budgeted_restaurant_revenue(4, 2024)
        print(f"  Food Sales: ${budgeted['food_sales']:,.2f}")
        print(f"  Beverage Sales: ${budgeted['bev_sales']:,.2f}")
        revenue = get_ytd_budgeted_restaurant_revenue(4, 2024)
        print(f"Restaurant Sales: ${revenue['restaurant_sales']:.2f}")
    else:
        print("DB connection failed.")