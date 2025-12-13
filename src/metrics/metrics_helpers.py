# contains helper functions for metrics operations

def format_metric(value: float, symbol: str="$", precision: int = 2) -> str:

    """
    Formats a given value with the given symbol and precision.

    Args:
        value (float): The value to be formatted.
        symbol (str): The symbol to be used for formatting.
        precision (int): The number of decimal places to round the result to. Defaults to 2.

    Returns:
        str: A string with the formatted value.
    """
    if symbol == "$":
        return f"${value:,.0f}"
    elif symbol == "%":
        return f"{value:,.{precision}f}%"

    return f"{value:,.0f}"


def compute_percentage(numerator: float,
                       denominator: float,
                       precision: int = 2,
                       as_fraction: bool = False
) -> float | None:
    """
    Computes the percentage of a given numerator and denominator

    Args:
        numerator (float): The numerator for the percentage calculation.
        denominator (float): The denominator for the percentage calculation.
        precision (int): The number of decimal places to round the result to. Defaults to 2.
        as_fraction (bool): If True, the result is returned as a fraction. If False, the result is returned as a percentage. 
                            Defaults to False.

    Returns:
        float | None: The computed percentage, or None if either the numerator or denominator is None or 0.
    """
    if numerator is None or denominator in (None, 0):
        return None

    percent = (numerator / denominator) * 100

    value = percent / 100 if as_fraction else percent

    return round(value, precision)


def compute_total(a: float, b: float) -> float:
    """
    Computes the total from passing a and b values

    Args:
        a (float): The first value.
        b (float): The second value.

    Returns:
        float: The total from a and b, rounded to 2 decimal places.
    """
    return a + b


def compute_gross_profit(actual_revenue : float, actual_costs: float) -> float:
    """
    Computes the gross profit from passing actual revenue and actual cost values

    Args:
        actual_revenue (float): The total revenue.
        actual_costs (float): The total cost.

    Returns:
        float: The gross profit, rounded to 2 decimal places.
    """
    return actual_revenue - actual_costs
