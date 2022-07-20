import matplotlib.pyplot as plt
import math

# List that holds x and y coordinates of the two points of original line
points = [[0, 0], [100, 0]]

# How many times should the line be transformed
number_of_iterations = 10


def make_triangle(point_a, point_b):
    """
    Return points A, B and C
    C is the tip of a equilateral triangle constructed from middle third of original AB
    new A and B are first and second third of original AB
    """
    a_x = point_a[0] + (point_b[0] - point_a[0]) / 3
    a_y = point_a[1] + (point_b[1] - point_a[1]) / 3
    b_x = point_a[0] + 2 * ((point_b[0] - point_a[0]) / 3)
    b_y = point_a[1] + 2 * ((point_b[1] - point_a[1]) / 3)
    c_x = (0.5 * (b_x - a_x) - (math.sqrt(3) / 2) * (b_y - a_y)) + a_x
    c_y = (math.sqrt(3) / 2) * (b_x - a_x) + 0.5 * (b_y - a_y) + a_y
    return [[a_x, a_y], [b_x, b_y], [c_x, c_y]]


def next_iteration(arr):
    """
    Add three points between every two points in arr
    """
    i = 0
    while i < len(arr) - 1:
        triangle = make_triangle(arr[i], arr[i + 1])
        arr.insert(i + 1, triangle[1])  # third
        arr.insert(i + 1, triangle[2])  # second
        arr.insert(i + 1, triangle[0])  # first
        i += 4


def draw_line(arr):
    """
    Plot lines between points in arr
    """
    # List to hold x values.
    x_number_values = []

    # List to hold y values.
    y_number_values = []

    # Get x and y values from the arr
    for p in arr:
        x_number_values.append(p[0])
        y_number_values.append(p[1])

    # Plot the number in the list and set the line thickness.
    plt.plot(x_number_values, y_number_values, linewidth=1)

    # Set the line chart title and the text font size.
    plt.title("Koch Curve", fontsize=19)

    # Disable axes
    plt.axis('off')

    # Set aspect ration to equal
    plt.gca().set_aspect("equal")

    # Display the plot in the matplotlib's viewer.
    plt.show()


for i in range(number_of_iterations):
    next_iteration(points)

draw_line(points)
