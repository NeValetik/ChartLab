import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import hashlib
import random
import os

def plot_comparison(df, value_col, category_col):
    plt.figure(figsize=(12, 7))

    # Sort and aggregate data
    grouped_data = df.groupby(category_col)[value_col].sum().sort_values(ascending=False)

    # Use a better colormap
    colors = sns.color_palette("viridis", len(grouped_data))

    # Create bar plot
    bars = plt.bar(grouped_data.index, grouped_data.values, color=colors, alpha=0.85)

    # Add labels on bars
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + max(grouped_data.values) * 0.02,  # Offset for visibility
                 f"{bar.get_height():,.0f}",
                 ha='center', fontsize=11, fontweight='bold', color='black')

    # Improve aesthetics
    plt.xlabel(category_col, fontsize=12, fontweight='bold')
    plt.ylabel(value_col, fontsize=12, fontweight='bold')
    plt.title(f"Comparison of {value_col} across {category_col}", fontsize=14, fontweight='bold', pad=15)
    plt.xticks(rotation=45, ha="right", fontsize=11)

    # Light grid
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    # Remove top and right spines for a cleaner look
    sns.despine()

    # Ensure the output directory exists
    output_dir = "../data/img"
    os.makedirs(output_dir, exist_ok=True)

    # Generate a short random hash
    # In order to avoid overriding images on the same input
    random_hash = hashlib.md5(str(random.random()).encode()).hexdigest()[:8]
    filename = f"{value_col}_vs_{category_col}_{random_hash}.png"
    filepath = os.path.join(output_dir, filename)

    plt.savefig(filepath, bbox_inches="tight", dpi=300)
    plt.close()

    return filepath


def plot_line_graph(df, x_col, y_col):
    # Convert the y_col to datetime if it's not already
    df[y_col] = pd.to_datetime(df[y_col])  # Ensure y_col is datetime

    # Set Seaborn style for better aesthetics
    sns.set(style="whitegrid")

    # Create the plot
    plt.figure(figsize=(12, 6))  # Larger figure size for better clarity
    plt.plot(df[y_col], df[x_col], linestyle='-', color='b', label=f'{x_col} over time', linewidth=2)

    # Improve plot labels, title, and legend
    plt.xlabel(f'{y_col}', fontsize=12, labelpad=15)
    plt.ylabel(f'{x_col}', fontsize=12, labelpad=15)
    plt.title(f'Line Graph of {x_col} Over {y_col}', fontsize=14, fontweight='bold', pad=20)
    plt.legend(loc='upper left', fontsize=11)

    # Rotate x-tick labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Set gridlines and customize them
    plt.grid(True, linestyle='--', alpha=0.6)

    # Ensure the output directory exists
    output_dir = "../data/img"
    os.makedirs(output_dir, exist_ok=True)

    # Generate a short random hash
    # In order to avoid overriding images on the same input
    random_hash = hashlib.md5(str(random.random()).encode()).hexdigest()[:8]
    filename = f"{x_col}_vs_{y_col}_{random_hash}.png"
    filepath = os.path.join(output_dir, filename)

    plt.savefig(filepath, bbox_inches="tight", dpi=300)
    plt.close()

    return filepath
