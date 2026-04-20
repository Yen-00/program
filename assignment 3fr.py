import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # required for 3D projection

# =========================
# Part 0 — Student ID
# =========================

student_id = "2561586"

d1 = int(student_id[-2])
d2 = int(student_id[-1])

k = (d1 + d2) % 4 + 2
shift = d1 - d2
n_points = 20 + d1
frame_step = d2 + 1

print("k =", k)
print("shift =", shift)
print("n_points =", n_points)
print("frame_step =", frame_step)

# =========================
# A1 — 2D Line Plot (x^2)
# =========================

x = list(range(1, n_points + 1))
y = [i**2 for i in x]

if len(x) > 0 and len(x) == len(y):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.title("y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
else:
    print("Error: invalid data in A1")

# =========================
# A2 — Distribution Plot
# =========================

data_values = np.random.normal(50, 10, 50)

print("First 10 values:", data_values[:10])

plt.figure(figsize=(8, 5))
plt.hist(data_values, bins=10)
plt.title("Distribution of Measurements")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# =========================
# B1 — Personalized 2D Plot
# =========================

y2 = [k * i + shift for i in x]

print("First 5 (x, y2):")
for i in range(5):
    print(x[i], y2[i])

plt.figure(figsize=(8, 5))
plt.plot(x, y2, linestyle='--', marker='x')
plt.title(f"ID {student_id} | y = kx + shift | k={k}, shift={shift}")
plt.xlabel("x")
plt.ylabel("y2")
plt.show()

# =========================
# B2 — 3D Scatter Plot
# =========================

y3 = [i + shift for i in x]
z = [k * i for i in x]

print("First 5 (x, y, z):")
for i in range(5):
    print(x[i], y3[i], z[i])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y3, z)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Scatter Plot")

plt.show()

# =========================
# B3 — Animation
# =========================

x_anim = list(range(n_points))
y_anim = [k * i + shift for i in x_anim]

fig, ax = plt.subplots()

line, = ax.plot([], [], lw=2)

ax.set_xlim(0, n_points)
ax.set_ylim(min(y_anim), max(y_anim))

ax.set_title(f"Animation: y = kx + shift | ID {student_id}")

def update(frame):
    print("Animating frame:", frame)
    line.set_data(x_anim[:frame], y_anim[:frame])
    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=range(0, n_points, frame_step),
    repeat=False
)

plt.show()