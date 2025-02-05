import numpy as np
import matplotlib.pyplot as plt


# Create the line chart
def create_line_chart(title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    # Add labels, title, and legend
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True)
    return plt

def add_line_to_chart(plot, x, y, label, color, filename='linechart.png'):
    plot.plot(x, y, marker='o', label=label, color=color, linewidth=2)
    plot.savefig(filename) 
    
title='Omenien ja päärynöiden myynnin kehitys (2017-2024)'
apple_label='Omenat (euroa)'
pear_label='Päärynät (euroa)'
apple_color='red'
pear_color='blue'
xlabel="Vuosi"
ylabel="Myynti (euroa)"

years = np.arange(2017, 2024)
apple_sales = [2000, 2100, 1900, 2600, 2800, 2700, 3000]  # Npuseva trendi nähtävissä
pear_sales = [4000, 4100, 3800, 3100, 3000, 2500, 2400]   # Laskevaa trendiä

create_line_chart(title, xlabel, ylabel)
add_line_to_chart(plt, years, pear_sales, pear_label, pear_color)
add_line_to_chart(plt, years, apple_sales, apple_label, apple_color)



