import random
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib
import plotly.io as pio
from matplotlib import pyplot as plt

def get_comparison(df, value_col, category_col):
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

    return pio.to_json(fig, pretty=True, remove_uids=True)

def get_comaprison(df, value_col, category_col):
    # Sort and aggregate data
    grouped_data = df.groupby(category_col)[value_col].sum().sort_values(ascending=False).reset_index()
    
    # Create dynamic color scale with smooth transitions
    # color_scale = px.colors.cyclical.Twilight
    color_scale = ['#1C0B85', '#8D2C8C', '#C7636B', '#EBAD51', '#F1F45B']
    max_value = grouped_data[value_col].max()
    
    # Create interactive bar plot with advanced styling
    fig = px.bar(
        grouped_data,
        x=category_col,
        y=value_col,
        color=value_col,
        color_continuous_scale=color_scale,
        text=value_col,
        hover_data={value_col: ':,.0f'},
        height=700,
        template='plotly_white+presentation',
        hover_name=category_col,
        range_y=[0, max_value * 1.15]
    )

    # Custom text positioning with dynamic threshold
    text_position = ['outside' if val < 0.15 * max_value else 'inside' for val in grouped_data[value_col]]
    
    # Update traces with advanced styling
    fig.update_traces(
        texttemplate='<b>%{text:,.0f}</b>',
        textposition=text_position,
        textfont_size=14,
        textfont_color=['white' if pos == 'inside' else '#404040' for pos in text_position],
        marker=dict(
            opacity=0.92,
            line=dict(width=2, color='white'),
        ),
        hovertemplate=(
            "<b>%{hovertext}</b><br><br>"
            f"{value_col}: <b>%{{y:,.0f}}</b><br>"
            "<extra></extra>"
        ),
        hoverlabel=dict(
            bgcolor='white',
            bordercolor='#404040',
            font_size=14
        )
    )

    # Advanced layout configuration
    fig.update_layout(
        title=dict(
            text=f"<span style='font-size:26px; font-weight:600;'>{value_col} ANALYSIS</span><br>"
                 f"<span style='font-size:18px; color:#606060'>{category_col} Distribution</span>",
            x=0.03,
            y=0.93,
            xanchor='left',
            yanchor='top'
        ),
        xaxis=dict(
            title=None,
            tickfont=dict(size=14, color='#606060', family='Poppins'),
            gridcolor='rgba(200, 200, 200, 0.1)',
            linecolor='#d0d0d0',
            showgrid=False,
            automargin=True
        ),
        yaxis=dict(
            title=None,
            gridcolor='rgba(200, 200, 200, 0.2)',
            showgrid=True,
            zeroline=False,
            tickformat=',.0f',
            tickfont=dict(size=12, color='#808080')
        ),
        coloraxis=dict(
            colorbar=dict(
                title=dict(text=f"{value_col} Scale", font=dict(size=12)),
                tickfont=dict(size=10),
                xpad=20,
                ypad=0
            )
        ),
        plot_bgcolor='rgba(255, 255, 255, 0.95)',
        paper_bgcolor='#f8f9fa',
        margin=dict(t=120, b=100, l=60, r=40),
        font=dict(family='Poppins, Arial', color='#404040'),
        separators=',.',
        bargap=0.2,
        bargroupgap=0.05,
        hoverdistance=100,
        annotations=[
            dict(
                x=0.98,
                y=1.12,
                xref='paper',
                yref='paper',
                text="VISUAL ANALYTICS DASHBOARD",
                showarrow=False,
                font=dict(size=16, color='#a0a0a0')
            )
        ]
    )

    # Add decorative elements
    fig.add_shape(
        type="rect",
        xref="paper",
        yref="paper",
        x0=0, y0=0,
        x1=1, y1=1,
        line=dict(color="#e0e0e0", width=2),
        fillcolor="rgba(0,0,0,0)"
    )

    # Add dynamic data summary
    total_value = grouped_data[value_col].sum()
    fig.add_annotation(
        x=0.95,
        y=0.98,
        xref="paper",
        yref="paper",
        text=f"<b>Total {value_col}:</b> {total_value:,.0f}<br>"
             f"<b>Max Value:</b> {max_value:,.0f}",
        showarrow=False,
        align="right",
        font=dict(size=12),
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="#d0d0d0",
        borderwidth=1
    )

    return pio.to_json(fig, pretty=True, remove_uids=True)

def get_line_graph(df, x_col, y_col):
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

    return pio.to_json(fig, pretty=True, remove_uids=True)

def get_grouped_bar_chart(df, y_col, x_col, group_col):
    # Aggregate data
    grouped_data = df.groupby([x_col, group_col])[y_col].sum().reset_index()

    # Generate color palette
    unique_groups = grouped_data[group_col].nunique()
    colors = sns.color_palette("mako", unique_groups)
    colors = [sns.desaturate(c, 0.6) for c in colors]
    hex_colors = [matplotlib.colors.rgb2hex(c) for c in colors]

    # Create grouped bar chart
    fig = px.bar(
        grouped_data,
        x=x_col,
        y=y_col,
        color=group_col,
        barmode='group',
        color_discrete_sequence=hex_colors,
        text=y_col,
        hover_data={y_col: ':,.0f'},
        custom_data=[group_col]
    )

    # Customize text position and formatting
    fig.update_traces(
        texttemplate='<b>%{text:,.0f}</b>',
        textposition='auto',
        insidetextanchor='middle',
        marker=dict(opacity=0.85),
        hovertemplate=(
            f"<b>%{{x}}</b><br>"
            f"<b>{group_col.title()}:</b> %{{customdata[0]}}<br>"  
            f"<b>{y_col.title()}:</b> %{{y:,.0f}}<extra></extra>"
        )
    )

    main_title = f"<span style='font-size:24px; font-weight:600'>{y_col.title()} by {x_col.title()} </span><br><span style='font-size:18px; color:#606060'>Grouped by {group_col.title()}</span>"


    # Update layout with styling
    fig.update_layout(
        title=dict(
            text=f"{main_title}",
            x=0.03,
            y=0.93,
            xanchor='left',
            yanchor='top'
        ),
        xaxis=dict(
            title=None,
            tickfont=dict(size=13),
            tickangle=-45
        ),
        yaxis=dict(
            title=None,
            tickformat=',.0f',
            gridcolor="lightgray",
            gridwidth=0.5
        ),
        plot_bgcolor="white",
        paper_bgcolor='#f9f9f9',
        margin=dict(t=100, b=120),
        bargap=0.15,
        font=dict(family='Poppins, Arial', color='#303030'),
        legend=dict(
            title_text=group_col.title(),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#e0e0e0',
            borderwidth=1,
            orientation='v',
            yanchor='middle',
            y=0.5,
            xanchor='left',
            x=1.02
        )
    )

    return pio.to_json(fig, pretty=True, remove_uids=True)

def get_stacked_bar_chart(df, y_col, x_col, group_col):
    # Aggregate the data
    grouped_data = df.groupby([x_col, group_col])[y_col].sum().reset_index()

    # Determine color palette
    unique_stacks = grouped_data[group_col].nunique()
    colors = sns.color_palette("PuRd", unique_stacks)
    colors = [sns.desaturate(c, 0.5) for c in colors]  # make colors softer
    colors = [(min(1, r + 0.15), min(1, g + 0.15), min(1, b + 0.15)) for (r, g, b) in colors]  # brighten
    hex_colors = [matplotlib.colors.rgb2hex(c) for c in colors]

    # Create the stacked bar chart
    fig = px.bar(
        grouped_data,
        x=x_col,
        y=y_col,
        color=group_col,
        barmode='stack',
        color_discrete_sequence=hex_colors,
        text_auto='.2s',
        hover_data={y_col: ':,.0f'},
        height=700,
        template='plotly_white'
    )

    # Enhance trace aesthetics
    fig.update_traces(
        marker=dict(line=dict(width=1.5, color='white')),
        textfont=dict(size=13),
        textposition='inside',
        hovertemplate="<b>%{x}</b><br>%{customdata[0]}: %{y:,.0f}<extra></extra>",
        customdata=grouped_data[[group_col]]
    )

    # Configure layout
    fig.update_layout(
        title=dict(
            text=f"<span style='font-size:24px; font-weight:600;'>{y_col.title()} by {x_col.title()}</span><br>"
                 f"<span style='font-size:18px; color:#606060'>Stacked by {group_col.title()}</span>",
            x=0.03,
            y=0.95,
            xanchor='left',
            yanchor='top'
        ),
        xaxis=dict(
            title=None,
            tickfont=dict(size=13, family='Poppins', color='#606060'),
            showgrid=False,
            linecolor='#d0d0d0'
        ),
        yaxis=dict(
            title=None,
            gridcolor='rgba(200, 200, 200, 0.3)',
            tickfont=dict(size=12, color='#808080'),
            zeroline=False
        ),
        plot_bgcolor='white',
        paper_bgcolor='#f8f9fa',
        margin=dict(t=100, b=100, l=60, r=40),
        font=dict(family='Poppins, Arial', color='#404040'),
        legend=dict(
            title=dict(text=group_col.title(), font=dict(size=13)),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#e0e0e0',
            borderwidth=1,
            orientation='v',
            yanchor='middle',
            y=0.5,
            xanchor='left',
            x=1.02,
            font=dict(size=12)
        )
    )

    # Optional: Add annotations or summary box
    total_sum = grouped_data[y_col].sum()
    total_sum = float(total_sum)  # ensure it's a number

    fig.add_annotation(
        x=1,
        y=1.02,
        xref="paper",
        yref="paper",
        text=f"<b>Total {y_col}:</b> {total_sum:,.0f}",
        showarrow=False,
        font=dict(size=13),
        align="right",
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="#d0d0d0",
        borderwidth=1
    )

    return pio.to_json(fig, pretty=True, remove_uids=True)

def get_scatter_plot(df, x_col, y_col, point_size=15, marker_symbol="circle", label_col=None):
    if x_col not in df.columns or y_col not in df.columns:
        raise ValueError(f"Columns '{x_col}' or '{y_col}' not found in DataFrame.")

    if pd.api.types.is_string_dtype(df[x_col]) or pd.api.types.is_object_dtype(df[x_col]):
        try:
            df[x_col] = pd.to_datetime(df[x_col])
        except Exception:
            pass

    # Use defined color palette from original example
    color_palette = ['#1C0B85', '#8D2C8C', '#C7636B', '#EBAD51', '#1E88E5']
    choice = int(random.choice([0, 1, 2, 3, 4]))
    point_color = color_palette[choice]  # Consistently styled color (e.g., purple)

    # Define custom hovertemplate
    hover = f"<b>{x_col}</b>: %{{x}}<br><b>{y_col}</b>: %{{y}}"
    if label_col and label_col in df.columns:
        hover += f"<br><b>Label</b>: %{{customdata[0]}}"

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        custom_data=[df[label_col]] if label_col else None
    )

    fig.update_traces(
        marker=dict(
            size=point_size,
            color=point_color,
            symbol=marker_symbol,
            line=dict(width=1.5, color='white'),
            opacity=0.9
        ),
        hovertemplate=hover + "<extra></extra>",
        mode="markers"
    )

    fig.update_layout(
        title=dict(
            text=f"<span style='font-size:26px; font-weight:600;'>{x_col.capitalize()} vs {y_col.capitalize()}</span><br>"
                 f"<span style='font-size:18px; color:#606060'>Scatter Plot</span>",
            x=0.03,
            y=0.93,
            xanchor='left',
            yanchor='top'
        ),
        xaxis=dict(
            title=x_col.capitalize(),
            tickfont=dict(size=14, color='#606060', family='Poppins'),
            gridcolor='rgba(200, 200, 200, 0.1)',
            linecolor='#d0d0d0',
            showgrid=True,
            automargin=True
        ),
        yaxis=dict(
            title=y_col.capitalize(),
            gridcolor='rgba(200, 200, 200, 0.2)',
            showgrid=True,
            zeroline=False,
            tickfont=dict(size=12, color='#808080')
        ),
        plot_bgcolor='rgba(255, 255, 255, 0.95)',
        paper_bgcolor='#f8f9fa',
        margin=dict(t=120, b=100, l=60, r=40),
        font=dict(family='Poppins, Arial', color='#404040'),
        hovermode="closest",
        hoverdistance=100,
        separators=',.',

    )

    # Add decorative frame
    fig.add_shape(
        type="rect",
        xref="paper",
        yref="paper",
        x0=0, y0=0,
        x1=1, y1=1,
        line=dict(color="#e0e0e0", width=2),
        fillcolor="rgba(0,0,0,0)"
    )

    # Add dynamic annotation summary
    total_points = len(df)
    fig.add_annotation(
        x=0.95,
        y=0.98,
        xref="paper",
        yref="paper",
        text=f"<b>Total Points:</b> {total_points:,}<br>"
             f"<b>Marker:</b> {marker_symbol.capitalize()}",
        showarrow=False,
        align="right",
        font=dict(size=12),
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="#d0d0d0",
        borderwidth=1
    )

    return pio.to_json(fig, pretty=True, remove_uids=True)

def get_pie_chart(df, x_col, y_col):
    # Convert y_col to numeric if it's not already
    if not pd.api.types.is_numeric_dtype(df[y_col]):
        # Clean and convert numeric values
        df[y_col] = (
            df[y_col]
            .astype(str)
            .str.replace(r"[^\d.]", "", regex=True)  # Remove non-numeric chars
            .pipe(pd.to_numeric, errors="coerce")
        )
        
        # Remove invalid rows
        df = df.dropna(subset=[y_col])
        if df.empty:
            raise ValueError(f"Column '{y_col}' contains no valid numeric data")

    # Convert x_col to string if it's numeric
    if pd.api.types.is_numeric_dtype(df[x_col]):
        df[x_col] = df[x_col].astype(str).str.replace(r"\.0$", "", regex=True)
        
    # Aggregate data
    grouped_data = df.groupby(x_col)[y_col].sum().sort_values(ascending=False).reset_index()

    # Generate professional color palette
    colors = sns.color_palette("viridis", len(grouped_data))
    hex_colors = [matplotlib.colors.rgb2hex(color) for color in colors]

    # Create interactive pie chart
    fig = px.pie(
        grouped_data,
        names=x_col,
        values=y_col,
        color_discrete_sequence=hex_colors,
        hole=0.3,  # Creates a donut-style chart
        hover_data={y_col: ':,.0f'}
    )

    # Customize traces
    fig.update_traces(
        texttemplate='<b>%{label}</b><br>%{value:,.0f} (%{percent})',
        textposition='auto',
        insidetextorientation='radial',
        marker=dict(
            line=dict(color='white', width=1.5),
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            f"{y_col}: <b>%{{customdata[0]:,.0f}}</b><br>"
            "Percentage: %{percent}<extra></extra>"
        ),
        pull=[0.05 if i == 0 else 0 for i in range(len(grouped_data))]  # Emphasize largest slice
    )

    total_value = float(grouped_data[y_col].sum())  # Ensure numeric type
    total_str = f"{total_value:,.2f}".rstrip('0').rstrip('.')  # Clean format

    # Professional layout configuration
    fig.update_layout(
        title=dict(
            text=f"<span style='font-size:24px; font-weight:600;'>{y_col} Distribution</span><br>"
                 f"<span style='font-size:18px; color:#606060'>by {x_col}</span>",
            x=0.03,
            y=0.95,
            xanchor='left',
            yanchor='top'
        ),
        annotations=[
            dict(
                text=f"Total {y_col}:<br>{total_str}",
                x=0.5,
                y=0.5,
                font_size=16,
                showarrow=False,
                font=dict(color='#606060')
            )
        ],
        plot_bgcolor='white',
        paper_bgcolor='#f8f9fa',
        margin=dict(t=100, b=60, l=60, r=160),
        font=dict(family='Poppins, Arial', color='#404040'),
        legend=dict(
            title=dict(text=f"{x_col}:", font=dict(size=13)),
            orientation='v',
            yanchor='middle',
            xanchor='right',
            x=1.2,
            itemclick=False,
            itemdoubleclick=False
        ),
    )

    return pio.to_json(fig, pretty=True, remove_uids=True)

def get_area_chart(df, x_column, y_column, color_column, chart_title="Area Chart"):
    required_columns = [x_column, y_column, color_column]
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"Error: The following columns are missing from the data: {missing_columns}")
        print(f"Available columns: {list(df.columns)}")
        return
    
    fig = px.area(df, 
                  x=x_column, 
                  y=y_column, 
                  color=color_column,
                  title=chart_title,
                  labels={
                      y_column: f'{y_column.title()} ($)',
                      x_column: x_column.title(),
                      color_column: color_column.title()
                  })
    
    fig.update_layout(
        title={
            'text': chart_title,
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20}
        },
        xaxis_title=x_column.title(),
        yaxis_title=f'{y_column.title()} ($)',
        font=dict(size=12),
        hovermode='x unified',
        width=1000,
        height=600,
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )
    
    fig.update_yaxes(tickformat='$,.0f')
    
    fig.update_traces(
        hovertemplate=f'<b>%{{fullData.name}}</b><br>' +
                     f'{x_column.title()}: %{{x}}<br>' +
                     f'{y_column.title()}: $%{{y:,.0f}}<br>' +
                     '<extra></extra>'
    )

    return pio.to_json(fig, pretty=True, remove_uids=True)


def get_histogram(df, column, step):
    # Ensure numeric data
    df[column] = pd.to_numeric(df[column], errors='coerce')

    # Drop NaNs
    df_clean = df.dropna(subset=[column])

    # Determine bins
    if step is not None:
        min_val = df_clean[column].min()
        max_val = df_clean[column].max()
        buckets = int((max_val - min_val) / float(step))
    else:
        buckets = 5

    # Create bin edges and labels
    bins = pd.cut(df_clean[column], bins=buckets)
    bin_counts = bins.value_counts().sort_index()
    bin_starts = [interval.left for interval in bin_counts.index]
    bin_ends = [interval.right for interval in bin_counts.index]
    bin_labels = [f"{int(start)}–{int(end)}" for start, end in zip(bin_starts, bin_ends)]

    # Create a DataFrame for Plotly Express
    hist_data = pd.DataFrame({
        "Range": bin_labels,
        "Frequency": bin_counts.values
    })

    # Create Plotly Express bar chart
    fig = px.bar(
        hist_data,
        x="Range",
        y="Frequency",
    )

    # Update layout for styling
    fig.update_layout(
        title=dict(
            text=f"<span style='font-size:26px; font-weight:600;'>Histogram of {column.title()}</span><br>"
                 f"<span style='font-size:18px; color:#606060'>{buckets} Bins</span>",
            x=0.03,
            y=0.93,
            xanchor='left',
            yanchor='top'
        ),
        xaxis=dict(
            title=f"{column.title()} Range",
            tickfont=dict(size=14, color='#606060', family='Poppins'),
            showgrid=False,
            linecolor='#d0d0d0'
        ),
        yaxis=dict(
            title="Frequency",
            gridcolor='rgba(200, 200, 200, 0.2)',
            zeroline=False,
            tickfont=dict(size=12, color='#808080')
        ),
        plot_bgcolor='rgba(255, 255, 255, 0.95)',
        paper_bgcolor='#f8f9fa',
        margin=dict(t=120, b=100, l=60, r=40),
        font=dict(family='Poppins, Arial', color='#404040'),
        bargap=0.2,
        bargroupgap=0.05,
        hoverlabel=dict(
            bgcolor='white',
            bordercolor='#404040',
            font_size=14
        ),
        separators=',.',
        annotations=[
            dict(
                x=0.95,
                y=0.98,
                xref='paper',
                yref='paper',
                text=f"<b>Total Samples:</b> {df_clean[column].count():,}<br>"
                     f"<b>Min–Max:</b> {df_clean[column].min():,.0f} – {df_clean[column].max():,.0f}",
                showarrow=False,
                align="right",
                font=dict(size=12),
                bgcolor="rgba(255,255,255,0.9)",
                bordercolor="#d0d0d0",
                borderwidth=1
            )
        ]
    )

    return pio.to_json(fig, pretty=True, remove_uids=True)

def get_bubble(df, x_col, y_col, size_col, category_col):
    # Ensure valid types
    df = df.copy()
    df[size_col] = pd.to_numeric(df[size_col], errors='coerce').fillna(0)

    # Normalize bubble sizes to enhance visual consistency
    size_scale = 3000 * df[size_col] / df[size_col].max()

    # Generate colors using seaborn's palette
    unique_categories = df[category_col].nunique()
    colors = sns.color_palette("viridis", unique_categories)
    hex_colors = [matplotlib.colors.rgb2hex(c) for c in colors]

    # Assign each category a color
    color_map = dict(zip(df[category_col].unique(), hex_colors))
    df['color'] = df[category_col].map(color_map)

    # Create interactive bubble chart
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        size=size_col,
        color=category_col,
        text=category_col,
        size_max=60,
        color_discrete_sequence=hex_colors,
        hover_name=category_col,
        hover_data={x_col: True, y_col: True, size_col: ':.0f'},
        template='plotly_white',
        opacity=0.85
    )

    # Update traces
    fig.update_traces(
        textposition='middle center',
        textfont=dict(size=12, color='black'),
        marker=dict(line=dict(width=1, color='white')),
        selector=dict(mode='markers'),
        hovertemplate=(
            f"<b>%{{hovertext}}</b><br>"
            f"{x_col}: %{{x}}<br>"
            f"{y_col}: %{{y}}<br>"
            f"{size_col}: %{{marker.size:.0f}}<extra></extra>"
        )
    )

    # Update layout to match others
    fig.update_layout(
        title=dict(
            text=f"<span style='font-size:24px; font-weight:600;'>{category_col} Bubble Chart</span><br>"
                 f"<span style='font-size:16px; color:#606060'>Bubble size based on {size_col}</span>",
            x=0.03,
            y=0.95,
            xanchor='left',
            yanchor='top'
        ),
        xaxis=dict(
            title=dict(text=x_col, font=dict(size=14, family='Arial')),
            tickfont=dict(size=12),
            gridcolor='rgba(220,220,220,0.3)'
        ),
        yaxis=dict(
            title=dict(text=y_col, font=dict(size=14, family='Arial')),
            tickfont=dict(size=12),
            gridcolor='rgba(220,220,220,0.3)'
        ),
        plot_bgcolor='white',
        paper_bgcolor='#f8f9fa',
        legend=dict(
            title=dict(text=category_col),
            font=dict(size=12)
        ),
        margin=dict(t=100, b=80, l=60, r=40),
        font=dict(family='Poppins, Arial', color='#404040'),
    )

    return pio.to_json(fig, pretty=True, remove_uids=True)