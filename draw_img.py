import matplotlib.pyplot as plt
import numpy as np

line_width = 1
square_width = 5
first_order_length = 3 * line_width + 2 * square_width

canvas = np.zeros((first_order_length, first_order_length)) + 255

# Draw the border
canvas[0, :] = 0
canvas[:, 0] = 0
canvas[-1, :] = 0
canvas[:, -1] = 0
mid = line_width + square_width
canvas[mid, :] = 0
canvas[:, mid] = 0

# Draw the hilbert curve

# Draw first order.
x = int(line_width + 0.5 * (square_width - 1))
canvas[x:-x, x] = 0
canvas[x, x:-x] = 0
canvas[x:-x, -(x + 1)] = 0

# Draw second order.
full_length = 2 * first_order_length - line_width
second_order = np.zeros((full_length, full_length)) + 255
second_order[:first_order_length, :first_order_length] = canvas
second_order[:first_order_length:, -first_order_length:] = canvas
second_order[-first_order_length:, :first_order_length] = np.rot90(canvas, -1)
second_order[-first_order_length:, -first_order_length:] = np.rot90(canvas, 1)

# Connect the first order segments.
second_order[first_order_length - x : first_order_length + x, x] = 0
second_order[first_order_length - x : first_order_length + x, -(x + 1)] = 0
second_order[
    (first_order_length - x - 1), first_order_length - x : first_order_length + x
] = 0

# Show canvas
plt.imshow(second_order, cmap="gray")
plt.show()
