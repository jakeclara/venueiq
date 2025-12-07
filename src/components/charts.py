# contains reusable chart components for the dashboard

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from src.utils.constants import THEME_COLORS

def make_pie_chart(data: pd.DataFrame, names: str, values: str, **kwargs: dict) -> go.Figure:
    """
    Creates a pie chart from the given DataFrame.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data to plot.
    names (str): The column name of the data to use as names.
    values (str): The column name of the data to use as values.
    *kwargs (dict): Additional keyword arguments to pass to plotly.express.pie.

    Returns:
    go.Figure: The pie chart figure.
    """
    fig = px.pie(data,
                 names=names,
                 values=values,
                 hover_name=names,
                 **kwargs)
    
    fig.update_traces(
        hovertemplate="<b>%{label}</b><br>%{value}<extra></extra>"
    )

    return fig


def make_budget_donut(actual: float, budgeted: float, color_map: dict | None = None) -> go.Figure:
    # calculate the percentage of actual compared to budgeted revenue
    percent = (actual / budgeted) * 100
    chart_percent = min(percent, 100)
    # calculate the remaining percentage
    remaining = max(100 - chart_percent, 0.01)

    # create a DataFrame with the label and value for each slice
    df = pd.DataFrame({
        "Label": ["Actual %", "Remaining %"],
        "Value": [chart_percent, remaining]
    })

    # create a pie chart
    fig = go.Figure(go.Pie(
        labels=df["Label"],
        values=df["Value"],
        hole=0.7,
        marker=dict(colors=[color_map["actual"], color_map["remaining"]]) if color_map else None,
        textinfo='none',
        hoverinfo='none'
    ))

    # add an annotation to the chart with the percentage value
    fig.update_layout(
        annotations=[dict(
            text=f"{percent:.0f}%",
            x=0.5, y=0.5,
            font_size=24,
            showarrow=False
        )],
        autosize=True,
        showlegend=False,
        margin=dict(t=0, b=0, l=0, r=0)
    )
    
    return fig


def make_grouped_revenue_bar_chart(data: dict, color_map: dict | None = None, **kwargs: dict) -> go.Figure:
    """
    Creates a grouped bar chart comparing actual revenue, prior year revenue, and budgeted revenue.

    Parameters:
    data (dict): A dictionary containing the actual, prior year, and budgeted revenue data.
    color_map (dict | None): A dictionary of theme colors to use for the bars.
    **kwargs (dict): Additional keyword arguments to pass to plotly.graph_objects.Bar.

    Returns:
    go.Figure: The grouped bar chart figure.
    """
    # create a figure and add a bar trace for actual revenue
    fig = go.Figure()
    fig.add_bar(
        name="Actual",
        x=["Food", "Beverage", "Total"],
        y=[
            data["food"]["actual"],
            data["beverage"]["actual"],
            data["total"]["actual"]
        ],
        marker_color=color_map["actual"] if color_map else None,
        **kwargs
    )

    # add a bar trace for prior year revenue
    fig.add_bar(
        name="Prior Year",
        x=["Food", "Beverage", "Total"],
        y=[
            data["food"]["py"],
            data["beverage"]["py"],
            data["total"]["py"]
        ],
        marker_color=color_map["py"] if color_map else None,
        **kwargs
    )

    # add a bar trace for budgeted revenue
    fig.add_bar(
        name="Budget",
        x=["Total"],
        y=[data["total"]["budgeted"]],
        marker_color=color_map["budgeted"] if color_map else None,
        **kwargs
    )

    # update the layout of the figure
    fig.update_layout(
        barmode='group',
        xaxis_title="",
        yaxis_title="",
        legend_title="",
        margin=dict(l=5, r=5, t=5, b=5),
        showlegend=True,
    )

    return fig


def make_bar_chart(data: dict, x: str, y: str, color_map: dict | None = None, **kwargs: dict) -> go.Figure:
    if isinstance(data, dict):
        data = pd.DataFrame(data)

    if color_map:
        fig = px.bar(
            data_frame=data,
            x=x,
            y=y,
            color=x,
            color_discrete_map=color_map,
            **kwargs
        )
    else:
        fig = px.bar(data_frame=data, x=x, y=y, **kwargs)

    fig.update_layout(
        margin=dict(l=5, r=5, t=5, b=5),
        showlegend=False,
    )

    return fig


def make_line_chart(data: pd.DataFrame, x: str, y: str, **kwargs: dict) -> go.Figure:
    """
    Creates a line chart from the given DataFrame.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data to plot.
    x (str): The column name of the data to use as x values.
    y (str): The column name of the data to use as y values.
    *kwargs (dict): Additional keyword arguments to pass to plotly.express.line.

    Returns:
    go.Figure: The line chart figure.
    """
    fig = px.line(data, x=x, y=y, **kwargs)
    return fig
