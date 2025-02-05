import matplotlib.pyplot as plt
import numpy as np

def create_stacked_bar_chart(data, labels, categories, colors, output_file):
    """
    Create a stacked bar chart with absolute values and save it as a vector graphics file.

    Parameters:
    - data: List of tuples/lists, where each sub-list represents a row of data (bars).
    - labels: List of labels for each bar (one per row in `data`).
    - categories: List of category names (one per value in each row of `data`).
    - colors: List of colors for each category.
    - output_file: String path to save the output vector graphics file.
    """
    # Convert data to a numpy array for easier manipulation
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
    ax.set_ylabel("Values")
    ax.set_title("Stacked Bar Chart with Absolute Values")
    ax.legend(loc="upper right")

    # Save the plot to a vector graphics file
    plt.tight_layout()
    plt.savefig(output_file, format="svg")
    plt.close()

# Example usage
"""
five_persons_four_variables = [
    (103, 115, 87, 80, 190),  ## Food
    (512, 432, 390, 698, 580),  ## Rent
    (118, 76, 25, 87, 62),  ## hobbies
    (340, 12, 130, 87, 34),  ## travel expenses   
]
"""

five_persons_four_variables = [
   (103, 115, 87, 80),  ## 1
   (512, 432, 390, 698),  ## 1
  (118, 76, 25, 87),  ## 2
   (340, 12, 130, 87),  ## 4 
   (340, 12, 130, 87),  ## 5
]

labels = [
    "Food expenses",
    "Rent",
    "Hobbies",
    "Travel",
]

categories = ["food", "rent", "hobbies", "travel"]
colors = ["blue", "red", "orange", "green"]

output_file = "stacked_bar_chart.svg"
create_stacked_bar_chart(five_persons_four_variables, labels, categories, colors, output_file)
