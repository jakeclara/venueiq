# data service for restaurant-related operations

from src.models.restaurant_sale import RestaurantSale
from src.services.query_helpers import get_total_field
from datetime import datetime

def get_total_restaurant_sales(start_date: datetime, end_date: datetime) -> float:
    """
    Retrieves the total restaurant sales within a given date range.

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.

    Returns:
        float: The total restaurant sales within the given date range.

    """
    return get_total_field(RestaurantSale, 'total_sales', start_date, end_date, 'sales_date')


def get_total_restaurant_costs(start_date: datetime, end_date: datetime) -> float:
    """
    Retrieves the total restaurant costs within a given date range.

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.

    Returns:
        float: The total restaurant costs within the given date range.
    """
    return get_total_field(RestaurantSale, 'total_cost', start_date, end_date, 'sales_date')


def get_top_selling_menu_items(start_date: datetime, end_date: datetime, limit: int = 1) -> list[dict]:
    """
    Computes the top selling menu items within a given date range

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.
        limit (int): The number of top selling menu items to return. Defaults to 1.

    Returns:
        list[dict]: A list of dictionaries containing the name and total sales of
        the top selling menu items within the given date range.
    """
    pipeline = [
        {
            '$match': {
                'sales_date': {
                    '$gte': start_date,
                    '$lt': end_date
                }
            }
        },
        {
            '$group': {
                '_id': '$item',
                'total_sales': {'$sum': '$total_sales'}
            }
        },
        {
            '$sort': {
                'total_sales': -1
            }
        },
        {
            '$limit': limit
        },
        {"$lookup": {
            "from": "menu_item",
            "localField": "_id",
            "foreignField": "_id",
            "as": "menu_item_details"
        }}, 
        {"$unwind": "$menu_item_details"
        },
        {"$project": {
            "name": "$menu_item_details.name",
            "total_sales": 1
        }}
    ]
    result = RestaurantSale.objects.aggregate(*pipeline)
    return list(result)


def get_restaurant_sales_by_category(start_date: datetime, end_date: datetime) -> list[dict]:
    """
    Retrieves the total restaurant sales grouped by category within a given date range.

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.

    Returns:
        list[dict]: A list of dictionaries containing the category and total sales for each category.
    """
    pipeline = [
        {
            '$match': {
                'sales_date': {
                    '$gte': start_date,
                    '$lt': end_date
                }
            }
        },
        {
            '$group': {
                '_id': '$category',
                'total_sales': {'$sum': '$total_sales'}
            }
        }
    ]
    result = RestaurantSale.objects.aggregate(*pipeline)
    return list(result)


def get_restaurant_cost_by_category(start_date: datetime, end_date: datetime) -> list[dict]:
    """
    Retrieves the total restaurant cost grouped by category within a given date range.

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.

    Returns:
        list[dict]: A list of dictionaries containing the category and total cost for each category.
    """
    pipeline = [
        {
            '$match': {
                'sales_date': {
                    '$gte': start_date,
                    '$lt': end_date
                }
            }
        },
        {
            '$group': {
                '_id': '$category',
                'total_cost': {'$sum': '$total_cost'}
            }
        }
    ]
    result = RestaurantSale.objects.aggregate(*pipeline)
    return list(result)


def get_restaurant_gross_profit(start_date: datetime, end_date: datetime) -> float:
    """
    Retrieves the total gross profit for restaurant sales within a given date range.

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.

    Returns:
        float: The total gross profit for restaurant sales within the given date range.
    """
    total_sales = get_total_field(RestaurantSale, 'total_sales', start_date, end_date, 'sales_date')
    total_cost = get_total_field(RestaurantSale, 'total_cost', start_date, end_date, 'sales_date')
    gross_profit = total_sales - total_cost
    return gross_profit


def get_hot_or_cold_menu_items(
    current_start: datetime, 
    current_end: datetime, 
    previous_start: datetime, 
    previous_end: datetime, 
    limit: int = 3,
    sort_by_ascending: bool = False
)-> list[dict]:
    """
    Retrieves a list of menu items that are currently hot (or cold) compared to the previous time period.

    The "hotness" or "coldness" of a menu item is determined by the difference in total sales between the current and previous time periods.

    The menu items are sorted by the difference in total sales in ascending or descending order.

    Args:
        current_start (datetime): The start date of the current time period.
        current_end (datetime): The end date of the current time period.
        previous_start (datetime): The start date of the previous time period.
        previous_end (datetime): The end date of the previous time period.
        limit (int): The number of menu items to return.
        sort_by_ascending (bool): If True, the menu items are sorted in ascending order by difference in total sales. If False, the menu items are sorted in descending order.

    Returns:
        list[dict]: A list of dictionaries containing the name, current total sales, previous total sales, and difference in total sales for each menu item.
    """
    sort_order = 1 if sort_by_ascending else -1
    
    pipeline = [
        {
            # match all restaurant sales that fall within the current time period
            '$match': {
                'sales_date': {
                    '$gte': current_start,
                    '$lt': current_end
                }
            }
        },
        {
            # group all restaurant sales by menu item
            '$group': {
                '_id': '$item',
                'current_total': {'$sum': '$total_sales'}
            }
        },
        {
            # perform a lookup to get the total sales for each menu item in the previous time period
            '$lookup': {
                'from': 'restaurant_sale',
                'let': {'item_id': '$_id'},
                'pipeline': [
                    {
                        # match all restaurant sales that fall within the previous time period
                        '$match': {
                            'sales_date': {
                                '$gte': previous_start,
                                '$lt': previous_end
                            },
                            # make sure we only look at the same menu item
                            '$expr': {'$eq': ['$item', '$$item_id']}
                        }
                    },
                    {
                        # group all restaurant sales by menu item and calculate the total sales for each menu item
                        '$group': {
                            '_id': None,
                            'previous_total': {'$sum': '$total_sales'}
                        }
                    }
                ],
                'as': 'previous_sales'

            }
        },
        {
            # project the fields we need
            '$project': {
                'current_total': 1,
                'previous_total': {
                    # if the lookup returned no results, set previous_total to 0
                    '$ifNull': [
                        {'$arrayElemAt': ['$previous_sales.previous_total', 0]},
                        0
                    ]
                },
                # calculate the difference in total sales between the current and previous time periods
                'difference': {
                    '$subtract': [
                        '$current_total',
                        {
                            '$ifNull': [
                                {'$arrayElemAt': ['$previous_sales.previous_total', 0]},
                                0
                            ]
                        }
                    ]
                }
            }
        },
        {
            # sort the results by the difference in total sales
            '$sort': {
                'difference': sort_order
            }
        },
        {
            # limit the number of results to the specified number
            '$limit': limit
        },
        {
            # perform a lookup to get the menu item details
            '$lookup': {
                'from': 'menu_item',
                'localField': '_id',
                'foreignField': '_id',
                'as': 'menu_item_details'
            }
        },
        {
            # unwind the menu item details
            '$unwind': '$menu_item_details'
        },
        {
            # project the fields we need
            '$project': {
                'name': '$menu_item_details.name',
                'current_total': 1,
                'previous_total': 1,
                'difference': 1,
                # calculate the percent increase or decrease in total sales
                'percent_change': {
                    '$cond': [
                        {'$eq': ['$previous_total', 0]},
                        None,
                        {
                            '$round': [
                                {
                                    '$multiply': [
                                        {
                                            '$divide': ['$difference', '$previous_total']
                                        },
                                        100
                                    ]
                                },
                                1
                            ]
                        }
                    ]
                }
            }
        }
    ]
    result = RestaurantSale.objects.aggregate(*pipeline)
    return list(result)


def get_average_sales_by_day(start_date: datetime, end_date: datetime) -> list[dict]:
    """
    Retrieves the average total sales per day of the week within a given date range.

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.

    Returns:
        list[dict]: A list of dictionaries containing the day of the week and the average total sales for that day.
    """
    pipeline = [
        {
            '$match': {
                'sales_date': {
                    '$gte': start_date,
                    '$lt': end_date
                }
            }
        },
        {
            "$group": {
                "_id": "$sales_date",
                "daily_total": {"$sum": "$total_sales"}
            }
        },
        {
            "$project": {
                "daily_total": 1,
                "day_of_week": {"$dayOfWeek": "$_id"}
            }
        },
        {
            "$group": {
                "_id": "$day_of_week",
                "average_sales": {"$avg": "$daily_total"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "day_of_week": "$_id",
                "average_sales": 1
            }
        },

        { "$sort": {"day_of_week": 1} }
    ]
    result = RestaurantSale.objects.aggregate(*pipeline)
    return list(result)
