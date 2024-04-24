import matplotlib.pyplot as plt
import numpy as np

# Horizontal bar chart
# bar()用来画垂直柱状图，barh()画水平柱状图

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
# fig, ax = plt.subplots()
fig = plt.figure(figsize=(8, 6))
ax = plt.axes()
# 取消边框
ax.spines[:].set_visible(False)
ax.set_axisbelow(True)
ax.grid(True, axis='y', color='#9E9E9E', clip_on=False)

# Example data
models = ('M1', 'M2', 'M3', 'M4', 'M5')
x_pos = np.arange(len(models))
performance = np.random.rand(len(models))
print("***x_pos-ModelSeq***", x_pos)
print("***height-Performance***", performance)

# 误差线: yerr=error 添加误差线; ecolor='red' 误差线颜色; capsize=5 两端线段长短
# error = 0.1 * np.random.rand(len(models))

# x:横坐标序列, height:横坐标对应的纵坐标序列（高度)
# alpha=0.5 透明度; width=0.5 每个条形的宽度;
# color='yellow' 填充前景色; edgecolor='red' 边框颜色; linewidth=3 边框宽度
ax.bar(x_pos, performance, width=0.4, color="green", align='center', label="Dataset1", zorder=10)
ax.set_xticks(x_pos, labels=models)

# ax.set_yticks([0.6, 0.7, 0.8, 0.9, 1.0])
# ax.axhline(0.85, color='red', lw=1.5)

# ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel('Performance')
ax.set_title('The Performance of Different Model')
ax.legend(loc=2, prop={'size': 12})         # 显示图例
plt.savefig(f"output/result_1.png")
# plt.show()