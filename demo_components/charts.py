"""
Chart Utilities for Riyadh Architecture Explorer.

Placeholder functions returning minimal Plotly figures.
These will be populated with architecture diagrams, pipeline visualizations,
and KPI charts in future milestones.
"""

import plotly.graph_objects as go


def placeholder_chart(title: str = "Chart") -> go.Figure:
    """
    Return an empty Plotly figure with dark theme and placeholder message.

    Args:
        title: Chart title.

    Returns:
        go.Figure: A minimal placeholder figure.
    """
    fig = go.Figure()
    fig.update_layout(
        title=dict(text=f"{title} — [Coming in future milestone]", font=dict(color="#8B949E")),
        paper_bgcolor="#0D1117",
        plot_bgcolor="#0D1117",
        font=dict(color="#E6EDF3"),
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        height=300,
    )
    fig.add_annotation(
        text="Architecture diagram placeholder",
        showarrow=False,
        font=dict(color="#30363D", size=16),
    )
    return fig


def placeholder_timeseries(title: str = "Timeseries") -> go.Figure:
    """
    Return an empty timeseries figure.

    Args:
        title: Chart title.

    Returns:
        go.Figure: A minimal placeholder figure.
    """
    fig = go.Figure()
    fig.update_layout(
        title=dict(text=f"{title} — [Coming in future milestone]", font=dict(color="#8B949E")),
        paper_bgcolor="#0D1117",
        plot_bgcolor="#0D1117",
        font=dict(color="#E6EDF3"),
        height=300,
    )
    fig.add_annotation(
        text="Timeseries placeholder",
        showarrow=False,
        font=dict(color="#30363D", size=16),
    )
    return fig


def placeholder_gauge(title: str = "Gauge") -> go.Figure:
    """
    Return an empty gauge figure.

    Args:
        title: Chart title.

    Returns:
        go.Figure: A minimal placeholder figure.
    """
    fig = go.Figure()
    fig.update_layout(
        title=dict(text=f"{title} — [Coming in future milestone]", font=dict(color="#8B949E")),
        paper_bgcolor="#0D1117",
        plot_bgcolor="#0D1117",
        font=dict(color="#E6EDF3"),
        height=300,
    )
    fig.add_annotation(
        text="Gauge placeholder",
        showarrow=False,
        font=dict(color="#30363D", size=16),
    )
    return fig
