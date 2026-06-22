import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

fig, ax = plt.subplots(figsize=(3, 3))

axis_color = "#9fa3a7"
curve_color = "#f2f2f2"
red = "#e35a50"

def add_bezier(points, color, lw):
    verts = [points[0]]
    codes = [Path.MOVETO]

    for c1, c2, end in points[1:]:
        verts.extend([c1, c2, end])
        codes.extend([Path.CURVE4, Path.CURVE4, Path.CURVE4])

    patch = PathPatch(
        Path(verts, codes),
        facecolor="none",
        edgecolor=color,
        lw=lw,
        capstyle="round",
        joinstyle="round",
    )
    ax.add_patch(patch)

# axes
ax.plot([0.08, 0.08], [0.08, 0.92], color=axis_color, linewidth=4)
ax.plot([0.08, 0.92], [0.08, 0.08], color=axis_color, linewidth=4)

# top gray curve
add_bezier([
    (0.18, 0.62),
    ((0.25, 0.88), (0.38, 0.94), (0.52, 0.80)),
    ((0.66, 0.66), (0.80, 0.68), (0.90, 0.80)),
], curve_color, 5)

# middle gray curve
add_bezier([
    (0.18, 0.36),
    ((0.27, 0.68), (0.40, 0.76), (0.54, 0.62)),
    ((0.68, 0.48), (0.80, 0.49), (0.90, 0.65)),
], curve_color, 5)

# bottom gray curve: broader and different curvature
add_bezier([
    (0.18, 0.18),
    ((0.30, 0.38), (0.48, 0.40), (0.62, 0.28)),
    ((0.76, 0.16), (0.84, 0.16), (0.90, 0.42)),
], curve_color, 5)

# red curve
add_bezier([
    (0.15, 0.50),
    ((0.22, 0.49), (0.27, 0.50), (0.32, 0.56)),
    ((0.38, 0.72), (0.43, 0.83), (0.50, 0.68)),
    ((0.56, 0.52), (0.58, 0.34), (0.66, 0.32)),
    ((0.74, 0.32), (0.78, 0.58), (0.86, 0.62)),
    ((0.89, 0.64), (0.92, 0.60), (0.94, 0.56)),
], red, 5.5)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

plt.tight_layout(pad=0)
plt.savefig("physics_curves_dark_bg.svg", transparent=True)
plt.savefig("physics_curves_dark_bg.png", dpi=300, transparent=True)
plt.show()
