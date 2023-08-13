import numpy as np
import matplotlib.pyplot as plt

# Vertices of the triangle
vertices = {'A': (1, -1), 'B': (-4, 6), 'C': (-3, -5)}

# Equations of the lines
# Ax + By + C = 0 => y = (-A/B)x - (C/B)
equations = [
    (1, -11, 9),     # x - 11y + 9 = 0
    (-5, 7, -25),    # -5x + 7y - 25 = 0
    (1, 1, 4)        # x + y + 4 = 0
]

# Create a plot
plt.figure()

# Plot each line
for A, B, C in equations:
    x_vals = np.linspace(-10, 10, 400)  # Generate x values
    y_vals = (-A/B) * x_vals - (C/B)    # Calculate y values based on the equation
    plt.plot(x_vals, y_vals, label=f'{A}x + {B}y + {C} = 0')

#'O' is the point of intersection of the perpendicular bisectors of all sides
O_x = -53/12
O_y = 5/12

# Plot the intersection point 'O'
plt.plot(O_x, O_y, 'go')  # 'go' means green circle
plt.text(O_x, O_y, ' O', verticalalignment='bottom', horizontalalignment='right')

# Extract coordinates
x_coords = [v[0] for v in vertices.values()]
y_coords = [v[1] for v in vertices.values()]

# Plot the vertices
plt.plot(x_coords, y_coords, 'ro')  # 'ro' means red circles

# Connect the vertices to form the triangle
plt.plot([x_coords[0], x_coords[1]], [y_coords[0], y_coords[1]], 'b-')  # 'b-' means blue line
plt.plot([x_coords[1], x_coords[2]], [y_coords[1], y_coords[2]], 'b-')
plt.plot([x_coords[2], x_coords[0]], [y_coords[2], y_coords[0]], 'b-')

# Add labels to vertices
for vertex, (x, y) in vertices.items():
    plt.text(x, y, f' {vertex}({x}, {y})')

# Set axis labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')


# Add legend
plt.legend()

# Display the plot
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.show()
