import numpy as np                 # v 1.19.2
import matplotlib.pyplot as plt    # v 3.3.2
import sys

# Enter x and y coordinates of points and colors
xs = []
ys = []
colors = []


bits = 2
n = 9

def truth_table(bits, n):
    size = 2 ** bits
    binaries = [('0'*(bits-len(bin(x)[2:])))+bin(x)[2:] for x in range(size)]
    binaries = binaries[::-1]
    binary_rep = '0'*(bits**2 - len(bin(n)[2:])) + bin(n)[2:]
    toReturn = []
    for index, binary in enumerate(binaries):
        b = [int(x) for x in binary]
        b = tuple(b)
        output = int(binary_rep[index])
        toAdd = (b, output)
        toReturn.append(toAdd)
    return tuple(toReturn)

step = lambda x: 1 if x > 0 else 0

def perceptron(A, w, b, x):
    return A(sum([i*j for i, j in zip(w, x)]) + b)

def trainer(table): 
    w = [0 for x in range(bits)]
    b = 0
    initial_w = [0 for x in range(bits)]
    initial_b = 0
    for x in range(100):
        for row in table:
            p_output = perceptron(step, w, b, row[0])
            t_output = row[1]
            if p_output != t_output:
                error = t_output - p_output
                b += (t_output - p_output)
                w = [i + j for i, j in zip(w, [x * error for x in row[0]])]
        if initial_w == w and initial_b == b:
            return w, b
        initial_w = w
        initial_b = b
    return w, b

table = truth_table(bits, n)
w, b = trainer(table)
w, b = ((-1, 1), 1)
for xm in range(-20, 20, 1):
    for ym in range(-20, 20, 1):
        x = xm / 10
        y = ym / 10 
        xs.append(x)
        ys.append(y)
        p_output = perceptron(step, w, b, (x, y))
        if p_output == 1:
            colors.append('g')
        else:
            colors.append('r')



# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -2, 2, -2, 2
ticks_frequency = 1

# Plot points
fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(xs, ys, c=colors)

# Set identical scales for both axes
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

# Set bottom and left spines as x and y axes of coordinate system
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Create 'x' and 'y' labels placed at the end of the axes
ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

# Create custom major ticks to determine position of tick labels
x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])

# Create minor ticks placed at each integer to enable drawing of minor grid
# lines: note that this has no effect in this example with ticks_frequency=1
ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

# # Draw arrows
# arrow_fmt = dict(markersize=4, color='black', clip_on=False)
# ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
# ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

plt.show()