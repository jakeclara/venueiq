import datetime
from src.metrics.metrics_helpers import compute_percentage, compute_total, compute_gross_profit
from src.services import budget, restaurant_service
from src.utils import dates


def get_statement_metrics(month: int, year: int) -> dict:
    """
    Retrieves monthly statement metrics for the given month and year.

    Args:
        month (int): The calendar month (1-12).
        year (int): The calendar year.

    Returns:
        dict: A dictionary containing the actual revenue, cost, profit, budgeted revenue, cost, profit,
        and prior year's revenue, cost, and profit for the given period.
    """
    mtd_start, mtd_end = dates.get_period_range("monthly", month, year)
    ytd_start, ytd_end = dates.get_period_range("ytd", month, year)

    actual_revenue = get_revenue_metrics(mtd_start, mtd_end, ytd_start, ytd_end)
    actual_cost = get_cost_metrics(mtd_start, mtd_end, ytd_start, ytd_end, actual_revenue)
    actual_profit = get_profit_metrics(actual_revenue, actual_cost)

    budgeted_revenue = get_budgeted_revenue_metrics(month, year)
    budgeted_cost = get_budgeted_cost_metrics(month, year, budgeted_revenue)
    budgeted_profit = get_budgeted_profit_metrics(budgeted_revenue, budgeted_cost)

    py_mtd_start, py_mtd_end = dates.get_period_range("monthly", month, year - 1)
    py_ytd_start, py_ytd_end = dates.get_period_range("ytd", month, year - 1)

    prior_year_revenue = get_revenue_metrics(py_mtd_start, py_mtd_end, py_ytd_start, py_ytd_end)
    prior_year_cost = get_cost_metrics(py_mtd_start, py_mtd_end, py_ytd_start, py_ytd_end, prior_year_revenue)
    prior_year_profit = get_profit_metrics(prior_year_revenue, prior_year_cost)

    return {
        "actual": {
            "revenue": actual_revenue,
            "cost": actual_cost,
            "profit": actual_profit
        },
        "budgeted": {
            "revenue": budgeted_revenue,
            "cost": budgeted_cost,
            "profit": budgeted_profit
        },
        "prior_year": {
            "revenue": prior_year_revenue,
            "cost": prior_year_cost,
            "profit": prior_year_profit
        }
    }
        

def get_revenue_metrics(mtd_start: datetime, mtd_end: datetime, ytd_start: datetime, ytd_end: datetime) -> dict:
    """
    Retrieves monthly and year-to-date actual revenue metrics for the given period.

    Args:
        mtd_start (datetime): The start date of the monthly period.
        mtd_end (datetime): The end date of the monthly period.
        ytd_start (datetime): The start date of the year-to-date period.
        ytd_end (datetime): The end date of the year-to-date period.

    Returns:
        dict: A dictionary containing the monthly and year-to-date actual revenue metrics.
    """
    mtd_revenue = restaurant_service.get_restaurant_sales_by_category(mtd_start, mtd_end)
    mtd_revenue_map = {category["_id"]: category["total_sales"] for category in mtd_revenue}
    mtd_food_revenue = mtd_revenue_map.get("Food", 0)
    mtd_bev_revenue = mtd_revenue_map.get("Beverage", 0)
    mtd_total_revenue = compute_total(mtd_food_revenue, mtd_bev_revenue)

    ytd_revenue = restaurant_service.get_restaurant_sales_by_category(ytd_start, ytd_end)
    ytd_revenue_map = {category["_id"]: category["total_sales"] for category in ytd_revenue}
    ytd_food_revenue = ytd_revenue_map.get("Food", 0)
    ytd_bev_revenue = ytd_revenue_map.get("Beverage", 0)
    ytd_total_revenue = compute_total(ytd_food_revenue, ytd_bev_revenue)

    return {
        "mtd": {
            "food_revenue": mtd_food_revenue,
            "beverage_revenue": mtd_bev_revenue,
            "total_revenue": mtd_total_revenue
        },
        "ytd": {
            "food_revenue": ytd_food_revenue,
            "beverage_revenue": ytd_bev_revenue,
            "total_revenue": ytd_total_revenue
        }
    }


def get_cost_metrics(
        mtd_start: datetime,
        mtd_end: datetime,
        ytd_start: datetime,
        ytd_end: datetime,
        revenue_metrics: dict
) -> dict:
    """
    Retrieves the monthly and year-to-date actual cost metrics.

    Args:
        mtd_start (datetime): The start date of the monthly date range.
        mtd_end (datetime): The end date of the monthly date range.
        ytd_start (datetime): The start date of the year-to-date date range.
        ytd_end (datetime): The end date of the year-to-date date range.
        revenue_metrics (dict): A dictionary containing the monthly and year-to-date revenue metrics.

    Returns:
        dict: A dictionary containing the monthly and year-to-date actual cost metrics.
    """
    mtd_costs = restaurant_service.get_restaurant_cost_by_category(mtd_start, mtd_end)
    mtd_cost_map = {category["_id"]: category["total_cost"] for category in mtd_costs}
    mtd_food_cost = mtd_cost_map.get("Food", 0)
    mtd_bev_cost = mtd_cost_map.get("Beverage", 0)
    mtd_total_cost = compute_total(mtd_food_cost, mtd_bev_cost)

    mtd_food_cost_pct = compute_percentage(mtd_food_cost, revenue_metrics["mtd"]["food_revenue"])
    mtd_bev_cost_pct = compute_percentage(mtd_bev_cost, revenue_metrics["mtd"]["beverage_revenue"])

    ytd_costs = restaurant_service.get_restaurant_cost_by_category(ytd_start, ytd_end)
    ytd_cost_map = {category["_id"]: category["total_cost"] for category in ytd_costs}
    ytd_food_cost = ytd_cost_map.get("Food", 0)
    ytd_bev_cost = ytd_cost_map.get("Beverage", 0)
    ytd_total_cost = compute_total(ytd_food_cost, ytd_bev_cost)

    ytd_food_cost_pct = compute_percentage(ytd_food_cost, revenue_metrics["ytd"]["food_revenue"])
    ytd_bev_cost_pct = compute_percentage(ytd_bev_cost, revenue_metrics["ytd"]["beverage_revenue"])

    return {
        "mtd": {
            "food_cost": mtd_food_cost,
            "beverage_cost": mtd_bev_cost,
            "total_cost": mtd_total_cost,
            "food_cost_pct": mtd_food_cost_pct,
            "beverage_cost_pct": mtd_bev_cost_pct
        },
        "ytd": {
            "food_cost": ytd_food_cost,
            "beverage_cost": ytd_bev_cost,
            "total_cost": ytd_total_cost,
            "food_cost_pct": ytd_food_cost_pct,
            "beverage_cost_pct": ytd_bev_cost_pct
        }
    }


def get_profit_metrics(revenue_metrics: dict, cost_metrics: dict) -> dict:
    """
    Retrieves profit metrics for the given period.

    Args:
        revenue_metrics (dict): A dictionary containing the monthly and year-to-date revenue metrics.
        cost_metrics (dict): A dictionary containing the monthly and year-to-date cost metrics.

    Returns:
        dict: A dictionary containing the computed profit metrics for the given period.
    """
    return {
        "mtd": {
            "gross_profit": compute_gross_profit(
                revenue_metrics["mtd"]["total_revenue"],
                cost_metrics["mtd"]["total_cost"]
            )
        },
        "ytd": {
            "gross_profit": compute_gross_profit(
                revenue_metrics["ytd"]["total_revenue"],
                cost_metrics["ytd"]["total_cost"])
        }
    }


def get_budgeted_revenue_metrics(month: int, year: int) -> dict:
    """
    Retrieves the budgeted revenue metrics for the given month and year.

    Args:
        month (int): The month for which to retrieve the budgeted revenue metrics.
        year (int): The year for which to retrieve the budgeted revenue metrics.

    Returns:
        dict: A dictionary containing the budgeted revenue metrics for the given month and year.
    """
    mtd_budgeted_food_revenue = budget.restaurant_budget_service.get_monthly_budgeted_food_revenue(month, year)
    mtd_budgeted_bev_revenue = budget.restaurant_budget_service.get_monthly_budgeted_bev_revenue(month, year)
    mtd_budgeted_total_revenue = compute_total(mtd_budgeted_food_revenue, mtd_budgeted_bev_revenue)

    ytd_budgeted_food_revenue = budget.restaurant_budget_service.get_ytd_budgeted_food_revenue(month, year)
    ytd_budgeted_bev_revenue = budget.restaurant_budget_service.get_ytd_budgeted_bev_revenue(month, year)
    ytd_budgeted_total_revenue = compute_total(ytd_budgeted_food_revenue, ytd_budgeted_bev_revenue)

    return {
        "mtd": {
            "food_revenue": mtd_budgeted_food_revenue,
            "beverage_revenue": mtd_budgeted_bev_revenue,
            "total_revenue": mtd_budgeted_total_revenue
        },
        "ytd": {
            "food_revenue": ytd_budgeted_food_revenue,
            "beverage_revenue": ytd_budgeted_bev_revenue,
            "total_revenue": ytd_budgeted_total_revenue
        }
    }


def get_budgeted_cost_metrics(month: int, year: int, revenue_metrics: dict) -> dict:
    """
    Retrieves budgeted cost metrics for the given month and year.

    Args:
        month (int): The month for which to retrieve the budgeted cost metrics.
        year (int): The year for which to retrieve the budgeted cost metrics.
        revenue_metrics (dict): A dictionary containing the revenue metrics for the given month and year.

    Returns:
        dict: A dictionary containing the budgeted cost metrics for the given month and year.
    """
    mtd_budgeted_food_cost = budget.restaurant_budget_service.get_monthly_budgeted_food_cost(month, year)
    mtd_budgeted_bev_cost = budget.restaurant_budget_service.get_monthly_budgeted_bev_cost(month, year)
    mtd_budgeted_total_cost = compute_total(mtd_budgeted_food_cost, mtd_budgeted_bev_cost)

    mtd_budgeted_food_cost_pct = compute_percentage(
        mtd_budgeted_food_cost,
        revenue_metrics["mtd"]["food_revenue"]
    )
    mtd_budgeted_bev_cost_pct = compute_percentage(
        mtd_budgeted_bev_cost,
        revenue_metrics["mtd"]["beverage_revenue"]
    )

    ytd_budgeted_food_cost = budget.restaurant_budget_service.get_ytd_budgeted_food_cost(month, year)
    ytd_budgeted_bev_cost = budget.restaurant_budget_service.get_ytd_budgeted_bev_cost(month, year)
    ytd_budgeted_total_cost = compute_total(ytd_budgeted_food_cost, ytd_budgeted_bev_cost)

    ytd_budgeted_food_cost_pct = compute_percentage(
        ytd_budgeted_food_cost,
        revenue_metrics["ytd"]["food_revenue"]
    )
    ytd_budgeted_bev_cost_pct = compute_percentage(
        ytd_budgeted_bev_cost,
        revenue_metrics["ytd"]["beverage_revenue"]
    )

    return {
        "mtd": {
            "food_cost": mtd_budgeted_food_cost,
            "beverage_cost": mtd_budgeted_bev_cost,
            "total_cost": mtd_budgeted_total_cost,
            "food_cost_pct": mtd_budgeted_food_cost_pct,
            "beverage_cost_pct": mtd_budgeted_bev_cost_pct
        },
        "ytd": {
            "food_cost": ytd_budgeted_food_cost,
            "beverage_cost": ytd_budgeted_bev_cost,
            "total_cost": ytd_budgeted_total_cost,
            "food_cost_pct": ytd_budgeted_food_cost_pct,
            "beverage_cost_pct": ytd_budgeted_bev_cost_pct
        }
    }


def get_budgeted_profit_metrics(revenue_metrics: dict, cost_metrics: dict) -> dict:
    """
    Retrieves budgeted profit metrics for the given period.

    Args:
        revenue_metrics (dict): A dictionary containing the revenue metrics for the given period.
        cost_metrics (dict): A dictionary containing the cost metrics for the given period.

    Returns:
        dict: A dictionary containing the budgeted profit metrics for the given period.
    """
    return {
        "mtd": {
            "gross_profit": compute_gross_profit(
                revenue_metrics["mtd"]["total_revenue"],
                cost_metrics["mtd"]["total_cost"]
            )
        },
        "ytd": {
            "gross_profit": compute_gross_profit(
                revenue_metrics["ytd"]["total_revenue"],
                cost_metrics["ytd"]["total_cost"])
        }
    }
