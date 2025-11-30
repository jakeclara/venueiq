# budget-related helper functions

from typing import Type
from mongoengine.document import Document

def get_monthly_budget_total(model: Type[Document], month: int, year: int, field: str) -> float:
    """
    Retrieves the total value of a given field in a budget document
    for a given month and year.

    Args:
        model (Type[Document]): The MongoEngine model to query.
        month (int): The month to query (1-12).
        year (int): The year to query.
        field (str): The name of the field to retrieve the total value for.

    Returns:
        float: The total value of the given field in the budget document
        for the specified month and year, or 0.0 if no matching document is found.
    """
    # attempt to retrieve a budget document for the given month and year
    budget_doc = model.objects(month=month, year=year).first()

    # if a budget document is found, retrieve the total value of the given field
    if budget_doc:
        total_value = getattr(budget_doc, field, 0.0)
        return float(total_value)
    # if no matching budget document is found, return 0.0
    return 0.0


def get_ytd_budget_total(model: Type[Document],month: int, year: int, field: str) -> float:
    """
    Retrieves the year-to-date (YTD) total value of a given field in a budget document
    for a given month and year.

    Args:
        model (Type[Document]): The MongoEngine model to query.
        month (int): The month to query (1-12).
        year (int): The year to query.
        field (str): The name of the field to retrieve the total value for.

    Returns:
        float: The YTD total value of the given field in the budget document
        for the specified month and year, or 0.0 if no matching document is found.
    """
    pipeline = [
        {
            # match all budget documents with a year equal to the given year
            # and a month less than or equal to the given month
            '$match': {
                'year': year,
                'month': {'$lte': month}
            }
        },
        {
            # group the results by the given field and sum over it
            '$group': {
                '_id': None,
                'ytd_total': {'$sum': f'${field}'}
            }
        }
    ]

    # execute the aggregation and return the result
    result = model.objects.aggregate(*pipeline)
    ytd_total = next(result, {}).get('ytd_total', 0.0)
    return ytd_total
