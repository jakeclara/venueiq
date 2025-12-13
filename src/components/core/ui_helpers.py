from dash import html
from src.utils.constants import THEME_COLORS


def get_donut_chart_colors(actual: float, budgeted: float) -> dict:
    """
    Returns a dictionary with "actual" and "remaining" keys containing the 
    theme colors to be used for a donut chart based on the given actual and budgeted values.

    The "remaining" key will always contain the "secondary" color.
    """
    if actual >= budgeted:
        actual_color = THEME_COLORS["success"]
    elif actual >= 0.9 * budgeted:
        actual_color = THEME_COLORS["warning"]
    else:
        actual_color = THEME_COLORS["danger"]

    return {
        "actual": actual_color,
        "remaining": THEME_COLORS["secondary"]
    }


def get_variance_color(variance: float) -> str:
    """
    Returns the corresponding theme color based on the variance value.

    Args:
        variance (float): The variance value.

    Returns:
        str: The corresponding theme color.
    """
    return THEME_COLORS["success"] if variance >= 0 else THEME_COLORS["danger"]


def variance_bar(variance: float) -> html.Div:
    """
    Returns a html.Div element with a style that displays a variance bar based on the given variance value.

    Args:
        variance (float): The variance value.

    Returns:
        html.Div: A html.Div element with a style that displays a variance bar based on the given variance value.
    """
    return html.Div(
        style={
            "height": "6px",
            "width": "25%",
            "backgroundColor": get_variance_color(variance),
            "margin": "0 auto",
            "borderRadius": "3px",
        }
    )