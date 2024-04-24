import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

# fname should be the absolute path, but the positive may be ok!!!
myfont1 = FontProperties(fname="./TIMES.ttf", size=22)


def draw_figrue_1():
    M1 = [0.740, 0.746, 0.748, 0.756, 0.744, 0.750, 0.761, 0.744, 0.742, 0.734]
    M2 = [0.376, 0.384, 0.388, 0.387, 0.377, 0.379, 0.398, 0.373, 0.378, 0.367]
    M3 = [0.489, 0.485, 0.491, 0.489, 0.493, 0.489, 0.502, 0.491, 0.498, 0.494]

    fig, ax = plt.subplots(3, sharex=True, figsize=(8, 6))
    plt.subplots_adjust(hspace=0)

    x_ticks = np.linspace(0.1, 1.0, 10)
    x_labels = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    y_ticks1 = np.linspace(0.72, 0.77, 6)
    y_ticks2 = np.linspace(0.48, 0.51, 4)
    y_ticks3 = np.linspace(0.36, 0.4, 5)
    ax[0].plot(x_labels, M1, 'go-', label="M1")
    ax[1].plot(x_labels, M3, 'b^-', label="M3")
    ax[2].plot(x_labels, M2, 'rv-', label="M2")
    ax[2].set_xticks(x_ticks)
    ax[2].xaxis.set_tick_params(labelsize=14)
    ax[0].set_yticks(y_ticks1)
    ax[1].set_yticks(y_ticks2)
    ax[2].set_yticks(y_ticks3)
    ax[0].yaxis.set_tick_params(labelsize=14)
    ax[1].yaxis.set_tick_params(labelsize=14)
    ax[2].yaxis.set_tick_params(labelsize=14)
    ax[0].set_ylim(0.725, 0.77)
    ax[1].set_ylim(0.475, 0.51)
    ax[2].set_ylim(0.365, 0.4)
    ax[0].tick_params(bottom=False)
    ax[1].tick_params(bottom=False)
    ax[0].spines['bottom'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    ax[1].spines['bottom'].set_visible(False)
    ax[2].spines['top'].set_visible(False)

    # 指定位置进行标注
    for i, txt in enumerate(M1):
        t = ax[0].annotate("%.3f" % txt, (x_labels[i], M1[i] + 0.002), ha='center')
        t.set_fontsize(14)
    for i, txt in enumerate(M3):
        t = ax[1].annotate("%.3f" % txt, (x_labels[i], M3[i] + 0.002), ha='center')
        t.set_fontsize(14)
    for i, txt in enumerate(M2):
        t = ax[2].annotate("%.3f" % txt, (x_labels[i], M2[i] + 0.002), ha='center')
        t.set_fontsize(14)

    # 绘制断层线
    d = .005
    kwargs = dict(transform=ax[0].transAxes, color='k', clip_on=False)
    ax[0].plot((-d, +d), (-d, +d), **kwargs)        # 左边框
    ax[0].plot((1 - d, 1 + d), (-d, +d), **kwargs)   # 右边框

    kwargs.update(transform=ax[1].transAxes)
    ax[0].plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax[0].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    # kwargs = dict(transform=ax[1].transAxes, color='k', clip_on=False)
    # ax[1].plot((-d, +d), (-d, +d), **kwargs)
    # ax[1].plot((1 - d, 1 + d), (-d, +d), **kwargs)

    kwargs.update(transform=ax[2].transAxes)
    ax[1].plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax[1].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    ax[0].grid(alpha=0.8, linestyle='-')
    ax[0].legend(prop={'size': 16})
    ax[1].grid(alpha=0.8, linestyle='-')
    ax[1].legend(prop={'size': 16}, loc="upper left")
    ax[2].grid(alpha=0.8, linestyle='-')
    ax[2].legend(prop={'size': 16})
    plt.xlabel(r'$\lambda$', fontsize=14)
    plt.tight_layout()
    plt.show()
    plt.savefig("output/figure1.png")


draw_figrue_1()