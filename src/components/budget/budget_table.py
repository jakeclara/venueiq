
from dash import dash_table
from dash.dash_table.Format import Format, Group, Scheme

from src.utils.constants import MONTHS, STATEMENT_TABLE_COLORS

def get_budget_table_columns():
    """
    Returns a list of column definitions for a budget table component.

    The list will contain the following columns:

    - "account": A text column for the account/section name.
    - Twelve numeric columns, one for each month of the year.
    - "Total": A numeric column that displays the total budget for the year.

    Returns:
        list: A list of column definitions for the budget table component.
    """
    columns = [
        {
            "id": "account",
            "name": "",
            "type": "text",
        }
    ]

    for month in MONTHS:
        columns.append({
            "id": str(month["value"]),
            "name": month["label"],   
            "type": "numeric",
            "format": Format(group=Group.yes, precision=0, scheme=Scheme.fixed),
        })

    columns.append({
        "id": "total",
        "name": "Total",
        "type": "numeric",
        "format": Format(group=Group.yes, precision=0, scheme=Scheme.fixed),
    })

    return columns

# create a list of month column IDs
month_cols = [str(month) for month in range(1, 13)] + ["total"]

def make_budget_table(table_id: str = "budget-table", **kwargs: dict) -> dash_table.DataTable:
    """
    Creates a dash_table.DataTable component with the given columns and data.

    Parameters
    ----------
    table_id : str, optional
        The id of the table to be created. Defaults to "budget-table".
    **kwargs : dict
        Keyword arguments to be passed to the DataTable constructor.

    Returns
    -------
    dash_table.DataTable
        The DataTable object with the given columns and data.
    """
    return dash_table.DataTable(
        id=table_id,
        columns=get_budget_table_columns(),
        data=kwargs.get("data", []),
        fixed_rows={'headers': True, 'data': 1},
        style_header={
            # bold, centered, and colored header text
            'fontWeight': 'bold',
            'backgroundColor': STATEMENT_TABLE_COLORS['header'],
            'textAlign': 'center',
            'color': STATEMENT_TABLE_COLORS['header_text']
        },
        style_table={
            # allow horizontal scrolling
            'overflowX': 'auto'
        },
        style_cell={
            # center text in cells, and set padding and width
            'height': 'auto',
            'minWidth': '100px',
            'width': '100px',
            'maxWidth': '150px',
            'whiteSpace': 'normal',
            'textAlign': 'right',
            'padding': '8px'
        },
        style_cell_conditional=[
            {
                "if": {"column_id": "account"},
                "minWidth": "150px",
                "width": "150px",
                "maxWidth": "150px",
                "textAlign": "left",
            }
        ],
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': STATEMENT_TABLE_COLORS['odd'],
            },
            {
                "if": {"filter_query": "{is_section} = True"},
                "fontWeight": "bold",
            },
            {
                "if": {"filter_query": '{row_id} = "gross_profit"'},
                "fontWeight": "bold",
            },
            *[
                {
                    "if": {"filter_query": f'{{account}} = "{total_name}"'},
                    "borderTop": f"2px solid {STATEMENT_TABLE_COLORS['total_border']}",
                    "borderBottom": f"2px solid {STATEMENT_TABLE_COLORS['total_border']}",
                    "paddingTop": "8px",
                }
                for total_name in ["Total Revenues", "Total Cost"]
            ],
        ],
        **kwargs
    )