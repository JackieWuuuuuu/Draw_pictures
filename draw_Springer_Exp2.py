import matplotlib.pyplot as plt
import numpy as np
import os  # 用于创建目录

# 模型名称
models = ['SSD', 'YOLO', 'YOLOv4', 'YOLOv5', 'Improved\nYOLOv5', 'Proposed\nmethod']

# 模型参数量（单位：百万）
param_counts = [24, 7.1, 63.9, 7.2, 5.8, 1.1]

# recall 和 F1 score 数据（假设的数据）
recall_values = [0.4122, 0.2713, 0.4362, 0.4931, 0.2859, 0.5240]
f1score_values = [0.3871, 0.3120, 0.4228, 0.4723, 0.3485, 0.4900]

# 创建一个图形对象
fig, ax1 = plt.subplots(figsize=(10, 6))

# 自定义颜色
line_color_param = '#9A5747'  # 红色（十六进制颜色）

# 设置左侧坐标轴的颜色和字体加粗
ax1.tick_params(axis='y', labelcolor='#CC141E')  # 设置左侧Y轴刻度颜色
ax1.set_ylabel('Parameters(Millions)', fontsize=12, color='#CC141E', fontweight='bold')  # 设置左侧Y轴标签加粗
ax1.plot(models, param_counts, marker='s', color=line_color_param, linestyle='-', linewidth=2, markersize=8, label='Parameters')
ax1.set_xlabel('Models', fontsize=12, fontweight='bold')
# 设置模型名称的字体加粗
ax1.set_xticklabels(models, fontweight='bold')

# 创建第三个 Y 轴来绘制 Recall 和 F1 Score
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # 设置第三个 Y 轴的位置
ax3.tick_params(axis='y', labelcolor='green')  # 设置第三个Y轴刻度颜色
ax3.set_ylabel('Recall / F1 Score', fontsize=12, color='green', fontweight='bold')  # 设置第三个Y轴标签
ax3.plot(models, recall_values, marker='^', color='green', linestyle='-', linewidth=2, markersize=8, label='Recall')
ax3.plot(models, f1score_values, marker='D', color='orange', linestyle='-', linewidth=2, markersize=8, label='F1 Score')

# 设置图例位置
ax1.legend(loc='upper left', fontsize=10, bbox_to_anchor=(0, 1))  # 设置左上角位置
ax3.legend(loc='upper left', fontsize=10, bbox_to_anchor=(0, 0.92))  # 设置左上角位置，稍微偏下

# 设置标题和加粗
plt.title('Comparison of Model Parameters, Recall and F1 Scores', fontsize=14, fontweight='bold')

# 显示网格
ax1.grid(True)

# 调整布局以避免标签重叠
plt.tight_layout()

# 定义保存路径
output_folder = r'C:\PythonCode\yolov10-main\draw_picture_output'  # 你可以修改为目标文件夹路径
os.makedirs(output_folder, exist_ok=True)  # 如果文件夹不存在，则创建

# 保存图像到指定的文件夹
output_path = os.path.join(output_folder, 'model_comparison_with_recall_f1_removed_mAP1.png')  # 输出文件路径
plt.savefig(output_path)

# 显示图表
plt.show()

# 输出保存路径
print(f"图表已保存到: {output_path}")
