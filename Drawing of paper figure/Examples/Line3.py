import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

myfont3 = FontProperties(fname='./LinLibertine_R.ttf', size=22)
myfont4 = FontProperties(fname='./LinLibertine_R.ttf', size=26)


def draw_figure_5():
    pmr_5_pred = [8.23, 12.54, 15.01, 14.78, 15.05, 14.74]
    pmr_5_ground = [33.85, 65.88, 89.50, 100.0, 100.0, 100.0]
    pmr_3_pred = [10.72, 17.57, 18.42, 18.44, 18.75, 18.89]
    pmr_3_ground = [60.47, 100.0, 100.0, 100.0, 100.0, 100.0]
    pmr_2_pred = [17.33, 17.53, 17.43, 17.59, 17.53, 17.61]
    pmr_2_ground = [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
    x_labels = [1, 2, 3, 4, 5, 6]

    fig, ax = plt.subplots(2, sharex=True, figsize=(9, 6))
    plt.subplots_adjust(hspace=0.01)

    y_ticks1 = np.linspace(30, 100, 8)
    y_ticks2 = np.linspace(6, 20, 8)

    ax[1].plot(x_labels, pmr_5_pred, 'o-', label=r'$d=1$')
    ax[1].plot(x_labels, pmr_3_pred, 'o-', label=r'$d=2$')
    ax[1].plot(x_labels, pmr_2_pred, 'o-', label=r'$d=4$')
    ax[0].plot(x_labels, pmr_5_ground, 'o--', label=r'$d=1$ ground-turth')
    ax[0].plot(x_labels, pmr_3_ground, 'o--', label=r'$d=2$ ground-turth')
    ax[0].plot(x_labels, pmr_2_ground, 'o--', label=r'$d=4$ ground-turth')

    ax[1].xaxis.set_tick_params(labelsize=14)
    ax[0].set_yticks(y_ticks1)
    ax[1].set_yticks(y_ticks2)
    ax[0].yaxis.set_tick_params(labelsize=14)
    ax[1].yaxis.set_tick_params(labelsize=14)
    ax[0].tick_params(bottom=False)
    ax[0].spines['bottom'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    d = .008
    kwargs = dict(transform=ax[0].transAxes, color='k', clip_on=False)
    ax[0].plot((-d, +d), (-d, +d), **kwargs)
    ax[0].plot((1 - d, 1 + d), (-d, +d), **kwargs)
    kwargs.update(transform=ax[1].transAxes)
    ax[0].plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax[0].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    ax[0].grid(alpha=0.8, linestyle='-')
    legend = ax[0].legend(prop={'size': 15}, title='PMR')
    legend.get_title().set_fontsize('15')
    ax[1].grid(alpha=0.8, linestyle='-')
    legend = ax[1].legend(prop={'size': 15}, title='PMR')
    legend.get_title().set_fontsize('15')

    plt.xlabel(r'$L$', fontsize=16)
    plt.tight_layout()
    plt.savefig('output/figure5.png')
    plt.show()


draw_figure_5()