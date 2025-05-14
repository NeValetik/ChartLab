import pandas as pd
import os
import seaborn as sns
import matplotlib.colors
import plotly.express as px

def plot_comparison(df, value_col, category_col):
    # Sort and aggregate data
    grouped_data = df.groupby(category_col)[value_col].sum().sort_values(ascending=False).reset_index()

    # Generate colors using seaborn's viridis palette
    colors = sns.color_palette("viridis", len(grouped_data))
    hex_colors = [matplotlib.colors.rgb2hex(color) for color in colors]

    # Create interactive bar plot
    fig = px.bar(
        grouped_data,
        x=category_col,
        y=value_col,
        color=category_col,
        color_discrete_sequence=hex_colors
    )

    # Customize the plot
    fig.update_traces(
        texttemplate='%{y:,.0f}',
        textposition='outside',
        marker=dict(opacity=0.85)
    )

    fig.update_layout(
        title=dict(
            text=f"Comparison of {value_col} across {category_col}",
            font=dict(size=16, family="Arial", color="black")
        ),
        xaxis=dict(
            title=dict(text=category_col, font=dict(size=14, family="Arial")),
            tickangle=-45,
            tickfont=dict(size=12)
        ),
        yaxis=dict(
            title=dict(text=value_col, font=dict(size=14, family="Arial")),
            gridcolor="lightgray",
            gridwidth=0.5,
            showgrid=True
        ),
        plot_bgcolor="white",
        showlegend=False,
        margin=dict(t=60, b=100)
    )

    # Save as HTML
    filename = f"{value_col}_vs_{category_col}.html"
    filepath = get_img_output_path(filename)
    fig.write_html(filepath, include_plotlyjs="cdn")
    return filepath

def plot_line_graph(df, x_col, y_col):
    # Convert to datetime
    df[y_col] = pd.to_datetime(df[y_col])

    # Create interactive line plot
    fig = px.line(
        df,
        x=y_col,
        y=x_col,
        title=f"Trend of {x_col} Over Time"
    )

    # Customize the plot
    fig.update_traces(
        line=dict(color="blue", width=2.5),
        hovertemplate="<b>Date</b>: %{x|%Y-%m-%d}<br><b>Value</b>: %{y}<extra></extra>"
    )

    fig.update_layout(
        title=dict(
            text=f"Trend of {x_col} Over Time",
            font=dict(size=16, family="Arial", color="black")
        ),
        xaxis=dict(
            title=dict(text=y_col, font=dict(size=14, family="Arial")),
            tickangle=-45,
            gridcolor="rgba(211, 211, 211, 0.6)",
            gridwidth=0.5,
            showgrid=True
        ),
        yaxis=dict(
            title=dict(text=x_col, font=dict(size=14, family="Arial")),
            gridcolor="rgba(211, 211, 211, 0.6)",
            gridwidth=0.5,
            showgrid=True
        ),
        plot_bgcolor="white",
        hovermode="x unified",
        margin=dict(t=60, b=100),
        legend=dict(
            title_text="",
            x=0.02,
            y=0.98,
            bgcolor="rgba(255, 255, 255, 0.8)"
        )
    )

    filename = f"{x_col}_and_{y_col}.html"
    filepath = get_img_output_path(filename)
    fig.write_json(filepath, include_plotlyjs="cdn")
    return filepath

def get_img_output_path(filename: str) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.abspath(os.path.join(script_dir, ".."))
    output_dir = os.path.join(src_dir, "data", "img")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, filename)