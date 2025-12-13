# executes aggregates for the budget page

from src.services import budget
from src.metrics.metrics_helpers import compute_percentage, format_metric

def get_annual_budget_data(year: int) -> list:
    """
    Retrieves a list of combined budget documents for a given year.

    Args:
        year (int): The year for which to retrieve the combined budget documents.

    Returns:
        list: A list of combined budget documents for the specified year.
    """
    return budget.combined_budget_service.get_annual_budget_docs(year)
