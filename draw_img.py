import matplotlib.pyplot as plt
import numpy as np

line_color = np.array([36, 226, 255]) / 255
border_width = 1
curve_width = 3
half_curve_width = (curve_width - 1) // 2
square_width = 15
first_order_length = 3 * border_width + 2 * square_width

canvas = np.zeros((first_order_length, first_order_length, 3)) + 1

# Draw the border
canvas[0, :] = 0
canvas[:, 0] = 0
canvas[-1, :] = 0
canvas[:, -1] = 0
mid = border_width + square_width
canvas[mid, :] = 0
canvas[:, mid] = 0

# Draw the hilbert curve

# Draw first order.
x = int(border_width + 0.5 * (square_width - 1))
canvas[x:-x, (x - half_curve_width) : (x + half_curve_width + 1)] = line_color
canvas[
    (x - half_curve_width) : (x + half_curve_width + 1),
    (x - half_curve_width) : (-x + half_curve_width),
] = line_color
canvas[x:-x, (-(x + 1) - half_curve_width) : (-(x + 1) + half_curve_width + 1)] = (
    line_color
)

# Draw second order.
full_length = 2 * first_order_length - border_width
second_order = np.zeros((full_length, full_length, 3)) + 1
second_order[:first_order_length, :first_order_length] = canvas
second_order[:first_order_length:, -first_order_length:] = canvas
second_order[-first_order_length:, :first_order_length] = np.rot90(canvas, -1)
second_order[-first_order_length:, -first_order_length:] = np.rot90(canvas, 1)

# Connect the first order segments.
second_order[
    (first_order_length - x - half_curve_width) : (
        first_order_length + x + half_curve_width
    ),
    (x - half_curve_width) : (x + half_curve_width + 1),
] = line_color
second_order[
    (first_order_length - x - half_curve_width) : (
        first_order_length + x + half_curve_width
    ),
    (-(x + 1) - half_curve_width) : (-(x + 1) + half_curve_width + 1),
] = line_color
second_order[
    ((first_order_length - x - 1) - half_curve_width) : (
        (first_order_length - x) + half_curve_width
    ),
    (first_order_length - x - half_curve_width - 1) : (
        first_order_length + x + half_curve_width
    ),
] = line_color

# Show canvas
plt.imshow(second_order)
plt.show()
