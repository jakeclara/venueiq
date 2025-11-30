# data service for event-related operations

from src.models.event import Event
from datetime import datetime
from src.services.helpers import get_total_field

def get_total_event_sales(start_date: datetime, end_date: datetime) -> float:
    """
    Retrieves the total event sales within a given date range.

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.

    Returns:
        float: The total event sales within the given date range.
    """
    return get_total_field(Event, 'total_sales', start_date, end_date, 'event_date')



def get_event_with_highest_sales(start_date: datetime, end_date: datetime, limit: int = 1) -> list[dict]:
    """
    Retrieves a list of events with the highest total sales within a given date range,
    sorted in descending order of total sales.

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.
        limit (int): The number of events to return. Defaults to 1.

    Returns:
        list[dict]: A list of dictionaries containing the event details, including
        client name, event type, total sales, and a computed display name.
    """
    pipeline = [
        {
            '$match': {
                'event_date': {
                    '$gte': start_date,
                    '$lt': end_date
                }
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
        {
            '$project': {
                '_id': 1,
                'client_name': 1,
                'event_type': 1,
                'total_sales': 1,
                'display_name': {'$concat': ['$client_name', ' ', '$event_type']}
            }
        }
    ]
    result = Event.objects.aggregate(*pipeline)
    return list(result)


def get_num_of_events(start_date: datetime, end_date: datetime) -> int:
    """
    Returns the number of events within a given date range.

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.

    Returns:
        int: The number of events within the given date range.
    """
    number_of_events = Event.objects(
        event_date__gte=start_date, 
        event_date__lt=end_date
        ).count()
    return number_of_events


def get_events_above_threshold(start_date: datetime, end_date: datetime, threshold: float) -> list[dict]:
    """
    Returns a list of events that have a total sales above a given threshold
    within a given date range.

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.
        threshold (float): The minimum total sales required for an event to be included.

    Returns:
        list[dict]: A list of dictionaries containing the client name, event type, total sales,
        event date, and a display name for each event.
    """
    pipeline = [
        {
            '$match': {
                'event_date': {
                    '$gte': start_date,
                    '$lt': end_date
                },
                'total_sales': {'$gt': threshold}
            }
        },
        {
            '$sort': {
                'total_sales': -1
            }
        },
        {
            '$project': {
                '_id': 1,
                'client_name': 1,
                'event_type': 1,
                'total_sales': 1,
                'event_date': 1,
                'display_name': {'$concat': ['$client_name', ' ', '$event_type']}
            }
        }
    ]
    result = Event.objects.aggregate(*pipeline)
    return list(result)


def get_average_event_sales(start_date: datetime, end_date: datetime) -> float:
    """
    Computes the average total sales per event within a given date range.

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.

    Returns:
        float: The average total sales per event within the given date range.
    """
    pipeline = [
        {
            '$match': {
                'event_date': {
                    '$gte': start_date,
                    '$lt': end_date
                }
            }
        },
        {
            '$group': {
                '_id': None,
                'average_sales': {'$avg': '$total_sales'}
            }
        }
    ]
    result = Event.objects.aggregate(*pipeline)
    average_sales = next(result, {}).get('average_sales', 0.0)
    return round(average_sales, 2)


def get_event_type_breakdown(start_date: datetime, end_date: datetime) -> list[dict]:
    """
    Computes the total number of events for each event type within a given date range

    Args:
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.

    Returns:
        list[dict]: A list of dictionaries containing the event type and its corresponding count,
            sorted in descending order of count.
    """
    pipeline = [
        {
            '$match': {
                'event_date': {
                    '$gte': start_date,
                    '$lt': end_date
                }
            }
        },
        {
            '$group': {
                '_id': '$event_type',
                'count': {'$sum': 1}
            }
        },
        {
            '$project': {
                'event_type': '$_id',
                'count': 1,
                '_id': 0
            }
        },
        {
            '$sort': {
                'count': -1
            }
        }
    ]
    result = Event.objects.aggregate(*pipeline)
    return list(result)
