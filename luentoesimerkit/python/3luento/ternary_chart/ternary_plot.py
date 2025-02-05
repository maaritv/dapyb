import matplotlib.pyplot as plt
import ternary

# Esimerkki käyttää kirjastoa python-ternary
# pip3 install python-ternary
# https://github.com/marcharper/python-ternary/tree/master

# Ternary plot parameters
scale = 100  # Scale of the plot (percentage-based)

# Create a figure for ternary plot
fig, ax = plt.subplots(figsize=(10, 10))
figure, tax = ternary.figure(ax=ax, scale=scale)
fig.set_size_inches(15, 15)
tax.set_title("Ternary Plot: Resource Allocation in percents\nBlue: research oriented, Red: marketing and development mostly\nOrange: Development oriented\n", fontsize=16)

# Example problem: Allocation of resources 
# A: Research, B: Marketing, C: Development
example_points = [
    (70, 20, 10),  # Focused on Research, blue
    (10, 50, 40),  # Balanced between Marketing and Development, red
    (10, 30, 60),  # Development-heavy, orange
    (30, 30, 40),  # Equally balanced
    (80, 20, 0)    # Only research and marketing
]

# Plot example points
#for point in example_points:

tax.scatter([example_points[0]], marker='o', color='blue', label=f"Point {example_points[0]}")
tax.scatter([example_points[1]], marker='o', color='red', label=f"Point {example_points[1]}")
tax.scatter([example_points[2]], marker='o', color='orange', label=f"Point {example_points[2]}")
tax.scatter([example_points[3]], marker='o', color='violet', label=f"Point {example_points[3]}")
tax.scatter([example_points[4]], marker='o', color='black', label=f"Point {example_points[4]}")


# Add labels
offset = 0.015
tax.bottom_axis_label("Research", fontsize=12, offset=-0.07)
tax.right_axis_label("Marketing", fontsize=12, offset=0.07)
tax.left_axis_label("Development", fontsize=12, offset=0.07)
tax.left_corner_label("R 100", fontsize=12, offset=0)
tax.top_corner_label("M 100", fontsize=12, offset=0)
tax.right_corner_label("D 100", fontsize=12, offset=0)

# Customize gridlines and boundary
tax.gridlines(color="gray", multiple=10)
tax.gridlines(color="blue", multiple=5)
tax.boundary(linewidth=2.0)
# Display legend
tax.legend()


tax.ticks(axis='lbr', linewidth=1, multiple=5, offset=0.01)
##Ei näytetä oletuskoordinaatiostoa.
tax.clear_matplotlib_ticks()
#tax.get_axes().axis('off')

# Show plot
plt.margins(100, 100)
#plt.autumn()
#plt.autoscale()
plt.tight_layout()
#plt.show()
plt.savefig("ternaryplot.png") 

