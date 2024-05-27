import matplotlib.pyplot as plt
import numpy as np

# Parameters
order = 4
line_color = np.array([36, 226, 255]) / 255
border_width = 1
curve_width = 3
half_curve_width = (curve_width - 1) // 2
square_width = 15
first_order_length = 3 * border_width + 2 * square_width
x = int(border_width + 0.5 * (square_width - 1))
draw_grid = False
draw_border = True


def get_1st_order_hc():
    canvas = np.zeros((first_order_length, first_order_length, 3)) + 1

    # Draw the grid
    if draw_grid:
        mid = border_width + square_width
        canvas[mid, :] = 0
        canvas[:, mid] = 0

    # Draw first order.
    canvas[x:-x, (x - half_curve_width) : (x + half_curve_width + 1)] = line_color
    canvas[
        (x - half_curve_width) : (x + half_curve_width + 1),
        (x - half_curve_width) : (-x + half_curve_width),
    ] = line_color
    canvas[x:-x, (-(x + 1) - half_curve_width) : (-(x + 1) + half_curve_width + 1)] = (
        line_color
    )
    return canvas


def recursive_hc(order: int):
    if order < 1 or not isinstance(order, int):
        raise ValueError("Order must be a positive integer.")
    if order == 1:
        return get_1st_order_hc()
    else:
        prev_order = recursive_hc(order - 1)
        length = prev_order.shape[0]
        full_length = 2 * length - border_width
        img = np.zeros((full_length, full_length, 3)) + 1
        img[:length, :length] = prev_order
        img[:length:, -length:] = prev_order
        img[-length:, :length] = np.rot90(prev_order, -1)
        img[-length:, -length:] = np.rot90(prev_order, 1)

        # Connect the previous order segments.
        img[
            (length - x - half_curve_width) : (length + x + half_curve_width),
            (x - half_curve_width) : (x + half_curve_width + 1),
        ] = line_color
        img[
            (length - x - half_curve_width) : (length + x + half_curve_width),
            (-(x + 1) - half_curve_width) : (-(x + 1) + half_curve_width + 1),
        ] = line_color
        img[
            ((length - x - 1) - half_curve_width) : ((length - x) + half_curve_width),
            (length - x - half_curve_width - 1) : (length + x + half_curve_width),
        ] = line_color

        return img


final_img = recursive_hc(order)

# Draw the border
if draw_border:
    final_img[0, :] = 0
    final_img[:, 0] = 0
    final_img[-1, :] = 0
    final_img[:, -1] = 0

# Show canvas
plt.imshow(final_img)
plt.show()
