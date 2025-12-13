# reusable table for p&l style statement for food or events departments

from dash import dash_table
from dash.dash_table.Format import Format, Group, Scheme


from src.metrics.metrics_helpers import compute_percentage, format_metric
from src.utils.constants import STATEMENT_SECTION_HEADERS, STATEMENT_TABLE_COLORS

# table columns
columns = [
    {"name": "", "id": "line_item"},
    {
        "name": "Actual", 
        "id": "mtd_actual",
        "type": "numeric",
        "format": Format(
            precision=0,
            group=Group.yes,
            group_delimiter=",",
            scheme=Scheme.fixed
        )
    },
    {
        "name": "MTD Budget",
        "id": "mtd_budget",
        "type": "numeric",
        "format": Format(
            precision=0,
            group=Group.yes,
            group_delimiter=",",
            scheme=Scheme.fixed
        )
    },
    {
        "name": "% of Budget",
        "id": "mtd_pct_budget",
        "type": "numeric",
        "format": Format(
            precision=0,
            scheme='%',
        )
    },
    {
        "name": "MTD Prior Year",
        "id": "mtd_py",
        "type": "numeric",
        "format": Format(
            precision=0,
            group=Group.yes,
            group_delimiter=",",
            scheme=Scheme.fixed
        )
    },
    {
        "name": "% of PY",
        "id": "mtd_pct_py",
        "type": "numeric",
        "format": Format(
            precision=0,
            scheme='%',
        )},
    {
        "name": "YTD Actual",
        "id": "ytd_actual",
        "type": "numeric",
        "format": Format(
            precision=0,
            group=Group.yes,
            group_delimiter=",",
            scheme=Scheme.fixed
        )
    },
    {
        "name": "YTD Budget",
        "id": "ytd_budget",
        "type": "numeric",
        "format": Format(
            precision=0,
            group=Group.yes,
            group_delimiter=",",
            scheme=Scheme.fixed
        )
    },
    {
        "name": "% of Budget",
        "id": "ytd_pct_budget",
        "type": "numeric",
        "format": Format(
            precision=0,
            scheme='%',
        )},
    {
        "name": "YTD Prior Year",
        "id": "ytd_py",
        "type": "numeric",
        "format": Format(
            precision=0,
            group=Group.yes,
            group_delimiter=",",
            scheme=Scheme.fixed
        )
    },
    {
        "name": "% of PY",
        "id": "ytd_pct_py",
        "type": "numeric",
        "format": Format(
            precision=0,
            scheme='%',
        )},
]

# columns with %
percent_column_ids = [
        col['id'] for col in columns if "%" in col['name']
]


def make_statement_table(table_id: str = "statement-table", **kwargs: dict) -> dash_table.DataTable:
    """
    Creates a dash_table.DataTable with the given columns and data.

    Parameters
    ----------
    table_id : str, optional
        The id of the table to be created. Defaults to "statement-table".
    **kwargs : dict
        Keyword arguments to be passed to the DataTable constructor.

    Returns
    -------
    dash_table.DataTable
        The DataTable object with the given columns and data.
    """
    return dash_table.DataTable(
        id=table_id,
        columns=columns,
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
            'padding': '6px'
        },
        style_cell_conditional=[
            # set max width and text alignment for the line item column
            {
                'if': {'column_id': 'line_item'},
                'maxWidth': '150px',
                'width': '150px',
                'textAlign': 'left',
            },
        ],
        style_data_conditional=[
            # set bold text for each label in the section headers
            *[
                {
                    'if': {
                        'filter_query': f'{{line_item}} = "{label}"',
                    },
                    'fontWeight': 'bold',
                }
                for label in STATEMENT_SECTION_HEADERS
            ],
            # set background color for odd rows
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': STATEMENT_TABLE_COLORS['odd'],
            },
            # set border and padding for the total row
            {
                "if": {"filter_query": '{line_item} = "Total"'},
                "borderTop": f"2px solid {STATEMENT_TABLE_COLORS['total_border']}",
                "borderBottom": f"2px solid {STATEMENT_TABLE_COLORS['total_border']}",
                "paddingTop": "8px",
            },
            # set background color for each percentage column
            *[
                {
                    'if': {'column_id': col_id},
                    'backgroundColor': STATEMENT_TABLE_COLORS['pct_column_bg'],
                }
                for col_id in percent_column_ids
            ],
        ],
        **kwargs
    )
