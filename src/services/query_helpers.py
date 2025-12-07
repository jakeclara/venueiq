# helper functions for services

from datetime import datetime
from typing import Any, Dict, Optional, Type
from xml.dom.minidom import Document

def get_total_field(
    model: Type[Document],
    field: str, 
    start_date: datetime, 
    end_date: datetime,
    date_field_title: str,
    extra_filter: Optional[Dict[str, Any]] = None
) -> float:
    """
    Retrieves the total value of a given field in a model within a specified date range.

    Args:
        model (Type[Document]): The model to query.
        field (str): The field to sum over.
        start_date (datetime): The start date of the date range.
        end_date (datetime): The end date of the date range.
        date_field_title (str): The title of the field that contains the dates.
        extra_filter (Optional[Dict[str, Any]], optional): Additional filter conditions to apply to the query.

    Returns:
        float: The total value of the given field within the specified date range.
    """
    # if extra_filter is provided, use it as the starting point
    # otherwise, create an empty match condition.
    if extra_filter:
        match = extra_filter.copy()
    else:
        match = {}

    # add the date range condition to the match condition
    match[date_field_title] = {
        '$gte': start_date,
        '$lt': end_date
    }

    # define the aggregation pipeline to sum over the given field
    pipeline = [
        {'$match': match},
        {'$group': {
            '_id': None,
            'total': {'$sum': f'${field}'}
        }}
    ]

    # execute the aggregation and return the result
    result = model.objects.aggregate(*pipeline)
    return next(result, {}).get('total', 0.0)