import matplotlib.pyplot as plt
import numpy as np

def create_stacked_bar_chart(data, labels, categories, colors, output_file):
    """
    Example uses fake data.
    Create a stacked bar chart with absolute values and save it as a vector graphics file.

    Parameters:
    - data: Numpy array where each row represents a bar and columns represent categories.
    - labels: List of labels for each bar (one per row in `data`).
    - categories: List of category names (one per column in `data`).
    - colors: List of colors for each category.
    - output_file: String path to save the output vector graphics file.
    """
    # Ensure data is a numpy array
    data = np.array(data)

    # Number of bars (rows) and categories (columns)
    num_bars, num_categories = data.shape

    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Compute the positions for the bars
    bar_positions = np.arange(num_bars)

    # Initialize the bottom positions for stacking
    bottom = np.zeros(num_bars)

    # Plot each category as a stack
    for i in range(num_categories):
        ax.bar(bar_positions, data[:, i], bottom=bottom, color=colors[i], label=categories[i])
        bottom += data[:, i]

    # Add labels, legend, and formatting
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Billion €")
    ax.set_title("Vientiteollisuus Pohjoismaissa 2056 (keksittyä dataa)")
    ax.legend(loc="upper right")

    # Save the plot to a vector graphics file
    plt.tight_layout()
    #plt.savefig(output_file, format="svg")
    plt.savefig(output_file)
    plt.close()

# Example usage
example_points = np.array([
    [14.6, 9.0, 43.0, 10.6],  # Suomi
    [18.6, 12.3, 68.2, 8.9],  # Ruotsi
    [7.9, 5.6, 17.0, 68.7],  # Norja 
    [4.5, 14.5, 8.9, 44.9],   # Tanska
    [6.7, 7.6, 9.8, 38.6]     # Islanti
])

labels = [
    "Suomi",
    "Ruotsi",
    "Norja",
    "Tanska",
    "Islanti"
]

categories = ["Metsäteollisuus", "Maatalous", "Metalliteollisuus", "Muut"]
colors = ["green", "brown", "lightblue", "orange"]

output_file = "stacked_bar_chart.png"
create_stacked_bar_chart(example_points, labels, categories, colors, output_file)
