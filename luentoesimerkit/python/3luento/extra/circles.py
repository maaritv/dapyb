import matplotlib.pyplot as plt

# Data for pie charts
example_points = [
    (70, 20, 10),  # Focused on Research, blue
    (10, 50, 40),  # Balanced between Marketing and Development, red
    (10, 30, 60),  # Development-heavy, orange
    (30, 30, 40),  # Equally balanced
    (80, 20, 0)    # Only research and marketing
]

titles = [
    "Focused on Research",
    "Balanced (Marketing & Development)",
    "Development-heavy",
    "Equally Balanced",
    "Research and Marketing Only"
]

colors_list = [
    ["blue", "green", "orange"],  # Colors for each section (Research, Marketing, Development)
    ["blue", "green", "orange"],
    ["blue", "green", "orange"],
    ["blue", "green", "orange"],
    ["blue", "green", "orange"]
]

labels = ["Research", "Marketing", "Development"]

# Create subplots for pie charts
fig, axes = plt.subplots(1, len(example_points), figsize=(15, 5))
fig.suptitle("Pie Charts for Different Resource Allocations", fontsize=16)

# Plot each pie chart
for ax, point, title, colors in zip(axes, example_points, titles, colors_list):
    ax.pie(point, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title(title, fontsize=10)

plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to fit the title
plt.savefig("circles.png")
