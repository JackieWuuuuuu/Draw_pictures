import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 模型名称
models = ['EfficientNet-B3', 'Vision Transformer', 'YOLOv5-cls', 'YOLOv8-cls', 'Proposed method']
x = np.arange(len(models))

# 各类别准确率
nodr = [76.66, 71.76, 83.95, 84.49, 91.48]
mild_npdr = [73.85, 71.90, 76.28, 74.44, 81.90]
moderate_npdr = [70.06, 75.12, 68.86, 70.08, 82.53]
severe_npdr = [78.19, 78.31, 79.12, 83.05, 90.68]
pdr = [79.58, 76.59, 80.45, 84.85, 87.40]
data = [nodr, mild_npdr, moderate_npdr, severe_npdr, pdr]

# 类别标签
grades_labels = ['No DR', 'Mild NPDR', 'Moderate NPDR', 'Severe NPDR', 'PDR']

# 定义颜色（RGB归一化）
rgb_colors = [
    (234, 240, 178),
    (200, 226, 178),
    (126, 203, 185),
    (59, 182, 197),
    (29, 145, 194),
]
colors = [(r / 255, g / 255, b / 255) for r, g, b in rgb_colors]

# 创建柱状图
bar_width = 0.15
offsets = np.linspace(-2, 2, len(data)) * bar_width

plt.figure(figsize=(13, 8))
for i, (grade, color) in enumerate(zip(data, colors)):
    bars = plt.bar(x + offsets[i], grade, width=bar_width, label=grades_labels[i], color=color, edgecolor='black', linewidth=0.8)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                 f'{height:.1f}', ha='center', va='bottom', fontsize=9, rotation=90)

# 设置标题和轴标签
plt.title('Grading Accuracy Comparison of Different Models on the IDRiD Dataset',
          fontsize=15, fontweight='bold', pad=20)
plt.xlabel('Models', fontsize=13, labelpad=15)
plt.ylabel('Accuracy (%)', fontsize=13)

# X轴美化
plt.xticks(x, models, fontsize=12, fontname='Arial')
plt.yticks(np.arange(60, 105, 10), fontsize=11)
plt.ylim(60, 105)
plt.tick_params(axis='x', which='major', pad=10)
plt.tick_params(axis='y', which='major', pad=10)

# 添加网格线
plt.grid(axis='y', linestyle='--', linewidth=0.6, alpha=0.7)

# 图例美化
plt.legend(fontsize=11, frameon=True, loc='upper left', bbox_to_anchor=(0.001, 1.0), ncol=1)

# 自适应布局
plt.tight_layout(pad=2.0)

# 保存图像为SVG文件
output_svg_path = r"C:\Users\59104\Desktop\NB\DDR_bar_comparison_pretty.svg"
plt.savefig(output_svg_path, format='svg')
plt.show()

output_svg_path
