import matplotlib.pyplot as plt
import numpy as np

# Grouped bar chart with labels
# Color参考:
# https://matplotlib.org/stable/gallery/color/named_colors.html
# https://matplotlib.org/stable/tutorials/colors/colors.html

labels = ['D1', 'D2', 'D3', 'D4']
M1_means = [20, 34, 30, 35]
M2_means = [25, 32, 34, 20]

x = np.arange(len(labels))  # the label locations
width = 0.30  # the width of the bars

fig, ax = plt.subplots()
ax.grid(True, axis='y', color='#9E9E9E', clip_on=False)

rects1 = ax.bar(x - width/2 - 0.02, M1_means, width, color="gray", label='Model-1', zorder=10)
rects2 = ax.bar(x + width/2 + 0.02, M2_means, width, color="silver", label='Model-2', zorder=10)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by Model-1 and Model-2')
ax.set_xticks(x, labels)
ax.legend()

# 条形图/柱状图最上方显示高度值
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
fig.tight_layout()
plt.savefig(f"output/result_2.png")
# plt.show()