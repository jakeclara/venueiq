# contains helper functions for metrics operations

def format_metric(value: float | None, symbol: str="$", precision: int = 2) -> str:
    """
    Formats a given value with the given symbol and precision.

    Args:
        value (float | None): The value to format.
        symbol (str): The symbol to use for formatting, either "$" or "%".
        precision (int): The number of decimal places to round to.

    Returns:
        str: The formatted string.
    """
    if value is None:
        return "-"
    
    if symbol == "$":
        return f"${value:,.0f}"
    elif symbol == "%":
        return f"{value:,.{precision}f}%"

    return f"{value:,.0f}"


def compute_percentage(numerator: float | None,
                       denominator: float | None,
                       precision: int = 2,
                       as_fraction: bool = False
) -> float | None:
    """
    Computes the percentage of a given numerator and denominator.

    Args:
        numerator (float | None): The numerator for the percentage calculation.
        denominator (float | None): The denominator for the percentage calculation.
        precision (int): The number of decimal places to round to, defaults to 2.
        as_fraction (bool): Whether to return the percentage as a fraction of 1, or as a percentage value, defaults to False.

    Returns:
        float | None: The computed percentage, or None if either the numerator or denominator is None or 0.
    """
    if numerator is None or denominator in (None, 0):
        return None

    percent = (numerator / denominator) * 100

    value = percent / 100 if as_fraction else percent

    return round(value, precision)


def compute_total(a: float | None, b: float | None) -> float:
    """
    Computes the total of two given values, treating None as 0.

    Args:
        a (float | None): The first value to add.
        b (float | None): The second value to add.

    Returns:
        float: The total of a and b, or 0 if either a or b is None.
    """
    val_a = 0 if a is None else a
    val_b = 0 if b is None else b

    return val_a + val_b


def compute_gross_profit(actual_revenue : float | None, actual_costs: float | None) -> float:
    """
    Computes the gross profit by subtracting actual costs from actual revenue.

    Args:
        actual_revenue (float | None): The actual revenue.
        actual_costs (float | None): The actual costs.

    Returns:
        float: The gross profit.
    """
    revenue = 0 if actual_revenue is None else actual_revenue
    costs = 0 if actual_costs is None else actual_costs

    return revenue - costs
