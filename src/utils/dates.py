# date-related utility functions

from datetime import datetime
import logging

# create logger
logger = logging.getLogger(__name__)

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


def get_period_range(period: str, month: int, year: int) -> tuple[datetime, datetime]:
    """
    Retrieves the start and end dates for a given period (monthly or ytd).

    Args:
        period (str): The period for which to retrieve the start and end dates. Can be "monthly" or "ytd".
        month (int): The calendar month (1-12) for which to retrieve the start and end dates.
        year (int): The calendar year for which to retrieve the start and end dates.

    Returns:
        tuple[datetime, datetime]: A tuple containing the start and end dates for the given period, month and year.
        Defaults to monthly if period is not "monthly" or "ytd".
    """
    period = period.lower()

    if period == "monthly":
        return monthly_date_range(month, year)
    elif period == "ytd":
        return ytd_date_range(month, year)
    
    logger.warning(f"Invalid period: {period}. Defaulting to monthly.")

    return monthly_date_range(month, year)