# builds rows for the budget table

from src.metrics.metrics_helpers import compute_percentage, format_metric

def build_budget_table_rows(budget_docs: list[object]) -> list[dict]:
    """
    Builds a list of rows for the budget table based on the combined budget documents.

    Args:
        budget_docs (list[object]): A list of combined budget documents for a given year.

    Returns:
        list[dict]: A list of rows for the budget table.
    """
    months = {}
    for month in range(1, 13):
        months[month] = {}
    
    # iterate through the budget documents and populate the months dictionary
    for doc in budget_docs:
        months[doc.month] = {
            "food_sales": doc.food_sales,
            "bev_sales": doc.bev_sales,
            "event_sales": doc.event_sales,
            "total_sales": doc.total_sales,
            "food_cost": doc.food_cost,
            "bev_cost": doc.bev_cost,
            "event_cost": doc.event_cost,
            "total_cost": doc.total_cost,
            "gross_profit": doc.gross_profit
        }
    
    # helper function to build a row in the table
    def row(label: str, field: str, row_id: str) -> dict:
        """
        Builds a row in the budget table.

        Args:
            label (str): The label for the row.
            field (str): The field to retrieve from the budget documents.
            row_id (str): The ID for the row.

        Returns:
            dict: A dictionary representing the row in the table.
        """
        values = {}
        for month in range(1, 13):
            values[str(month)] = months[month].get(field, 0.0)
        
        total = sum(values.values())

        return {
            "row_id": row_id,
            "account": label,
            **values,
            "total": total
        }
    

    # helper function to build a row in the table with percentages
    def percent_row(label: str, cost_field: str, sales_field: str, row_id: str) -> list[dict]:
        """
        Builds a row in the budget table with percentages.

        Args:
            label (str): The label for the row.
            cost_field (str): The field to retrieve from the budget documents for the cost.
            sales_field (str): The field to retrieve from the budget documents for the sales.
            row_id (str): The ID for the row.

        Returns:
            dict: A dictionary representing the row in the table.
        """
        values = {}
        total_sales = 0.0
        total_cost = 0.0

        for month in range(1, 13):
            sales = months[month].get(sales_field, 0.0)
            cost = months[month].get(cost_field, 0.0)
            pct = compute_percentage(cost, sales)
            values[str(month)] = format_metric(pct, "%")

            total_sales += sales
            total_cost += cost

        total_pct = compute_percentage(total_cost, total_sales)

        return {
            "row_id": row_id,
            "account": label,
            **values,
            "total": format_metric(total_pct, "%")
        }
        

    # build the rows in the table
    rows = [
        {
        "row_id": "section_revenue",
        "account": "Revenues",
        "is_section": "True",
        },
        row("Food", "food_sales", row_id="food_sales"),
        row("Beverage", "bev_sales", row_id="bev_sales"),
        row("Event", "event_sales", row_id="event_sales"),
        row("Total Revenues", "total_sales", row_id="total_sales"),
        {
        "row_id": "section_cost",
        "account": "Cost of Sales",
        "is_section": "True",
        },
        row("Food", "food_cost", row_id="food_cost"),
        row("Beverage", "bev_cost", row_id="bev_cost"),
        row("Event", "event_cost", row_id="event_cost"),
        row("Total Cost", "total_cost", row_id="total_cost"),
        {
        "row_id": "section_cogs_pct",
        "account": "COGS - %",
        "is_section": "True",
        },
        percent_row("Food", "food_cost", "food_sales", row_id="food_cogs_pct"),
        percent_row("Beverage", "bev_cost", "bev_sales", row_id="bev_cogs_pct"),
        percent_row("Event", "event_cost", "event_sales", row_id="event_cogs_pct"),

        row("Gross Profit", "gross_profit", row_id="gross_profit"),
    ]

    return rows