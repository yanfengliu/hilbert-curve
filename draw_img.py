import matplotlib.pyplot as plt
import numpy as np

line_width = 1
square_width = 5
canvas_length = 3 * line_width + 2 * square_width

canvas = np.zeros((canvas_length, canvas_length)) + 255

# Draw the border
canvas[0, :] = 0
canvas[:, 0] = 0
canvas[-1, :] = 0
canvas[:, -1] = 0
mid = line_width + square_width
canvas[mid, :] = 0
canvas[:, mid] = 0

# Draw the hilbert curve

# First order
x = int(line_width + 0.5 * (square_width - 1))
canvas[x:-x, x] = 0
canvas[x, x:-x] = 0
canvas[x:-x, -(x + 1)] = 0

# Show canvas
plt.imshow(canvas, cmap="gray")
plt.show()
