# date-related helper functions

from datetime import datetime

def monthly_date_range(month: int, year: int) -> tuple[datetime, datetime]:
    """
    Generates the start and end dates for a given year and month.

    Args:
        month (int): The calendar month (1-12).
        year (int): The calendar year.

    Returns:
        tuple[datetime, datetime]: A tuple containing the first day of the month
        and the first day of the following month.
    """
    start = datetime(year, month, 1)
    if month == 12:
        end = datetime(year + 1, 1, 1)
    else:
        end = datetime(year, month + 1, 1)
    return start, end


def ytd_date_range(month: int, year: int) -> tuple[datetime, datetime]:
    """
    Generates the start and end dates for year-to-date (YTD) calculations.

    Args:
        month (int): The calendar month (1-12).
        year (int): The calendar year.

    Returns:
        tuple[datetime, datetime]: A tuple containing January 1st of the given year
        and the first day of the following month.
    """
    start = datetime(year, 1, 1)
    if month == 12:
        end = datetime(year + 1, 1, 1)
    else:
        end = datetime(year, month + 1, 1)
    return start, end