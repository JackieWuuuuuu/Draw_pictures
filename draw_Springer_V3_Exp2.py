import matplotlib.pyplot as plt
import numpy as np
import os  # 用于创建目录

# 模型名称
models = ['SSD', 'YOLO', 'YOLOv4', 'YOLOv5', 'Improved\nYOLOv5', 'Proposed\nmethod']

# 模型参数量（单位：百万）
param_counts = [24, 7.1, 63.9, 7.2, 5.8, 1.1]

# 模型mAP值
map_values = [0.0059, 0.0035, 0.1993, 0.1040, 0.2490, 0.2550]

# 创建一个图形对象
fig, ax1 = plt.subplots(figsize=(10, 6))

# 自定义颜色
line_color_mAP = '#6888F5'  # 红色（十六进制颜色）
line_color_param = '#D77071'  # 蓝色（十六进制颜色）

# 设置左侧坐标轴的颜色和字体加粗
ax1.tick_params(axis='y', labelcolor='#6888F5')  # 设置左侧Y轴刻度颜色
ax1.set_ylabel('mAP', fontsize=12, color='#6888F5', fontweight='bold')  # 设置左侧Y轴标签加粗
ax1.plot(models, map_values, marker='o', color=line_color_mAP, linestyle='--', linewidth=2, markersize=8, label='mAP')
ax1.set_xlabel('Models', fontsize=12, fontweight='bold')
# 设置模型名称的字体加粗
ax1.set_xticklabels(models, fontweight='bold')

# 创建右侧坐标轴
ax2 = ax1.twinx()
ax2.tick_params(axis='y', labelcolor='#D77071')  # 设置右侧Y轴刻度颜色
ax2.set_ylabel('Parameters(Millions)', fontsize=12, color='#D77071', fontweight='bold')  # 设置右侧Y轴标签加粗
ax2.plot(models, param_counts, marker='s', color=line_color_param, linestyle='-', linewidth=2, markersize=8, label='Parameters')

# 设置标题和加粗
plt.title('Comparison of Model Parameters and mAP Values', fontsize=14, fontweight='bold')

# 显示图例，右上角的图例移到左上角
ax1.legend(loc='upper left', fontsize=10, bbox_to_anchor=(0, 1))  # 设置左上角位置
ax2.legend(loc='upper left', fontsize=10, bbox_to_anchor=(0, 0.92))  # 设置左上角位置，稍微偏下

# 显示网格
ax1.grid(True)

# 调整布局以避免标签重叠
plt.tight_layout()

# 定义保存路径
output_folder = r'C:\PythonCode\yolov10-main\draw_picture_output'  # 你可以修改为目标文件夹路径
os.makedirs(output_folder, exist_ok=True)  # 如果文件夹不存在，则创建

# 保存图像到指定的文件夹
output_path = os.path.join(output_folder, 'model_comparison_mAP.png')  # 输出文件路径
plt.savefig(output_path)

# 显示图表
plt.show()

# 输出保存路径
print(f"图表已保存到: {output_path}")
