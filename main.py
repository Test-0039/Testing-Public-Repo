import matplotlib.pyplot as plt
import numpy as np

labels = [
    "aaaa", "bbbb", "cccc", "dddd", 
    "eeee", "ffff", "gggg", "hhhh"
]
values = [0.36, 0.20, 0.11, 0.01, 0.08, 0.14, 0.09, 0.01]
colors = ["#3b82f6", "#60a5fa", "#93c5fd", "#bfdbfe", "#2563eb", "#1e40af", "#1e3a8a", "#172554"]

total = sum(values)
print(total)
angles = np.array(values) / total * 360

label_distance = 1.5
line_distance = 0.9
line_length = 0.6

def get_label_position(start_angle, angle):
    mid_angle = np.radians(start_angle - angle / 2)

    label_x = label_distance * np.cos(mid_angle)
    label_y = label_distance * np.sin(mid_angle)

    line_x_start = (line_distance + 0.05) * np.cos(mid_angle)
    line_y_start = (line_distance + 0.05) * np.sin(mid_angle)

    line_x_end = line_x_start + (line_length / np.sqrt(2)) * np.cos(mid_angle)
    line_y_end = line_y_start + (line_length / np.sqrt(2)) * np.sin(mid_angle)

    return label_x, label_y, line_x_start, line_y_start, line_x_end, line_y_end

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts = ax.pie(
    values, labels=None, colors=colors, startangle=90, counterclock=False,
    wedgeprops={"width": 0.3, "edgecolor": "white"}
)

start_angle = 90
for i, (wedge, angle, label) in enumerate(zip(wedges, angles, labels)):
    label_x, label_y, line_x_start, line_y_start, line_x_end, line_y_end = get_label_position(start_angle, angle)

    ax.text(label_x, label_y, f"{label}\n{values[i]}", ha='center', va='center', fontsize=10, color='blue')
    
    ax.plot([line_x_start, line_x_end], [line_y_start, line_y_end], color='blue', linewidth=1.2)

    start_angle -= angle

plt.title("jjjj", fontsize=14, y=0.5)
plt.show()
