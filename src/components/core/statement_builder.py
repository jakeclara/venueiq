# builds a list of dictionaries to represent the restaurant statement page table rows

from src.metrics.metrics_helpers import compute_percentage, format_metric
from src.utils.constants import STATEMENT_SECTION_HEADERS


def build_statement_rows(metrics: dict) -> list[dict]:
    """
    Builds a list of dictionaries to represent the restaurant statement page table.

    Each dictionary has the following keys:
    - line_item: the name of the line item
    - mtd_actual: the actual MTD value
    - mtd_budget: the budgeted MTD value
    - mtd_pct_budget: the percentage of budgeted MTD value vs actual MTD value
    - mtd_py: the actual MTD value of the prior year
    - mtd_pct_py: the percentage of actual MTD value of the prior year vs actual MTD value
    - ytd_actual: the actual YTD value
    - ytd_budget: the budgeted YTD value
    - ytd_pct_budget: the percentage of budgeted YTD value vs actual YTD value
    - ytd_py: the actual YTD value of the prior year
    - ytd_pct_py: the percentage of actual YTD value of the prior year vs actual YTD value

    Args:
    metrics (dict): a dictionary containing the metrics for the restaurant statement page table

    Returns:
    list[dict]: a list of dictionaries representing the restaurant statement page table
    """
    rows = []

    # revenues
    rows.append({
        "line_item": STATEMENT_SECTION_HEADERS[0],
        "mtd_actual": None,
        "mtd_budget": None,
        "mtd_pct_budget": None,
        "mtd_py": None,
        "mtd_pct_py": None,
        "ytd_actual": None,
        "ytd_budget": None,
        "ytd_pct_budget": None,
        "ytd_py": None,
        "ytd_pct_py": None,
    })
    
    # loop through categories and fill in the data
    for category in ["Food", "Beverage", "Total"]:
        mtd_actual = metrics["actual"]["revenue"]["mtd"][f"{category.lower()}_revenue"]
        mtd_budget = metrics["budgeted"]["revenue"]["mtd"][f"{category.lower()}_revenue"]
        mtd_py = metrics["prior_year"]["revenue"]["mtd"][f"{category.lower()}_revenue"]
        ytd_actual = metrics["actual"]["revenue"]["ytd"][f"{category.lower()}_revenue"]
        ytd_budget = metrics["budgeted"]["revenue"]["ytd"][f"{category.lower()}_revenue"]
        ytd_py = metrics["prior_year"]["revenue"]["ytd"][f"{category.lower()}_revenue"]

        rows.append({
            "line_item": category,
            "mtd_actual": mtd_actual,
            "mtd_budget": mtd_budget,
            "mtd_pct_budget": compute_percentage(mtd_actual, mtd_budget, as_fraction=True),
            "mtd_py": mtd_py,
            "mtd_pct_py": compute_percentage(mtd_actual, mtd_py, as_fraction=True),
            "ytd_actual": ytd_actual,
            "ytd_budget": ytd_budget,
            "ytd_pct_budget": compute_percentage(ytd_actual, ytd_budget, as_fraction=True),
            "ytd_py": ytd_py,
            "ytd_pct_py": compute_percentage(ytd_actual, ytd_py, as_fraction=True),
        })

    # costs
    rows.append({
        "line_item": STATEMENT_SECTION_HEADERS[1],
        "mtd_actual": None,
        "mtd_budget": None,
        "mtd_pct_budget": None,
        "mtd_py": None,
        "mtd_pct_py": None,
        "ytd_actual": None,
        "ytd_budget": None,
        "ytd_pct_budget": None,
        "ytd_py": None,
        "ytd_pct_py": None,
    })
    
    # loop through categories and fill in the data
    for category in ["Food", "Beverage", "Total"]:
        mtd_actual = metrics["actual"]["cost"]["mtd"][f"{category.lower()}_cost"]
        mtd_budget = metrics["budgeted"]["cost"]["mtd"][f"{category.lower()}_cost"]
        mtd_py = metrics["prior_year"]["cost"]["mtd"][f"{category.lower()}_cost"]
        ytd_actual = metrics["actual"]["cost"]["ytd"][f"{category.lower()}_cost"]
        ytd_budget = metrics["budgeted"]["cost"]["ytd"][f"{category.lower()}_cost"]
        ytd_py = metrics["prior_year"]["cost"]["ytd"][f"{category.lower()}_cost"]

        rows.append({
            "line_item": category,
            "mtd_actual": mtd_actual,
            "mtd_budget": mtd_budget,
            "mtd_pct_budget": compute_percentage(mtd_actual, mtd_budget, as_fraction=True),
            "mtd_py": mtd_py,
            "mtd_pct_py": compute_percentage(mtd_actual, mtd_py, as_fraction=True),
            "ytd_actual": ytd_actual,
            "ytd_budget": ytd_budget,
            "ytd_pct_budget": compute_percentage(ytd_actual, ytd_budget, as_fraction=True),
            "ytd_py": ytd_py,
            "ytd_pct_py": compute_percentage(ytd_actual, ytd_py, as_fraction=True),
        })
    
    # cogs percentage
    rows.append({
        "line_item": STATEMENT_SECTION_HEADERS[2],
        "mtd_actual": None,
        "mtd_budget": None,
        "mtd_pct_budget": None,
        "mtd_py": None,
        "mtd_pct_py": None,
        "ytd_actual": None,
        "ytd_budget": None,
        "ytd_pct_budget": None,
        "ytd_py": None,
        "ytd_pct_py": None,
    })
    
    # loop through categories and fill in the data
    for category in ["Food", "Beverage"]:
        mtd_actual = metrics["actual"]["cost"]["mtd"][f"{category.lower()}_cost_pct"]
        mtd_budget = metrics["budgeted"]["cost"]["mtd"][f"{category.lower()}_cost_pct"]
        mtd_py = metrics["prior_year"]["cost"]["mtd"][f"{category.lower()}_cost_pct"]
        ytd_actual = metrics["actual"]["cost"]["ytd"][f"{category.lower()}_cost_pct"]
        ytd_budget = metrics["budgeted"]["cost"]["ytd"][f"{category.lower()}_cost_pct"]
        ytd_py = metrics["prior_year"]["cost"]["ytd"][f"{category.lower()}_cost_pct"]

        rows.append({
            "line_item": category,
            "mtd_actual": format_metric(mtd_actual, "%"),
            "mtd_budget": format_metric(mtd_budget, "%"),
            "mtd_pct_budget": compute_percentage(mtd_actual, mtd_budget, as_fraction=True),
            "mtd_py": format_metric(mtd_py, "%"),
            "mtd_pct_py": compute_percentage(mtd_actual, mtd_py, as_fraction=True),
            "ytd_actual": format_metric(ytd_actual, "%"),
            "ytd_budget": format_metric(ytd_budget, "%"),
            "ytd_pct_budget": compute_percentage(ytd_actual, ytd_budget, as_fraction=True),
            "ytd_py": format_metric(ytd_py, "%"),
            "ytd_pct_py": compute_percentage(ytd_actual, ytd_py, as_fraction=True),
        })
    
    # profit
    mtd_actual = metrics["actual"]["profit"]["mtd"]["gross_profit"]
    mtd_budget = metrics["budgeted"]["profit"]["mtd"]["gross_profit"]
    mtd_py = metrics["prior_year"]["profit"]["mtd"]["gross_profit"]
    ytd_actual = metrics["actual"]["profit"]["ytd"]["gross_profit"]
    ytd_budget = metrics["budgeted"]["profit"]["ytd"]["gross_profit"]
    ytd_py = metrics["prior_year"]["profit"]["ytd"]["gross_profit"]

    rows.append({
        "line_item": STATEMENT_SECTION_HEADERS[3],
        "mtd_actual": mtd_actual,
        "mtd_budget": mtd_budget,
        "mtd_pct_budget": compute_percentage(mtd_actual, mtd_budget, as_fraction=True),
        "mtd_py": mtd_py,
        "mtd_pct_py": compute_percentage(mtd_actual, mtd_py, as_fraction=True),
        "ytd_actual": ytd_actual,
        "ytd_budget": ytd_budget,
        "ytd_pct_budget": compute_percentage(ytd_actual, ytd_budget, as_fraction=True),
        "ytd_py": ytd_py,
        "ytd_pct_py": compute_percentage(ytd_actual, ytd_py, as_fraction=True),
    })

    return rows