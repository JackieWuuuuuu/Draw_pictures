import matplotlib.pyplot as plt
import numpy as np
import os

# 定义模型顺序（在 YOLOv5 和 YOLOv8n 之间插入新模型）
models = ['SSD', 'YOLO', 'YOLOv4', 'YOLOv5', 'Santos(2022)', 'Santos(2023)', 'YOLOv8n', 'YOLOv10n', 'Proposed method']

# 每个模型对应的 5 类病灶的 AP 值
data = {
    'SSD': [0, 0.0007, 0, 0.0227, 0],
    'YOLO': [0, 0.0101, 0.0039, 0, 0],
    'YOLOv4': [0.0193, 0.0849, 0.0370, 0.1493, 0],
    'YOLOv5': [0.0047, 0.1300, 0.0306, 0.2500, 0],
    'Santos(2022)': [0.1110, 0.3520, 0.2240, 0.3650, 0],     # ← 你在这里填写 NewModel1 的数据
    'Santos(2023)': [0.2036, 0.3211, 0.3012, 0.3505, 0],  # ← 你在这里填写 NewModel2 的数据
    'YOLOv8n': [0.6790, 0.8810, 0.9120, 0.9550, 0.7190],
    'YOLOv10n': [0.5380, 0.8670, 0.8930, 0.9280, 0.8320],
    'Proposed method': [0.7710, 0.8960, 0.9250, 0.9590, 0.8270]
}

# 设置每类病灶的颜色
colors = [
    (71/255, 138/255, 193/255),   # MA
    (152/255, 201/255, 213/255),  # H
    (138/255, 155/255, 109/255),  # EX
    (228/255, 183/255, 138/255),  # CW
    (193/255, 152/255, 179/255)   # NB
]

x = np.arange(len(models))  # X轴位置
fig, ax = plt.subplots(figsize=(14, 8))

# 绘制每类病灶的折线
for i, category in enumerate(['MA', 'H', 'EX', 'CW', 'NB']):
    ax.plot(x, [data[model][i] for model in models],
            marker='o', label=category, color=colors[i],
            linestyle='-', markersize=10, linewidth=2.5)

# 设置标题和轴标签
ax.set_title('Comparison of AP Values of Different Lesions in Different Models', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Models', fontsize=14, fontweight='bold', labelpad=15)
ax.set_ylabel('AP Value', fontsize=14, fontweight='bold', labelpad=15)

# 设置刻度
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=12, rotation=45, ha='right')
ax.tick_params(axis='y', labelsize=12)

# 网格与图例
ax.grid(True, axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
ax.legend(title='Lesion Types', title_fontsize=14, fontsize=12, loc='upper left', bbox_to_anchor=(1, 1), frameon=False)

# 去除顶部和右侧边框，保留左和下边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

plt.tight_layout(rect=[0, 0, 0.85, 1])

# 保存路径（请根据你自己的目录修改）
save_path = r"C:\Users\59104\Desktop\机器视觉＋边缘计算\论文\论文图\Exp1_line.png"
plt.savefig(save_path, bbox_inches='tight', dpi=300)
plt.show()
