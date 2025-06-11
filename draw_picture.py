import matplotlib.pyplot as plt
import numpy as np
import os

# Data for recall, F1-score, mAP
models = ['YOLOv8n', 'V1', 'V2', 'V3', 'V4']
recall = [0.702, 0.846, 0.804, 0.776, 0.865]
f1_score = [0.760, 0.840, 0.810, 0.820, 0.860]
map_values = [0.833, 0.902, 0.862, 0.876, 0.909]

# Colors
recall_color = (223/255, 232/255, 213/255)
f1_score_color = (156/255, 173/255, 139/255)
map_color = (235/255, 206/255, 192/255)

# Grouped bar chart
x = np.arange(len(models))
bar_width = 0.22

fig, ax1 = plt.subplots(figsize=(15, 10))

# Plot bars for Recall, F1-score, mAP on the left y-axis
bars1 = ax1.bar(x - 1.5 * bar_width, recall, bar_width, label='Recall', color=recall_color, edgecolor='black', linewidth=0.7)
bars2 = ax1.bar(x - 0.5 * bar_width, f1_score, bar_width, label='F1-score', color=f1_score_color, edgecolor='black', linewidth=0.7)
bars3 = ax1.bar(x + 0.5 * bar_width, map_values, bar_width, label='mAP', color=map_color, edgecolor='black', linewidth=0.7)

ax1.set_ylabel('Scores (Recall, F1-score, mAP)', fontsize=16, fontweight='bold')
ax1.set_ylim(0, 1)
ax1.tick_params(axis='y', labelsize=14)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Add labels and title
ax1.set_title('Comparison of Model Performance (Scores)', fontsize=20, fontweight='bold', pad=20)
ax1.set_xticks(x)
ax1.set_xticklabels(models, fontsize=14, rotation=45, ha='right')

# Add legends
ax1.legend([bars1, bars2, bars3], ['Recall', 'F1-score', 'mAP'], loc='upper left', fontsize=14, frameon=False)

# Annotate bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{height:.3f}', (bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 5), textcoords="offset points", ha='center', fontsize=12)

# Add border to the plot
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_linewidth(1.5)
ax1.spines['bottom'].set_linewidth(1.5)

# Adjust layout
fig.tight_layout()

# Save the figure
folder_path = r'C:\PythonCode\yolov10-main\draw_picture_output'
file_name = 'comparison_without_FPS.png'
file_path = os.path.join(folder_path, file_name)

plt.savefig(file_path, bbox_inches='tight', dpi=300)
plt.show()
