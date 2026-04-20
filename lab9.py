import numpy as np
import matplotlib.pyplot as plt


# Function 1: Curve Plotting
def plot_curve(x_values, y_values):
    """
    Plots a curve using the given x and y values.
    """
    plt.figure()
    plt.plot(x_values, y_values, marker='o', linestyle='-')
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Curve Plot")
    plt.grid(True)
    plt.show()


# Function 2: Hertzsprung-Russell Diagram
def plot_hr_diagram(temperature, luminosity):
    """
    Plots a Hertzsprung-Russell diagram with temperature on the x-axis
    (decreasing) and luminosity on the y-axis.
    """
    plt.figure()
    plt.scatter(temperature, luminosity, c=temperature, cmap='plasma', edgecolors='k')
    plt.gca().invert_xaxis()
    plt.xlabel("Temperature (K)")
    plt.ylabel("Luminosity (L☉)")
    plt.title("Hertzsprung-Russell Diagram")
    plt.colorbar(label="Temperature (K)")
    plt.show()


# Function 3: Heat Map and Density Plot
def plot_density(data, color_map='gray'):
    """
    Creates a density plot using a heat map with a chosen color scheme.
    """
    plt.figure()
    data = np.array(data)
    plt.hist2d(data[:, 0], data[:, 1], bins=50, cmap=color_map, density=True)
    plt.colorbar(label="Density")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Density Plot")
    plt.show()


# Example usage (only runs when you execute this file directly)
if __name__ == "__main__":
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plot_curve(x, y)

    temp = np.array([3000, 5000, 7000, 9000, 11000])
    lum = np.array([0.1, 1, 10, 100, 1000])
    plot_hr_diagram(temp, lum)

    np.random.seed(0)
    data = np.random.randn(1000, 2)
    plot_density(data, 'hot')